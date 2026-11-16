import os, shutil
shutil.rmtree('dist',ignore_errors=True)
import hashlib as _h
ASSETV=_h.md5(open('styles.css','rb').read()+open('app.js','rb').read()).hexdigest()[:8]
SC='https://socialcord.chaloone.com/'
CM='https://community-manager.chaloone.com/'
APP='https://app.chaloone.com/'
NAV='''<div class="aurora"></div><canvas id="bg"></canvas><div class="glow"></div>
<header class="nav"><a class="logo" href="/"><img class="mark" src="/img/logo.svg" alt="K. Tech Services logo" width="36" height="36"><span>K. Tech <b class="grad">Services</b></span></a>
<nav class="links" id="links"><a href="/#services">Services</a><a href="/#work">Products</a><a href="/#process">Process</a><a href="/about.html">About</a><a href="/#contact">Contact</a></nav>
<a class="btn primary sm" href="/#contact">Start a project</a><button class="menu" aria-label="Menu">☰</button></header>'''
FOOT='''<footer><div class="wrap"><div class="cols">
<div><a class="logo" href="/"><img class="mark" src="/img/logo.svg" alt="K. Tech Services logo" width="36" height="36"><span>K. Tech <b class="grad">Services</b></span></a><p style="margin-top:16px;max-width:340px;line-height:1.6">Websites, web apps and mobile apps, designed and built by hand, from idea to launch and beyond. Based in Rajasthan, India · working worldwide.</p></div>
<div><h4>Services</h4><ul><li><a href="/#services">Website development</a></li><li><a href="/#services">Web app development</a></li><li><a href="/#services">Mobile app development</a></li><li><a href="/#services">UI / UX design</a></li><li><a href="/#services">AI agents</a></li><li><a href="/#services">Chatbots</a></li><li><a href="/#services">Discord bots</a></li><li><a href="/#services">Automation</a></li><li><a href="/#services">And many more tech services</a></li></ul></div>
<div><h4>Products</h4><ul><li><a href="/products/chalo-one.html">Chalo One</a></li><li><a href="/products/sanatan-sadhak.html">Sanatan Sadhak</a></li><li><a href="/products/socialcord-notifier.html">SocialCord Notifier</a></li><li><a href="/products/community-manager.html">Community Manager</a></li></ul></div>
<div><h4>Company</h4><ul><li><a href="/about.html">About</a></li><li><a href="/#contact">Contact</a></li><li><a href="mailto:support@chaloone.com">support@chaloone.com</a></li><li><a href="/privacy.html">Privacy</a> · <a href="/terms.html">Terms</a></li></ul></div>
</div><div class="legal"><span>© <span id="y"></span> K. Tech Services. All rights reserved. · Udyam-registered MSME, India</span><span>Owned &amp; built by Kunal Pareek</span></div></div></footer>'''
def page(title, desc, body):
    return f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title><meta name="description" content="{desc}"><meta property="og:title" content="{title}"><meta property="og:description" content="{desc}"><meta name="theme-color" content="#05060f">
<link rel="preconnect" href="https://fonts.googleapis.com"><link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="icon" type="image/png" sizes="32x32" href="/img/fav-32.png"><link rel="icon" type="image/png" sizes="16x16" href="/img/fav-16.png"><link rel="icon" type="image/svg+xml" href="/favicon.svg?v=4"><link rel="apple-touch-icon" href="/img/logo-512.png"><meta property="og:image" content="https://k-tech.chaloone.com/img/logo-512.png"><link rel="stylesheet" href="/styles.css?v={ASSETV}">
<script type="application/ld+json">{{"@context":"https://schema.org","@type":"Organization","name":"K. Tech Services","url":"https://k-tech.chaloone.com","email":"support@chaloone.com","address":{{"@type":"PostalAddress","addressRegion":"Rajasthan","addressCountry":"IN"}}}}</script>
</head><body>{NAV}<main>{body}</main>{FOOT}<script src="/app.js?v={ASSETV}" defer></script></body></html>'''
P={}
SERVICES=[('🌐','Website development','Fast, beautiful, SEO-ready websites for businesses, brands and portfolios, with smooth animations and an easy way to update content.'),
('⚙️','Web app development','Dashboards, portals, booking systems and SaaS products, with logins, payments, admin panels and real-time data.'),
('📱','Mobile app development','Android apps (and cross-platform when you need iOS) with modern design, offline support, notifications and cloud sync.'),
('🎨','UI / UX design','Clean interfaces and complete design systems, prototyped and tested before a single line of code.'),
('🛒','E-commerce & booking','Online stores, ordering and booking flows, wallets, coupons and payment gateways.'),
('🔌','APIs & backend','Secure APIs, databases and integrations with the tools you already use.'),
('🧠','AI agents','Smart agents that research, answer, decide and take actions inside your tools, built safely around your data.'),
('💬','Chatbots & assistants','Website, Discord and in-app chatbots that answer customers 24/7 and hand over to your team when needed.'),
('🤖','Discord bots','Custom Discord bots for communities: onboarding, roles, applications, alerts, rewards and moderation.'),
('⚡','Automation & workflows','Connect your apps and remove repeated manual work: reports, reminders, sync and notifications.'),
('☁️','Hosting, care & growth','Deployment, domains, speed, security updates, analytics and SEO, so your product keeps getting better.'),
('✨','And many more','Have a different tech idea? If it can be built, I can help you plan it, build it and run it. Just ask.')]
from services_data import S as SD, PRICE, PRICE_INFO
svc=''.join((f'<a class="card reveal d{i%3}" href="/services/{SD[b]["slug"]}">' if b in SD else f'<div class="card reveal d{i%3}">')+f'<span class="num">{i+1:02d}</span><div class="ic">{a}</div><h3>{b}</h3><p>{c}</p>'+(f'<div class="price">From <b>{PRICE[b]}</b></div>' if b in PRICE else '')+('<div class="go">Learn more <b>→</b></div></a>' if b in SD else '</div>') for i,(a,b,c) in enumerate(SERVICES))
PRODS=[('chalo-one','Chalo One','🧭','Super-app · Web','live','Food, groceries, rides and stays in one app, with a wallet, rewards and a smart assistant that compares options for you.'),
('sanatan-sadhak','Sanatan Sadhak','🪔','Mobile app · Android','soon','A calm companion for daily sadhana: mantra counter, sankalpa, Panchang, temples, Vedic library and a gentle guide.'),
('socialcord-notifier','SocialCord Notifier','🔔','Discord bot','live','Instant Discord alerts when your Instagram or Facebook posts a reel, post or video, with the right roles pinged.'),
('community-manager','Community Manager','🛡️','Discord bot','live','Applications, interviews, recruiter codes and rewards, secure onboarding, events and growth reports for Discord communities.')]
prods=''.join(f'<a class="card prod reveal d{i%2} {"big" if i in (0,3) else ""}" href="/products/{s}.html"><img class="plogo" src="/img/{s}.png" alt="{n} logo" loading="lazy"><div class="tag">{t}</div><h3>{n}</h3><p>{d}</p><div class="row" style="margin-top:16px"><span class="badge {"" if st=="live" else "soon"}">{"● Live" if st=="live" else "Early access"}</span></div><div class="go">View project <b>→</b></div></a>' for i,(s,n,ic,t,st,d) in enumerate(PRODS))
TECH=['React','TypeScript','Node.js','Next / Vite','Tailwind CSS','Kotlin','Jetpack Compose','Android','Firebase','Google Cloud','PostgreSQL','Supabase','Cloudflare','Discord API','REST APIs','Gemini AI','Docker','Git & CI']
marq=''.join(f'<span>{w}</span>' for w in (['Websites','Web apps','Mobile apps','UI/UX','E-commerce','Dashboards','APIs','AI agents','Chatbots','Discord bots','Automation','Booking systems','SaaS']*2))
P['index.html']=page('K. Tech Services by Kunal · Website, App, AI & Discord Bot Development (Rajasthan, India)','K. Tech Services is an Indian software studio by Kunal building websites, web apps, mobile apps, AI agents, chatbots and Discord bots. Makers of Chalo One, Sanatan Sadhak, SocialCord Notifier and Community Manager.',f'''
<section class="hero"><div class="orbit"><div><span>📱</span></div><div><span>⚡</span></div><div><span>🌐</span></div></div>
<div class="wrap"><div class="chip reveal"><b></b> Taking on new projects</div>
<h1 class="reveal d1">I build digital<br>products that <span class="grad">feel alive.</span></h1>
<p class="lead reveal d2">Hi, I’m Kunal, founder of K. Tech Services. I design and develop <span class="typed" data-words='["websites","web apps","mobile apps","online stores","dashboards","AI agents","chatbots","Discord bots"]'></span> for businesses that want to stand out, and I run four products of my own.</p>
<div class="row reveal d3"><a class="btn primary" href="#contact">Start your project →</a><a class="btn ghost" href="#work">See my work</a></div></div>
<div class="scroll"><i></i>Scroll</div></section>
<div class="marquee"><div>{marq}</div></div>
<section id="services"><div class="wrap"><div class="kicker reveal">What I do</div><h2 class="title reveal d1">From the first sketch to a product people use every day.</h2><p class="sub reveal d2">One person accountable for design, code and launch, so nothing gets lost between teams.</p><div class="grid g4">{svc}</div><p class="pnote reveal">Prices shown are <b>starting from</b> prices for a small, simple version. They are not final: every project is quoted on its own requirements, scope and potential. You get a free written quote before any work starts.</p></div></section>
<section id="work"><div class="wrap"><div class="kicker reveal">Built &amp; running</div><h2 class="title reveal d1">My own products, live with real users.</h2><p class="sub reveal d2">The best proof I can build yours: I design, build and run these myself, end to end.</p><div class="grid g3">{prods}</div></div></section>
<section><div class="wrap"><div class="stats">
<div class="stat reveal"><b data-to="4">0</b><span>Products shipped</span></div><div class="stat reveal d1"><b data-to="3" data-suf="">0</b><span>Platforms: web, Android, Discord</span></div>
<div class="stat reveal d2"><b data-to="100" data-suf="%">0</b><span>Hand-built, no templates</span></div><div class="stat reveal d3"><b data-to="24" data-suf="h">0</b><span>Reply time to new enquiries</span></div></div></div></section>
<section id="process"><div class="wrap"><div class="kicker reveal">How we work together</div><h2 class="title reveal d1">A simple process, no surprises.</h2>
<div class="steps"><div class="step reveal"><h3>Discover</h3><p>We talk about your goals, users and budget. You get a clear plan and quote.</p></div>
<div class="step reveal d1"><h3>Design</h3><p>Screens and a clickable prototype, refined with you until it feels right.</p></div>
<div class="step reveal d2"><h3>Build</h3><p>Weekly progress you can see and click. Fast, secure and tested.</p></div>
<div class="step reveal d3"><h3>Launch &amp; grow</h3><p>Go live on your domain, then hosting, updates and improvements.</p></div></div></div></section>
<section><div class="wrap"><div class="kicker reveal">Tools I use</div><h2 class="title reveal d1">Modern stack. Built to last.</h2><div class="tech reveal d2">{''.join(f'<span>{t}</span>' for t in TECH)}</div></div></section>
<section id="contact"><div class="wrap"><div class="cta reveal"><div class="kicker">Let’s build</div><h2>Have an idea? <span class="grad">Let’s make it real.</span></h2>
<p class="sub" style="margin:16px auto 0">Tell me what you need. I reply within one working day.</p>
<form class="contact" action="https://formsubmit.co/support@chaloone.com" method="POST" enctype="multipart/form-data" style="max-width:760px;margin-inline:auto"><input type="hidden" name="_subject" value="New project enquiry · k-tech.chaloone.com"><input type="hidden" name="_template" value="table"><input type="hidden" name="_captcha" value="false"><input type="hidden" name="_next" value="https://k-tech.chaloone.com/thanks"><input type="text" name="_honey" style="display:none" tabindex="-1" autocomplete="off"><div class="two"><input class="field" name="name" placeholder="Your name" required><input class="field" type="email" name="email"  placeholder="Your email" required></div>
<div class="two"><select class="field" name="service"><option>Website</option><option>Web app</option><option>Mobile app</option><option>E-commerce / booking</option><option>UI / UX design</option><option>Discord bot</option><option>Something else</option></select>
<select class="field" name="budget"><option>Budget: not sure yet</option><option>Under ₹25,000</option><option>₹25,000 – ₹1,00,000</option><option>₹1,00,000 – ₹5,00,000</option><option>₹5,00,000+</option></select></div>
<textarea class="field" name="msg" rows="5" placeholder="Tell me about your project" required></textarea><label class="drop"><input type="file" name="attachment" id="att"><span class="dic">📎</span><span class="dtx"><b>Attach a file</b> (optional)<small>Brief, document, PDF, sheet, images or a ZIP · up to 5 MB. Bigger files? Paste a Drive link in the message.</small></span></label><div><button class="btn primary">Send enquiry →</button></div></form></div></div></section>''')
def plogo(slug,name):
    if slug!='sanatan-sadhak': return f'<img class="plogo big" src="/img/{slug}.png" alt="{name} logo">'
    return ('<img class="plogo hero-ss" src="/img/sanatan-sadhak-logo-mid.webp" alt="Sanatan Sadhak logo" width="440" height="440">'
      '<span class="fire" aria-hidden="true"><i class="f1"></i><i class="f2"></i><i class="f3"></i><i class="f4"></i><b></b><b></b><b></b><b></b><b></b></span>'
      '<svg width="0" height="0" style="position:absolute" aria-hidden="true"><filter id="fireWarp"><feTurbulence type="fractalNoise" baseFrequency="0.035 0.09" numOctaves="2" seed="3" result="n">'
      '<animate attributeName="baseFrequency" dur="2.2s" values="0.035 0.09;0.05 0.13;0.035 0.09" repeatCount="indefinite"/></feTurbulence><feDisplacementMap in="SourceGraphic" in2="n" scale="7"/></filter></svg>')
def prod(slug,name,ic,tag,status,lead,feats,how,cta,url,mock):
    f=''.join(f'<div class="card reveal d{i%3}"><div class="ic">{a}</div><h3>{b}</h3><p>{c}</p></div>' for i,(a,b,c) in enumerate(feats))
    h=''.join(f'<li><b>{i+1}</b>{x}</li>' for i,x in enumerate(how))
    btn=f'<a class="btn primary" href="{url}" target="_blank" rel="noopener">{cta} →</a>' if url else f'<a class="btn primary" href="/#contact">{cta} →</a>'
    P[f'products/{slug}.html']=page(f'{name} · K. Tech Services',lead[:155],f'''
<section class="phero"><div class="wrap split"><div><div class="brandrow reveal"><span class="plogo-wrap {slug}">{plogo(slug,name)}</span><div class="chip"><b></b>{tag} · {"Live" if status=="live" else "Early access"}</div></div><h1 class="reveal d1"><span class="grad">{name}</span></h1><p class="lead reveal d2">{lead}</p>
<div class="row reveal d3">{btn}<a class="btn ghost" href="/#contact">Want something like this?</a></div></div><div class="mock reveal d2">{mock}</div></div></section>
{(f'<section><div class="wrap"><div class="kicker reveal">Live product</div><h2 class="title reveal d1">See it in action</h2><div class="gal reveal d2{' phones' if slug=='sanatan-sadhak' else ''}" data-auto="4500"><div class="bar"><i></i><i></i><i></i><em>{(url or "//Android app · live preview").split("//")[1].rstrip("/")}</em>'+(f'<a href="{url}" target="_blank" rel="noopener">Open live ↗</a>' if url else '')+'</div><div class="track">'+''.join(f'<img src="/img/shots/{slug}/{n}?v={__import__("hashlib").md5(open(f"img/shots/{slug}/{n}","rb").read()).hexdigest()[:8]}" alt="{name} screenshot {k+1}" loading="lazy" '+('width="638" height="1368"' if slug=='sanatan-sadhak' else 'width="1568" height="726"')+'>' for k,n in enumerate(sorted(os.listdir(f'img/shots/{slug}'))))+'</div><button class="gnav prev" aria-label="Previous screenshot">‹</button><button class="gnav next" aria-label="Next screenshot">›</button><div class="dots"></div></div></div></section>' if os.path.isdir(f'img/shots/{slug}') else '')}<section><div class="wrap"><div class="kicker reveal">Features</div><h2 class="title reveal d1">What it does</h2><div class="grid g3">{f}</div></div></section>
<section><div class="wrap split"><div><div class="kicker reveal">How it works</div><h2 class="title reveal d1">Simple from day one.</h2><ul class="list reveal d2">{h}</ul></div>
<div class="cta reveal" style="text-align:left;padding:44px"><h2 style="font-size:34px">Need a product like {name}?</h2><p class="sub">I designed and built it end to end. I can do the same for your idea.</p><div class="row" style="margin-top:24px"><a class="btn primary" href="/#contact">Start a project →</a></div></div></div></section>''')
prod('chalo-one','Chalo One','🧭','Super-app','live','Compare, plan, book and order from one place: food, groceries, rides and stays, with a built-in wallet, rewards and a smart assistant that helps you choose.',
 [('🍽️','Food & groceries','Restaurants and daily essentials in one cart.'),('🚕','Rides & stays','Compare cabs and places to stay without switching apps.'),('💬','Smart assistant','Ask in plain words and get suggestions and comparisons.'),('👛','Chalo Wallet','Faster payments and one history for everything.'),('🎁','Referrals & rewards','Invite friends and earn rewards.'),('🏪','Partner tools','Menus, inventory, orders and branches for partners.')],
 ['Sign in and set your address.','Search, or ask the assistant what you need.','Compare options and add them to one cart.','Pay with the wallet and track it all.'],'Open Chalo One',APP,
 '<div class="bub"><b>You:</b> Dinner for 4 tonight and a cab at 8?</div><div class="bub"><b>Chalo:</b> 3 family combos near you and a 6-seater at 7:55 PM. Add both?</div><div class="bub">🛒 1 cart · 👛 Wallet · 🎁 Rewards</div>')
prod('sanatan-sadhak','Sanatan Sadhak','🪔','Android app','soon','A calm, beautiful app for mantra chanting, daily sadhana, Panchang, temples and Vedic knowledge, with a gentle guide that answers your questions.',
 [('📿','Mantra & jaap counter','A digital mala with counts and history.'),('🎯','Sankalpa & sadhana','Set a sankalpa and follow your daily routine.'),('📅','Panchang & festivals','Tithi, nakshatra and festival calendar.'),('🛕','Temple finder','Find temples near you.'),('📚','Vedic library','Shlokas, aartis, stories, audio and video.'),('🙏','Mitra guide','Ask about rituals and meanings; get clear answers.')],
 ['Install and choose your deities and language.','Pick mantras and set a daily sankalpa.','Chant, listen to aartis and check the Panchang.','Ask the guide and join the community.'],'Visit the app website','https://sanatan-sadhak.chaloone.com/',
 '<div class="bub" id="panchang"><b>🌅 Today</b> · <span data-p="vaar">…</span> · <span data-p="paksha">…</span> · <span data-p="tithi">…</span> · <span data-p="nak">…</span></div><div class="bub">📿 Om Namah Shivaya · <b>108 / 108</b> ✓</div><div class="bub"><b>Mitra:</b> <span data-p="mitra">Today’s tithi guides your sadhana and vrat…</span></div>')
prod('socialcord-notifier','SocialCord Notifier','🔔','Discord bot','live','Instant alerts in your Discord server when your Instagram and Facebook accounts post a reel, post or video, with rich embeds and the right roles pinged.',
 [('⚡','Instant alerts','New posts appear in your channel within moments.'),('🎨','Rich embeds','Image, caption and link, styled for Discord.'),('📣','Role mentions','Ping only the roles you choose.'),('🗂️','Many feeds','Each account to its own channel.'),('🔒','Isolated per server','Every server keeps its own settings.'),('🖥️','Simple dashboard','Sign in with Discord and set up in minutes.')],
 ['Add the bot to your server.','Sign in to the dashboard with Discord.','Connect accounts and pick channels.','Choose roles to ping; alerts start right away.'],'Open SocialCord Notifier',SC,
 '<div class="bub">🔔 <b>New reel from @yourpage</b></div><div class="bub">“Behind the scenes of our new launch…”</div><div class="bub">@Followers you have a new post!</div>')
prod('community-manager','Community Manager','🛡️','Discord bot','live','Applications, interviews, recruiter codes and rewards, secure onboarding, events, engagement and moderation for Discord communities, run from Discord and a clear dashboard.',
 [('📝','Apply from Discord','Guided applications, rules quiz and private review rooms.'),('🎟️','Recruiter codes & rewards','Invite tracking, leaderboard, wallet rewards and approvals.'),('🔐','Secure onboarding','Newcomers see only what they should until approved.'),('📅','Events package','Registration, Discord Events, reminders, polls and giveaways.'),('📊','Growth reports','Live stats channels and weekly or monthly reports.'),('🎛️','Roles & engagement','Premium role panels, levels, tickets and welcomes.')],
 ['Add the bot and sign in with Discord.','Follow the setup guide.','Post the Apply panel; members apply in Discord.','Review, interview and approve; rewards and reports run on their own.'],'Open Community Manager',CM,
 '<div class="bub">📋 <b>Join our team</b> · Press Apply to start</div><div class="bub">✅ Approved · 🎟️ Code <b>KUN-007</b> created</div><div class="bub">📊 Weekly report · +12 joined · 92% still here</div>')
P['about.html']=page('About · K. Tech Services','About K. Tech Services and its founder.',f'''
<section class="phero"><div class="wrap me"><div class="avatar reveal"><div><img src="/img/logo.svg" alt="K. Tech Services logo" style="width:62%;height:62%"></div></div><div><div class="kicker reveal">About</div><h1 class="reveal d1">Hi, I’m <span class="grad">Kunal.</span></h1>
<p class="lead reveal d2">I started K. Tech Services to build software the way I like to use it: fast, clear and genuinely useful. I take products from idea to launch myself: design, front-end, back-end, mobile and hosting.</p>
<p class="sub reveal d3">Alongside client work I build and run my own products: Chalo One, Sanatan Sadhak, SocialCord Notifier and Community Manager. Running them every day keeps my skills sharp and my promises honest.</p>
<div class="row reveal d3" style="margin-top:28px"><a class="btn primary" href="/#contact">Work with me →</a><a class="btn ghost" href="/#work">See products</a></div>
</div></div></section>
<section><div class="wrap"><div class="facts reveal"><h2>Company at a glance</h2><dl>
<dt>Company</dt><dd>K. Tech Services</dd>
<dt>Owner &amp; founder</dt><dd>Kunal Pareek</dd>
<dt>What we do</dt><dd>Websites, web &amp; mobile apps, AI agents, chatbots and Discord bots</dd>
<dt>Our products</dt><dd>Chalo One · Sanatan Sadhak · SocialCord Notifier · Community Manager</dd>
<dt>Registration</dt><dd>Udyam-registered MSME, Rajasthan, India</dd>
<dt>Contact</dt><dd><a href="mailto:support@chaloone.com">support@chaloone.com</a></dd>
</dl><p class="rights">© K. Tech Services. All rights reserved. The K. Tech Services name and logo, and the names and logos of its products, belong to K. Tech Services. Other brand names belong to their owners. See our <a href="/privacy">Privacy policy</a> and <a href="/terms">Terms</a>.</p></div></div></section>''')
P['privacy.html']=page('Privacy policy · K. Tech Services','How K. Tech Services handles personal data.',f'''<section class="phero"><div class="wrap prose"><h1>Privacy policy</h1><p>Last updated: 15 November 2026</p>
<p>This policy explains how K. Tech Services collects and uses information on this website and in our products: Chalo One, Sanatan Sadhak, SocialCord Notifier and Community Manager.</p>
<h2>What we collect</h2><ul><li>Details you give us, such as name and email.</li><li>For Discord products: your Discord user ID, username and the server settings you configure. We do not read private messages.</li><li>Content you create in our products, such as orders, mantra counts, applications or settings.</li><li>Basic technical data used to keep services secure and working.</li></ul>
<h2>How we use it</h2><ul><li>To provide and improve our products.</li><li>To keep accounts and communities safe.</li><li>To reply to your messages.</li></ul><p>We do not sell personal data.</p>
<h2>Service providers</h2><p>We host on Google Cloud, Firebase and Cloudflare. They process data only to provide their service to us.</p>
<h2>Your choices</h2><p>Write to support@chaloone.com to access, correct or delete your data. Removing a Discord bot from your server stops all collection for that server.</p></div></section>''')
P['terms.html']=page('Terms of service · K. Tech Services','Terms for K. Tech Services products.',f'''<section class="phero"><div class="wrap prose"><h1>Terms of service</h1><p>Last updated: 15 November 2026</p>
<p>By using our website or products you agree to these terms.</p><h2>Using our products</h2><ul><li>Use them lawfully and follow the rules of connected platforms, such as Discord’s Terms of Service.</li><li>You are responsible for your account and content.</li><li>We may suspend use that harms others or our services.</li></ul>
<h2>Availability</h2><p>Services may change or be unavailable at times. Early-access features may change.</p><h2>Liability</h2><p>Products are provided “as is”. To the extent allowed by law, K. Tech Services is not liable for indirect losses.</p>
<h2>Governing law</h2><p>These terms are governed by the laws of India.</p><h2>Contact</h2><p>support@chaloone.com</p></div></section>''')
P['thanks.html']=page('Thank you · K. Tech Services','Your enquiry has been sent.','<section class="phero"><div class="wrap" style="text-align:center"><h1>Thank you<span class="grad">!</span></h1><p class="lead" style="margin-inline:auto">Your enquiry reached me. I reply within one working day at the email you gave.</p><div class="row" style="justify-content:center;margin-top:28px"><a class="btn primary" href="/">Back to home →</a></div></div></section>')
P['404.html']=page('Not found · K. Tech Services','Page not found.','<section class="phero"><div class="wrap" style="text-align:center"><h1><span class="grad">404</span></h1><p class="lead" style="margin-inline:auto">This page doesn’t exist.</p><div class="row" style="justify-content:center"><a class="btn primary" href="/">Go home</a></div></div></section>')
P['contact.html']='<!doctype html><meta http-equiv="refresh" content="0;url=/#contact"><link rel="canonical" href="/#contact">'
import json as _j
BASE='https://k-tech.chaloone.com'
ORG={"@type":"Organization","@id":BASE+"/#org","name":"K. Tech Services","alternateName":["K Tech Services","KTech Services","K-Tech Services Rajasthan"],"url":BASE+"/","logo":{"@type":"ImageObject","url":BASE+"/img/logo-512.png","width":512,"height":512},"image":BASE+"/img/logo-512.png","email":"support@chaloone.com","founder":{"@type":"Person","name":"Kunal","jobTitle":"Founder & Developer"},"address":{"@type":"PostalAddress","addressRegion":"Rajasthan","addressCountry":"IN"},"areaServed":"IN","description":"K. Tech Services is an Indian software studio by Kunal that builds websites, web apps, mobile apps, AI agents, chatbots and Discord bots, and runs its own products: Chalo One, Sanatan Sadhak, SocialCord Notifier and Community Manager.","knowsAbout":["Website development","Web app development","Mobile app development","UI/UX design","AI agents","Chatbots","Discord bots","Automation"],"hasOfferCatalog":{"@type":"OfferCatalog","name":"Services","itemListElement":[{"@type":"Offer","itemOffered":{"@type":"Service","name":n}} for n in ["Website development","Web app development","Mobile app development","UI/UX design","E-commerce and booking systems","APIs and backend","AI agents","Chatbots and assistants","Discord bot development","Automation and workflows","Hosting, care and growth"]]}}

for _t,_d in SD.items():
    _ic=next(a for a,b,c in SERVICES if b==_t)
    _g=''.join(f'<div class="card reveal d{i%3}"><div class="ic">{a}</div><h3>{b}</h3><p>{c}</p></div>' for i,(a,b,c) in enumerate(_d['gets']))
    _f=''.join(f'<details class="faq reveal"><summary>{q}</summary><p>{a}</p></details>' for q,a in _d['faq'])
    _o=''.join(f'<a class="chipl" href="/services/{v["slug"]}">{k}</a>' for k,v in SD.items() if k!=_t)
    P[f'services/{_d["slug"]}.html']=page(f'{_d["title"]} · K. Tech Services by Kunal Pareek',(_d['intro'][0])[:155],f'''
<section class="phero"><div class="wrap"><div class="chip reveal"><b></b>Service</div><h1 class="reveal d1"><span style="font-size:.8em">{_ic}</span> <span class="grad">{_d["title"]}</span></h1>{''.join(f'<p class="lead reveal d2">{p}</p>' for p in _d['intro'])}
<div class="pricetag reveal d3">Starting from <b class="grad">{PRICE.get(_t,'')}</b><span>A starting point, not a final price. Your quote depends on your requirements and project scope.</span></div><div class="row reveal d3"><a class="btn primary" href="/#contact">Get a free quote →</a><a class="btn ghost" href="/#work">See my products</a></div></div></section>
<section><div class="wrap"><div class="kicker reveal">What you get</div><h2 class="title reveal d1">Everything you need, done properly.</h2><div class="grid g4">{_g}</div></div></section>
<section><div class="wrap"><div class="pricebox reveal"><div class="kicker">Pricing</div><h2>Starting from <span class="grad">{PRICE.get(_t,"")}</span></h2><p><b>This is not a final price.</b> It is the starting point for a small, simple version. The final price depends on your requirements, the scope and potential of the project, and how it may grow.</p><p><b>What changes the price:</b> {PRICE_INFO[_t][0]}</p><p><b>Not included:</b> {PRICE_INFO[_t][1]}</p><p>You get a clear written quote, free and with no obligation, before any work starts.</p><a class="btn primary" href="/#contact">Get my free quote →</a></div></div></section>
<section><div class="wrap"><div class="kicker reveal">FAQ</div><h2 class="title reveal d1">Common questions</h2><div class="faqs">{_f}</div></div></section>
<section><div class="wrap"><div class="cta reveal"><h2>Ready to start? <span class="grad">Let’s talk.</span></h2><p class="sub" style="margin:16px auto 0">Tell me about your project and I’ll reply within one working day.</p><div class="row" style="justify-content:center;margin-top:24px"><a class="btn primary" href="/#contact">Start a project →</a></div>
<div class="chips" style="margin-top:34px">{_o}</div></div></div></section>''')
SITE={"@type":"WebSite","@id":BASE+"/#site","url":BASE+"/","name":"K. Tech Services","publisher":{"@id":BASE+"/#org"},"inLanguage":"en-IN"}
APPS={'chalo-one':('Chalo One','https://app.chaloone.com/','TravelApplication'),'sanatan-sadhak':('Sanatan Sadhak','https://sanatan-sadhak.chaloone.com/','LifestyleApplication'),'socialcord-notifier':('SocialCord Notifier','https://socialcord.chaloone.com/','SocialNetworkingApplication'),'community-manager':('Community Manager','https://community-manager.chaloone.com/','BusinessApplication')}
for k,v in P.items():
    if k.endswith('.html') and '<head>' in v and k!='contact.html':
        path='' if k=='index.html' else k[:-5]
        url=BASE+'/'+path
        graph=[ORG,SITE]
        slug=k.split('/')[-1][:-5]
        if k.startswith('products/') and slug in APPS:
            n,u,cat=APPS[slug]
            graph.append({"@type":"SoftwareApplication","name":n,"url":u,"applicationCategory":cat,"operatingSystem":"Android" if slug=='sanatan-sadhak' else "Web, Discord" if 'cord' in slug or 'community' in slug else "Web","image":BASE+'/img/'+slug+'.png',"author":{"@id":BASE+"/#org"},"publisher":{"@id":BASE+"/#org"},"offers":{"@type":"Offer","price":"0","priceCurrency":"INR"}})
        if k in('404.html','thanks.html'): extra='<meta name="robots" content="noindex">'
        else: extra=f'<link rel="canonical" href="{url}"><meta property="og:url" content="{url}">'
        extra+=('<meta property="og:type" content="website"><meta property="og:site_name" content="K. Tech Services"><meta property="og:locale" content="en_IN">'
                '<meta name="twitter:card" content="summary_large_image"><meta name="twitter:image" content="'+BASE+'/img/og.png"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="630">'
                '<link rel="icon" type="image/png" sizes="48x48" href="/img/favicon-48.png?v=4"><link rel="icon" type="image/png" sizes="192x192" href="/img/icon-192.png?v=4"><link rel="shortcut icon" href="/favicon.ico?v=4"><link rel="manifest" href="/site.webmanifest">'
                '<meta name="author" content="Kunal, K. Tech Services">')
        v=v.replace('<meta property="og:image" content="https://k-tech.chaloone.com/img/logo-512.png">','<meta property="og:image" content="'+BASE+'/img/og.png">')
        import re as _re
        v=_re.sub(r'<script type="application/ld\+json">.*?</script>','<script type="application/ld+json">'+_j.dumps({"@context":"https://schema.org","@graph":graph},ensure_ascii=False)+'</script>',v,count=1,flags=_re.S)
        v=v.replace('</head>',extra+'</head>',1)
    out=os.path.join('dist',k); os.makedirs(os.path.dirname(out),exist_ok=True); open(out,'w').write(v)
for f in ['_headers','app.js','styles.css','favicon.ico','favicon.svg','robots.txt','site.webmanifest']: shutil.copy(f,'dist/'+f)
for d in ['img','socialcord-notifier','community-manager']: shutil.copytree(d,'dist/'+d,dirs_exist_ok=True)
_urls=['']+[k[:-5] for k in sorted(P) if k not in('index.html','404.html','thanks.html','contact.html')]+['socialcord-notifier/privacy','socialcord-notifier/terms','community-manager/privacy','community-manager/terms']
_today=__import__('datetime').date.today().isoformat()
open('dist/sitemap.xml','w').write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'+''.join(f'<url><loc>{BASE}/{u}</loc><lastmod>{_today}</lastmod></url>\n' for u in _urls)+'</urlset>\n')
print(len(P),'pages ->',len(_urls),'sitemap urls')
