const apiUrl = window.location.origin.includes("localhost")
    ? "http://127.0.0.1:8080"
    : "https://ksiazki-api.herokuapp.com";

// Funkcje pomocnicze
async function apiCall(url, options = {}) {
    try {
        const response = await fetch(url, options);
        if (response.ok) {
            return response;
        } else {
            const error = await response.json();
            new Error(error.detail || 'Błąd API');
        }
    } catch (error) {
        alert(`Błąd: ${error.message}`);
        throw error;
    }
}

function showMessage(msg) {
    alert(msg);
}

function clearInputs(...ids) {
    ids.forEach(id => document.getElementById(id).value = '');
}

// KSIĄŻKI
async function dodajKsiazke() {
    const tytul = document.getElementById("tytul").value.trim();
    const autor = document.getElementById("autor").value.trim();
    const rok = document.getElementById("rok").value.trim();

    if (!tytul || !autor || !rok) {
        return showMessage("Proszę uzupełnić wszystkie pola!");
    }

    try {
        await apiCall(`${apiUrl}/ksiazki/`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ id: Date.now(), tytul, autor, rok, dostepna: true })
        });

        showMessage("Książka dodana!");
        clearInputs("tytul", "autor", "rok");
        await pobierzKsiazki();
    } catch (error) {
        // Błąd już obsłużony w apiCall
    }
}

async function pobierzKsiazki() {
    const response = await fetch(`${apiUrl}/ksiazki/`);
    const ksiazki = await response.json();

    const listaKsiazek = document.getElementById("ksiazki");
    listaKsiazek.innerHTML = "";

    ksiazki.forEach(ksiazka => {
        const element = document.createElement("li");

        const tekstKsiazki = document.createElement("span");
        tekstKsiazki.textContent = `${ksiazka.tytul} - ${ksiazka.autor} (${ksiazka.rok}) - ${ksiazka.dostepna ? "✅ Dostępna" : "❌ Wypożyczona"}`;

        const przyciskZwrotu = document.createElement("button");
        przyciskZwrotu.textContent = "🔄 Zwróć";
        przyciskZwrotu.onclick = () => otworzZwrot(ksiazka.tytul);

        const przyciskUsun = document.createElement("button");
        przyciskUsun.textContent = "🗑 Usuń";
        przyciskUsun.onclick = () => usunKsiazke(ksiazka.tytul);

        element.appendChild(tekstKsiazki);
        element.appendChild(przyciskZwrotu);
        element.appendChild(przyciskUsun);
        listaKsiazek.appendChild(element);
    });
}

function otworzZwrot(nazwaKsiazki) {
    document.getElementById("zwrotContainer").style.display = "block";
    document.getElementById("zwrotKsiazka").textContent = `Zwracasz książkę: ${nazwaKsiazki}`;
    document.getElementById("emailZwrot").focus();
}

function zamknijZwrot() {
    document.getElementById("zwrotContainer").style.display = "none";
}

async function usunKsiazke(nazwaKsiazki) {
    if (!confirm(`Czy na pewno chcesz usunąć książkę: ${nazwaKsiazki}?`)) return;

    try {
        const response = await fetch(`${apiUrl}/ksiazki/usun/?nazwa_ksiazki=${encodeURIComponent(nazwaKsiazki)}`, {
            method: "DELETE"
        });

        if (!response.ok) {
            const errorData = await response.json();
            alert(`Błąd: ${errorData.detail}`);
            return;
        }

        alert("📖 Książka usunięta!");
        await pobierzKsiazki(); // Automatyczne odświeżenie listy książek
    } catch (error) {
        console.error("❌ Błąd połączenia:", error);
        alert("Nie udało się połączyć z serwerem!");
    }
}

async function potwierdzZwrot() {
    const nazwaKsiazki = document.getElementById("zwrotKsiazka").textContent.replace("Zwracasz książkę: ", "").trim();
    const emailUzytkownika = document.getElementById("emailZwrot").value.trim();

    if (!emailUzytkownika) {
        alert("Podaj e-mail!");
        return;
    }

    try {
        const response = await fetch(`${apiUrl}/wypozyczenia/zwroc/`, {
            method: "PUT",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ nazwa_ksiazki: nazwaKsiazki, email_uzytkownika: emailUzytkownika })
        });

        if (!response.ok) {
            const errorData = await response.json();
            alert(`Błąd: ${errorData.detail}`);
            return;
        }

        alert("📖 Książka zwrócona!");
        await pobierzKsiazki();
        zamknijZwrot();
    } catch (error) {
        console.error("❌ Błąd połączenia:", error);
        alert("Nie udało się połączyć z serwerem!");
    }
}

// WYSZUKIWANIE
async function wyszukajKsiazke() {
    const tytul = document.getElementById("szukajTytul").value.trim();
    const autor = document.getElementById("szukajAutor").value.trim();

    if (!tytul && !autor) {
        document.getElementById("wyniki").innerHTML = "";
        return;
    }

    try {
        let url = `${apiUrl}/ksiazki/szukaj/?`;
        if (tytul) url += `tytul=${encodeURIComponent(tytul)}&`;
        if (autor) url += `autor=${encodeURIComponent(autor)}`;

        const response = await fetch(url);
        const wyniki = await response.json();

        const lista = document.getElementById("wyniki");
        lista.innerHTML = wyniki.length === 0
            ? "<li>Brak wyników.</li>"
            : wyniki.map(k => `<li>${k.tytul} - ${k.autor} (${k.rok})</li>`).join("");

    } catch (error) {
        showMessage("Błąd wyszukiwania!");
    }
}

// UŻYTKOWNICY
async function dodajUzytkownika() {
    const imie = document.getElementById("imie").value.trim();
    const email = document.getElementById("email").value.trim();

    if (!imie || !email) {
        alert("Podaj imię i e-mail!");
        return;
    }

    try {
        const response = await fetch(`${apiUrl}/uzytkownicy/`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
                id: Date.now(), // Dodanie id użytkownika
                imie,
                email
            })
        });

        if (!response.ok) {
            let errorData;
            try {
                errorData = await response.json();
            } catch (err) {
                errorData = { detail: "Nieznany błąd serwera" };
            }
            console.error("Błąd serwera:", errorData);
            alert(`Błąd: ${JSON.stringify(errorData)}`);
            return;
        }

        alert("Użytkownik dodany!");
        await pobierzUzytkownikow();
    } catch (error) {
        console.error("Błąd połączenia:", error);
        alert("Nie udało się połączyć z serwerem.");
    }
}

async function usunUzytkownika(id) {
    try {
        await apiCall(`${apiUrl}/uzytkownicy/${id}`, { method: "DELETE" });
        showMessage("Użytkownik usunięty!");
        await pobierzUzytkownikow();
    } catch (error) {
        // Błąd już obsłużony w apiCall
    }
}

async function pobierzUzytkownikow() {
    try {
        const response = await fetch(`${apiUrl}/uzytkownicy/`);
        const uzytkownicy = await response.json();

        const lista = document.getElementById("uzytkownicy");
        lista.innerHTML = "";

        uzytkownicy.forEach(u => {
            const li = document.createElement("li");
            li.textContent = `${u.imie} - ${u.email}`;

            const btnUsun = document.createElement("button");
            btnUsun.textContent = "❌ Usuń";
            btnUsun.onclick = () => usunUzytkownika(u.id);

            li.appendChild(btnUsun);
            lista.appendChild(li);
        });
    } catch (error) {
        showMessage("Błąd pobierania użytkowników!");
    }
}

async function wypozyczKsiazke() {
    const nazwaKsiazki = document.getElementById("nazwaKsiazki").value.trim();
    const emailUzytkownika = document.getElementById("emailUzytkownika").value.trim();

    if (!nazwaKsiazki || !emailUzytkownika) {
        alert("Podaj nazwę książki i e-mail!");
        return;
    }

    try {
        const response = await fetch(`${apiUrl}/wypozyczenia/wypozycz/`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ nazwaKsiazki: nazwaKsiazki, emailUzytkownika: emailUzytkownika })
        });

        if (response.ok) {
            alert("Książka wypożyczona!");
            await pobierzKsiazki();  // 💡 Automatyczne odświeżenie listy książek
        } else {
            const errorData = await response.json();
            alert(`Błąd: ${errorData.detail}`);
        }
    } catch (error) {
        alert("Błąd połączenia z serwerem!");
    }
}

function formatDate(dateString) {
    if (!dateString) return "Nie zwrócono";  // Obsługa pustych wartości
    const date = new Date(dateString);
    return date.toLocaleString("pl-PL");
}

async function pobierzHistorie() {
    const emailUzytkownika = document.getElementById("emailUzytkownikaHistoria").value.trim();
    if (!emailUzytkownika) {
        alert("Podaj e-mail użytkownika!");
        return;
    }

    const response = await fetch(`${apiUrl}/wypozyczenia/historia/${encodeURIComponent(emailUzytkownika)}`);
    const historia = await response.json();

    const listaHistoria = document.getElementById("listaHistoria");
    listaHistoria.innerHTML = "";

    historia.historia.forEach(w => {
        const element = document.createElement("li");
        element.textContent = `📖 ${w.nazwaKsiazki} | Wypożyczono: ${formatDate(w.wypozyczono_date)} | Zwrot: ${w.return_date ? formatDate(w.return_date) : "Nie zwrócono"}`;
        listaHistoria.appendChild(element);
    });
}


// INICJALIZACJA
window.onload = () => {
    pobierzKsiazki().then();
    pobierzUzytkownikow().then();

    // Event listenery dla wyszukiwania
    document.getElementById("szukajTytul").addEventListener("input", wyszukajKsiazke);
    document.getElementById("szukajAutor").addEventListener("input", wyszukajKsiazke);
    document.getElementById("dodajUzytkownika").onclick = dodajUzytkownika;
};