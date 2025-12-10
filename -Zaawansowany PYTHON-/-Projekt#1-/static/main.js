const $ = id => document.getElementById(id);
let currentUser = null;
let es = null;

async function post(path, body){
  const r = await fetch(path, {
    method: 'POST',
    headers: {'Content-Type':'application/json'},
    body: JSON.stringify(body)
  });
  return await r.json();
}

// Auth actions
$('btnRegister').onclick = async () => {
  const u = $('username').value.trim(), p = $('password').value;
  const res = await post('/api/register', {username:u, password:p});
  $('authMsg').innerText = res.ok ? "Zarejestrowano. Zaloguj." : ("Błąd: "+res.msg);
};

$('btnLogin').onclick = async () => {
  const u = $('username').value.trim(), p = $('password').value;
  const res = await post('/api/login', {username:u, password:p});
  if(res.ok){ enter(res.user); } else { $('authMsg').innerText = "Błąd: "+res.msg; }
};

$('btnLogout').onclick = () => {
  currentUser = null;
  $('dash').hidden = true;
  $('authPanel').hidden = false;
  if(es) { es.close(); es = null; }
};

$('btnTransfer').onclick = async () => {
  const to = parseInt($('to_account').value);
  const amount = parseFloat($('amount').value);
  if(!currentUser) return alert("Zaloguj się");
  if(!to || !amount) return alert("Wypełnij pola");
  const res = await post('/api/transfer', {from_user: currentUser, to_account_id: to, amount: amount});
  if(res.ok){
    addEventToTop(res.event);
    await loadAccounts();
    pulseSuccess();
  } else {
    alert("Błąd: "+res.msg);
  }
};

function enter(user){
  currentUser = user;
  $('who').innerText = user;
  $('authPanel').hidden = true;
  $('dash').hidden = false;
  $('authMsg').innerText = "";
  loadAccounts();
  loadPastEvents();
  startSSE();
}

async function loadAccounts(){
  const res = await post('/api/balance', {username: currentUser});
  const el = $('accounts'); el.innerHTML = "";
  if(res.ok){
    res.accounts.forEach(acc => {
      const d = document.createElement('div');
      d.className = 'acc';
      d.innerHTML = `<div class="acc-id">Konto ${acc.id}</div><div class="acc-balance">${acc.balance.toFixed(2)} zł</div>`;
      el.appendChild(d);
    });
  } else {
    el.innerText = "Błąd: "+res.msg;
  }
}

async function loadPastEvents(){
  const r = await fetch('/api/events'); const res = await r.json();
  if(res.ok){
    const list = res.events.slice(0,200).reverse();
    list.forEach(addEventToTop);
  }
}

function addEventToTop(ev){
  const ul = $('events');
  const li = document.createElement('li');
  const t = new Date((ev.ts || Date.now()/1000) * 1000);
  if(ev.type === 'transfer'){
    li.innerHTML = `<div class="ev-line"><strong>Przelew</strong> ${ev.amount.toFixed(2)} zł</div><div class="ev-sub">od ${ev.from} → konto ${ev.to_account} • ${t.toLocaleString()}</div>`;
  } else if(ev.type === 'register'){
    li.innerHTML = `<div class="ev-line"><strong>Nowy użytkownik</strong> ${ev.user}</div><div class="ev-sub">${t.toLocaleString()}</div>`;
  } else {
    li.innerText = `${t.toLocaleString()} — ${JSON.stringify(ev)}`;
  }
  ul.prepend(li);
  // animate
  li.classList.add('pop');
  setTimeout(()=> li.classList.remove('pop'), 800);
  while(ul.children.length > 200) ul.removeChild(ul.lastChild);
}

function startSSE(){
  if(es) es.close();
  es = new EventSource('/events');
  es.onmessage = e => {
    try {
      const ev = JSON.parse(e.data);
      addEventToTop(ev);
      loadAccounts();
    } catch(err){}
  };
  es.onerror = () => { /* silent, browser auto reconnects */ };
}

function pulseSuccess(){
  document.body.animate([{boxShadow: '0 0 0 0 rgba(79,70,229,0.0)'},{boxShadow: '0 8px 40px 6px rgba(79,70,229,0.06)'}], {duration: 600});
}
