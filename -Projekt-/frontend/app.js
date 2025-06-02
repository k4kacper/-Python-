const apiUrl = window.location.origin.includes("localhost")
    ? "http://127.0.0.1:8080"
    : "";

async function apiCall(url, options = {}) {
    try {
        const response = await fetch(url, options);
        if (response.ok) {
            return response;
        } else {
            const error = await response.json();
            throw new Error(error.detail || 'Błąd API');
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

        const kontenerPrzyciskow = document.createElement("div");
        kontenerPrzyciskow.className = "kontener-przyciskow";

        const przyciskZwrotu = document.createElement("button");
        przyciskZwrotu.textContent = "🔄 Zwróć";

        if (ksiazka.dostepna) {
            przyciskZwrotu.disabled = true;
            przyciskZwrotu.style.opacity = "0.5";
            przyciskZwrotu.style.cursor = "not-allowed";
        } else {
            przyciskZwrotu.onclick = () => otworzZwrot(ksiazka.tytul);
        }

        const przyciskUsun = document.createElement("button");
        przyciskUsun.textContent = "🗑 Usuń";
        przyciskUsun.onclick = () => usunKsiazke(ksiazka.tytul);

        kontenerPrzyciskow.appendChild(przyciskZwrotu);
        kontenerPrzyciskow.appendChild(przyciskUsun);

        element.appendChild(tekstKsiazki);
        element.appendChild(kontenerPrzyciskow);
        listaKsiazek.appendChild(element);
    });
}

function otworzZwrot(nazwaKsiazki) {
    document.getElementById("zwrotContainer").style.display = "block";
    document.getElementById("zwrotKsiazka").textContent = `Zwracasz książkę: ${nazwaKsiazki}`;
    document.getElementById("emailZwrot").value = "";
    document.getElementById("emailZwrot").focus();
}

function zamknijZwrot() {
    document.getElementById("zwrotContainer").style.display = "none";
    clearInputs("emailZwrot");
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
        await pobierzKsiazki();
    } catch (error) {
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
            : wyniki.map(k => `<li>${k.tytul} - ${k.autor} (${k.rok}) - ${k.dostepna ? "✅ Dostępna" : "❌ Wypożyczona"}</li>`).join("");

    } catch (error){
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
                id: Date.now(),
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
            alert(`Błąd: ${errorData.detail}`);
            return;
        }

        alert("Użytkownik dodany!");
        clearInputs("imie", "email");
        await pobierzUzytkownikow();
    } catch (error){
    }
}

async function usunUzytkownika(id) {
    if (!confirm("Czy na pewno chcesz usunąć tego użytkownika?")) return;

    try {
        await apiCall(`${apiUrl}/uzytkownicy/${id}`, { method: "DELETE" });
        showMessage("Użytkownik usunięty!");
        await pobierzUzytkownikow();
    } catch (error) {
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

            const tekst = document.createElement("span");
            tekst.textContent = `${u.imie} - ${u.email}`;
            tekst.style.flex = "1";

            const btnUsun = document.createElement("button");
            btnUsun.textContent = "❌ Usuń";
            btnUsun.onclick = () => usunUzytkownika(u.id);

            li.appendChild(tekst);
            li.appendChild(btnUsun);
            lista.appendChild(li);
        });
    } catch (error){
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
            clearInputs("nazwaKsiazki", "emailUzytkownika");
            await pobierzKsiazki();
        } else {
            const errorData = await response.json();
            alert(`Błąd: ${errorData.detail}`);
        }
    } catch (error){
    }
}
async function pobierzHistorie() {
    const emailUzytkownika = document.getElementById("emailUzytkownikaHistoria").value.trim();
    if (!emailUzytkownika) {
        alert("Podaj e-mail użytkownika!");
        return;
    }

    try {
        const response = await fetch(`${apiUrl}/wypozyczenia/historia/${encodeURIComponent(emailUzytkownika)}`);
        const historia = await response.json();
        historia.historia = undefined;

        const listaHistoria = document.getElementById("listaHistoria");
        listaHistoria.innerHTML = "";

        const element = document.createElement("li");
        element.textContent = "Brak historii wypożyczeń dla tego użytkownika.";
        listaHistoria.appendChild(element);
    } catch (error){
    }
}
function wyczyscHistorie() {
    const listaHistoria = document.getElementById("listaHistoria");
    listaHistoria.innerHTML = "<li>🗑 Historia została wyczyszczona.</li>";
}

window.onload = () => {
    pobierzKsiazki();
    pobierzUzytkownikow();
    document.getElementById("szukajTytul").addEventListener("input", wyszukajKsiazke);
    document.getElementById("szukajAutor").addEventListener("input", wyszukajKsiazke);
    document.getElementById("dodajUzytkownika").onclick = dodajUzytkownika;
};