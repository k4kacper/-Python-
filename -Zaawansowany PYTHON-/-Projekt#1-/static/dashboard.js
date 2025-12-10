// dashboard.js — REST + WS + historia
const API = "/api";
let me = sessionStorage.getItem("me");
let ws = null;

const $ = id => document.getElementById(id);
const notify = (text) => {
  const n = document.createElement("div");
  n.className = "notification";
  n.textContent = text;
  const container = document.getElementById("notifications") || document.body;
  container.prepend(n);
  setTimeout(()=> n.remove(), 7000);
};

if(!me){
  window.location.href = "/static/index.html";
} else {
  // show user in sidebar if exists
  const meEl = $("me");
  if(meEl) meEl.textContent = me;
  init();
}

async function init(){
  await fetchUsers();
  await refreshBalance();
  await fetchHistory(80); // pobierz do 80 najnowszych
  connectWS();
}

async function fetchUsers(){
  try{
    const res = await fetch(`${API}/users`);
    if(res.ok){
      const users = await res.json();
      const ul = $("users");
      if(!ul) return;
      ul.innerHTML = "";
      users.forEach(u => {
        const li = document.createElement("li");
        li.className = "user-row";
        li.innerHTML = `<div>${u.username}</div><div class="small">${u.balance.toFixed(2)} PLN</div>`;
        ul.appendChild(li);
      });
    }
  }catch(e){
    notify("Błąd pobierania listy użytkowników");
  }
}

async function refreshBalance(){
  try{
    const res = await fetch(`${API}/balance/${encodeURIComponent(me)}`);
    if(res.ok){
      const data = await res.json();
      const el = $("balance");
      if(el) el.textContent = data.balance.toFixed(2) + " PLN";
    }
  }catch(e){
    notify("Błąd odświeżania salda");
  }
}

async function doTransfer(){
  const to = $("to") ? $("to").value.trim() : "";
  const amount = $("amount") ? parseFloat($("amount").value) : 0;
  if(!to || !amount || amount <= 0) { notify("Nieprawidłowe dane przelewu"); return; }
  try{
    const res = await fetch(`${API}/transfer`, {
      method:"POST",
      headers: {"Content-Type":"application/json"},
      body: JSON.stringify({from_user: me, to, amount})
    });
    if(!res.ok){
      const err = await res.json();
      notify(err.detail || "Błąd przelewu");
      return;
    }
    const data = await res.json();
    const balEl = $("balance");
    if(balEl) balEl.textContent = data.balance.toFixed(2) + " PLN";
    notify(`Przelew ${amount.toFixed(2)} PLN do ${to} wykonany`);

    // Optymistycznie dopisz lokalny event (serwer i tak wyśle oficjalne zdarzenie)
    const ev = {
      ts: new Date().toISOString(),
      type: "transfer",
      message: `${me} przelał ${amount.toFixed(2)} PLN do ${to}`,
      from: me,
      to: to,
      amount: amount
    };
    prependEventToDOM(ev);
    fetchUsers();
  }catch(e){
    notify("Błąd sieci podczas przelewu");
  }
}

// ----- Historia: fetch + render -----
function formatTs(iso){
  try{
    const d = new Date(iso);
    // lokalne czytelne: YYYY-MM-DD HH:MM
    const y = d.getFullYear();
    const m = String(d.getMonth()+1).padStart(2,"0");
    const day = String(d.getDate()).padStart(2,"0");
    const hh = String(d.getHours()).padStart(2,"0");
    const mm = String(d.getMinutes()).padStart(2,"0");
    return `${y}-${m}-${day} ${hh}:${mm}`;
  }catch(e){
    return iso;
  }
}

function renderEvent(ev){
  const li = document.createElement("li");
  li.className = "event";
  // message, ts and optional details
  const ts = ev.ts ? formatTs(ev.ts) : "";
  const fromTo = (ev.from && ev.to) ? `<div class="small">${ev.from} → ${ev.to} • ${ev.amount ? ev.amount.toFixed(2) + " PLN" : ""}</div>` : "";
  li.innerHTML = `<div class="tile-head">
      <div style="flex:1">
        <div class="kpi">${ev.type === "transfer" ? (ev.amount ? (ev.amount.toFixed(2)+" PLN") : "") : ""}</div>
        <div style="font-weight:700">${ev.message}</div>
        ${fromTo}
      </div>
      <div class="text-muted" style="margin-left:12px">${ts}</div>
    </div>`;
  return li;
}

async function fetchHistory(limit = 50){
  try{
    const res = await fetch(`${API}/history?limit=${limit}`);
    if(!res.ok) return;
    const arr = await res.json();
    const container = $("events");
    if(!container) return;
    container.innerHTML = "";
    // arr already newest-first (server inserts newest at 0)
    for(const ev of arr){
      const el = renderEvent(ev);
      container.appendChild(el);
    }
  }catch(e){
    console.error(e);
  }
}

function prependEventToDOM(ev){
  const container = $("events");
  if(!container) return;
  const el = renderEvent(ev);
  container.prepend(el);
}

// ----- WebSocket -----
function connectWS(){
  if(ws) ws.close();
  ws = new WebSocket((location.protocol === "https:" ? "wss:" : "ws:") + "//" + location.host + "/ws/notifications");
  ws.addEventListener("open", ()=> {
    notify("Połączono z powiadomieniami");
  });
  ws.addEventListener("message", (ev)=> {
    try{
      const json = JSON.parse(ev.data);
      if(json.type === "notification"){
        // server broadcast contains message, from, to, amount, ts
        const e = {
          ts: json.ts || new Date().toISOString(),
          type: "transfer",
          message: json.message,
          from: json.from,
          to: json.to,
          amount: json.amount ? Number(json.amount) : null
        };
        prependEventToDOM(e);
        notify(json.message);
        // odśwież balans / listę użytkowników (bez await)
        fetchUsers();
        refreshBalance();
      }
      if(json.type === "pong"){ /* ignore */ }
    }catch(e){
      // ignore
    }
  });
  ws.addEventListener("close", ()=> notify("Rozłączono z powiadomieniami"));
  ws.addEventListener("error", ()=> notify("Błąd połączenia WS"));
}

// logout
function logout(){
  sessionStorage.removeItem("me");
  sessionStorage.removeItem("balance");
  if(ws) ws.close();
  window.location.href = "/static/index.html";
}

// events binding (guard existence)
if($("btnRefresh")) $("btnRefresh").addEventListener("click", refreshBalance);
if($("btnTransfer")) $("btnTransfer").addEventListener("click", doTransfer);
if($("btnLogout")) $("btnLogout").addEventListener("click", logout);
