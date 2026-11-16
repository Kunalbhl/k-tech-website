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
      if (!reduce) el.style.transform = `perspective(900px) rotateX(${(py / r.height - .5) * -10}deg) rotateY(${(px / r.width - .5) * 10}deg) translateY(-6px)`; });
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

  // header: cursor spotlight + scrolled state
  const nav = document.querySelector('.nav');
  if (nav) { nav.addEventListener('pointermove', (e) => { const r = nav.getBoundingClientRect(); nav.style.setProperty('--nx', (e.clientX - r.left) + 'px'); nav.style.setProperty('--ny', (e.clientY - r.top) + 'px'); });
    const sc = () => nav.classList.toggle('scrolled', scrollY > 30); sc(); addEventListener('scroll', sc, { passive: true }); }
  // live Panchang (local astronomical calc, same approach as the Sanatan Sadhak app)
  const pc = document.getElementById('panchang');
  if (pc) { const d2r = Math.PI / 180, n360 = (x) => ((x % 360) + 360) % 360, sn = (x) => Math.sin(x * d2r);
    const now = new Date(), ist = new Date(now.getTime() + (330 + now.getTimezoneOffset()) * 60000);
    const rise = Date.UTC(ist.getFullYear(), ist.getMonth(), ist.getDate(), 1, 0); // ~06:30 IST sunrise
    const T = (rise / 864e5 + 2440587.5 - 2451545) / 36525;
    const M = 357.5291092 + 35999.0502909 * T, Lp = 218.3164477 + 481267.88123421 * T, D = 297.8501921 + 445267.1114034 * T, Mp = 134.9633964 + 477198.8675055 * T, F = 93.272095 + 483202.0175233 * T;
    const sun = n360(280.46646 + 36000.76983 * T + (1.914602 - .004817 * T) * sn(M) + .019993 * sn(2 * M) + .000289 * sn(3 * M) - .00569);
    const moon = n360(Lp + 6.288774 * sn(Mp) + 1.274027 * sn(2 * D - Mp) + .658314 * sn(2 * D) + .213618 * sn(2 * Mp) - .185116 * sn(M) - .114332 * sn(2 * F) + .058793 * sn(2 * D - 2 * Mp) + .057066 * sn(2 * D - M - Mp) + .053322 * sn(2 * D + Mp) + .045758 * sn(2 * D - M) - .040923 * sn(M - Mp) - .03472 * sn(D) - .030383 * sn(M + Mp));
    const ti = Math.floor(n360(moon - sun) / 12), shukla = ti < 15, k = ti % 15;
    const TN = ['Pratipada','Dwitiya','Tritiya','Chaturthi','Panchami','Shashthi','Saptami','Ashtami','Navami','Dashami','Ekadashi','Dwadashi','Trayodashi','Chaturdashi', shukla ? 'Purnima' : 'Amavasya'];
    const NK = ['Ashwini','Bharani','Krittika','Rohini','Mrigashira','Ardra','Punarvasu','Pushya','Ashlesha','Magha','Purva Phalguni','Uttara Phalguni','Hasta','Chitra','Swati','Vishakha','Anuradha','Jyeshtha','Mula','Purva Ashadha','Uttara Ashadha','Shravana','Dhanishta','Shatabhisha','Purva Bhadrapada','Uttara Bhadrapada','Revati'];
    const ayan = 23.853 + (T * 100) * .01397, nak = NK[Math.floor(n360(moon - ayan) / (360 / 27))];
    const VA = ['Ravivar','Somvar','Mangalvar','Budhvar','Guruvar','Shukravar','Shanivar'];
    const tithi = TN[k], tips = { Ekadashi: 'Ekadashi vrat is kept from sunrise to the next morning; chant Vishnu’s names.', Chaturthi: 'Chaturthi is dear to Shri Ganesha; offer durva and modak.', Trayodashi: 'Pradosh kaal this evening is ideal for Shiva puja.', Ashtami: 'Ashtami is auspicious for Devi upasana.', Purnima: 'Purnima: Satyanarayan katha and charity bring blessings.', Amavasya: 'Amavasya: remember your ancestors with tarpan and daan.', Navami: 'Navami is sacred to Shri Ram and Devi.' };
    const set = (k2, v) => { const el = pc.parentNode.querySelector(`[data-p="${k2}"]`); if (el) el.textContent = v; };
    set('vaar', VA[ist.getDay()]); set('paksha', (shukla ? 'Shukla' : 'Krishna') + ' Paksha'); set('tithi', tithi); set('nak', nak + ' Nakshatra');
    set('mitra', tips[tithi] || `${tithi} in ${shukla ? 'Shukla' : 'Krishna'} Paksha, a good day to keep your daily japa and sankalpa.`); }
  // product mock: type each line in turn, then repeat
  document.querySelectorAll('.mock').forEach((mk) => { const bubs = [...mk.querySelectorAll('.bub')]; if (!bubs.length || reduce) return;
    const nodes = bubs.map((b) => { const w = document.createTreeWalker(b, NodeFilter.SHOW_TEXT), a = []; let n; while ((n = w.nextNode())) a.push([n, n.textContent]); return a; });
    const run = () => { nodes.forEach((a) => a.forEach(([n]) => (n.textContent = ''))); let bi = 0, ni = 0, ci = 0;
      const step = () => { if (bi >= bubs.length) { bubs.forEach((b) => b.classList.remove('typing')); return setTimeout(run, 6000); }
        const a = nodes[bi]; bubs.forEach((b, j) => b.classList.toggle('typing', j === bi));
        if (ni >= a.length) { bi++; ni = 0; ci = 0; return setTimeout(step, 450); }
        const [n, full] = a[ni]; n.textContent = full.slice(0, ++ci); if (ci >= full.length) { ni++; ci = 0; } setTimeout(step, 28); };
      step(); };
    const ob = new IntersectionObserver((es) => { if (es[0].isIntersecting) { ob.disconnect(); setTimeout(run, 600); } }); ob.observe(mk); });
  // attachment picker: show chosen file, enforce 5 MB
  const att = document.getElementById('att');
  if (att) att.addEventListener('change', () => { const f = att.files[0], t = att.closest('.drop').querySelector('b');
    if (f && f.size > 5 * 1024 * 1024) { att.value = ''; t.textContent = 'File is over 5 MB, please share a link instead'; return; }
    t.textContent = f ? '✓ ' + f.name : 'Attach a file'; att.closest('.drop').classList.toggle('has', !!f); });
  const cf = document.querySelector('form.contact'); if (cf) cf.addEventListener('submit', () => { const b = cf.querySelector('button'); b.textContent = 'Sending…'; b.disabled = true; });
  const y = document.getElementById('y'); if (y) y.textContent = new Date().getFullYear();
  const mb = document.querySelector('.menu'); if (mb) mb.onclick = () => document.getElementById('links').classList.toggle('open');
})();
