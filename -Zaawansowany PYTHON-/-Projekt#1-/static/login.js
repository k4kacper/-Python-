// login.js
const API = "/api";
const $ = id => document.getElementById(id);
const notify = (text) => {
  const n = document.createElement("div");
  n.className = "notification";
  n.textContent = text;
  document.querySelector(".notifications").prepend(n);
  setTimeout(()=> n.remove(), 6000);
};

async function login(){
  const username = $("username").value.trim();
  const password = $("password").value;
  if(!username || !password) { notify("Wpisz nazwę i hasło"); return; }

  try {
    const res = await fetch(`${API}/login`, {
      method: "POST",
      headers: {"Content-Type":"application/json"},
      body: JSON.stringify({username, password})
    });
    if(!res.ok){
      const err = await res.json();
      notify(err.detail || "Błąd logowania");
      return;
    }
    const data = await res.json();
    // zapamiętaj użytkownika w sessionStorage i przejdź do dashboard
    sessionStorage.setItem("me", data.username);
    // opcjonalnie zapisz saldo początkowe
    sessionStorage.setItem("balance", data.balance);
    window.location.href = "/static/dashboard.html";
  } catch(e){
    notify("Błąd sieci");
  }
}

$("btnLogin").addEventListener("click", login);

// enter key
["username","password"].forEach(id => {
  document.getElementById(id).addEventListener("keydown", e => {
    if(e.key === "Enter") login();
  });
});
