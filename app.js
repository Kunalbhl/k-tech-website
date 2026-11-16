// Interactive layer: particle network, cursor glow, reveals, tilt, magnetic buttons, counters, typing.
(() => {
  const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
  // particle network that reacts to the mouse
  const c = document.getElementById('bg'); const x = c && c.getContext('2d');
  let W, H, pts = [], m = { x: -999, y: -999 };
  function size() { if (!c) return; W = c.width = innerWidth * devicePixelRatio; H = c.height = innerHeight * devicePixelRatio; const n = Math.min(110, Math.floor(innerWidth / 14)); pts = Array.from({ length: n }, () => ({ x: Math.random() * W, y: Math.random() * H, vx: (Math.random() - .5) * .35 * devicePixelRatio, vy: (Math.random() - .5) * .35 * devicePixelRatio })); }
  function draw() {
    if (!x) return; x.clearRect(0, 0, W, H); const L = 140 * devicePixelRatio;
    for (const p of pts) { p.x += p.vx; p.y += p.vy; if (p.x < 0 || p.x > W) p.vx *= -1; if (p.y < 0 || p.y > H) p.vy *= -1;
      const dx = p.x - m.x, dy = p.y - m.y, d = Math.hypot(dx, dy); if (d < 160 * devicePixelRatio) { p.x += dx / d * 1.2; p.y += dy / d * 1.2; }
      x.fillStyle = 'rgba(180,190,255,.55)'; x.beginPath(); x.arc(p.x, p.y, 1.4 * devicePixelRatio, 0, 7); x.fill(); }
    for (let i = 0; i < pts.length; i++) for (let j = i + 1; j < pts.length; j++) { const a = pts[i], b = pts[j], d = Math.hypot(a.x - b.x, a.y - b.y);
      if (d < L) { x.strokeStyle = `rgba(124,92,255,${(1 - d / L) * .35})`; x.lineWidth = devicePixelRatio * .8; x.beginPath(); x.moveTo(a.x, a.y); x.lineTo(b.x, b.y); x.stroke(); } }
    requestAnimationFrame(draw);
  }
  if (c && !reduce) { size(); draw(); addEventListener('resize', size); }
  const glow = document.querySelector('.glow');
  addEventListener('pointermove', (e) => { m.x = e.clientX * devicePixelRatio; m.y = e.clientY * devicePixelRatio; if (glow) { glow.style.left = e.clientX + 'px'; glow.style.top = e.clientY + 'px'; } });
  // reveal on scroll
  const io = new IntersectionObserver((es) => es.forEach((e) => { if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); } }), { threshold: .12 });
  document.querySelectorAll('.reveal').forEach((el) => io.observe(el));
  // spotlight + 3D tilt cards
  document.querySelectorAll('.card').forEach((el) => {
    el.addEventListener('pointermove', (e) => { const r = el.getBoundingClientRect(), px = e.clientX - r.left, py = e.clientY - r.top;
      el.style.setProperty('--mx', px + 'px'); el.style.setProperty('--my', py + 'px');
      if (!reduce) el.style.transform = `perspective(900px) rotateX(${(py / r.height - .5) * -6}deg) rotateY(${(px / r.width - .5) * 6}deg)`; });
    el.addEventListener('pointerleave', () => { el.style.transform = ''; });
  });
  // magnetic buttons
  document.querySelectorAll('.btn').forEach((b) => { b.addEventListener('pointermove', (e) => { const r = b.getBoundingClientRect(); b.style.transform = `translate(${(e.clientX - r.left - r.width / 2) * .18}px,${(e.clientY - r.top - r.height / 2) * .25}px)`; }); b.addEventListener('pointerleave', () => { b.style.transform = ''; }); });
  // counters
  const co = new IntersectionObserver((es) => es.forEach((e) => { if (!e.isIntersecting) return; const el = e.target, to = +el.dataset.to, suf = el.dataset.suf || ''; let t0;
    const step = (t) => { t0 ??= t; const k = Math.min(1, (t - t0) / 1400); el.textContent = Math.round(to * (1 - Math.pow(1 - k, 3))) + suf; if (k < 1) requestAnimationFrame(step); }; requestAnimationFrame(step); co.unobserve(el); }));
  document.querySelectorAll('[data-to]').forEach((el) => co.observe(el));
  // typing words
  const t = document.querySelector('.typed');
  if (t) { const words = JSON.parse(t.dataset.words); let w = 0, i = 0, del = false;
    const tick = () => { const s = words[w]; t.textContent = s.slice(0, i); if (!del && i < s.length) i++; else if (del && i > 0) i--; else if (!del) { del = true; return setTimeout(tick, 1400); } else { del = false; w = (w + 1) % words.length; }
      setTimeout(tick, del ? 45 : 85); }; tick(); }
  // contact form → email
  const f = document.querySelector('form.contact');
  if (f) f.addEventListener('submit', (e) => { e.preventDefault(); const d = new FormData(f);
    const body = `Name: ${d.get('name')}\nEmail: ${d.get('email')}\nService: ${d.get('service')}\nBudget: ${d.get('budget')}\n\n${d.get('msg')}`;
    location.href = `mailto:support@chaloone.com?subject=${encodeURIComponent('Project enquiry: ' + d.get('service'))}&body=${encodeURIComponent(body)}`; });
  const y = document.getElementById('y'); if (y) y.textContent = new Date().getFullYear();
  const mb = document.querySelector('.menu'); if (mb) mb.onclick = () => document.getElementById('links').classList.toggle('open');
})();
