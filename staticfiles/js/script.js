// ---------- Contact form: actually sends the message to the backend ----------
const contactForm = document.getElementById('contactForm');
if (contactForm) {
  contactForm.addEventListener('submit', async function (e) {
    e.preventDefault();
    const statusEl = document.getElementById('formStatus');
    const submitBtn = contactForm.querySelector('.form-submit');
    const payload = {
      name: contactForm.name.value.trim(),
      email: contactForm.email.value.trim(),
      message: contactForm.message.value.trim(),
      website: contactForm.website.value, // honeypot — bots fill this, humans don't
    };

    submitBtn.disabled = true;
    statusEl.textContent = 'sending...';
    statusEl.className = 'form-status mono';

    try {
      const res = await fetch('/api/contact/', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(payload),
      });

      if (res.ok) {
        statusEl.textContent = 'message sent — thanks! I\u2019ll get back to you soon.';
        statusEl.classList.add('success');
        contactForm.reset();
      } else {
        const data = await res.json().catch(() => ({}));
        const firstError = Object.values(data)[0];
        statusEl.textContent = Array.isArray(firstError)
          ? firstError[0]
          : 'something went wrong — please try again.';
        statusEl.classList.add('error');
      }
    } catch (err) {
      statusEl.textContent = 'network error — please try again.';
      statusEl.classList.add('error');
    } finally {
      submitBtn.disabled = false;
    }
  });
}

// ---------- Load skills from the API (falls back to static HTML if it fails) ----------
async function loadSkills() {
  const grid = document.getElementById('skillGrid');
  if (!grid) return;
  try {
    const res = await fetch('/api/skills/');
    if (!res.ok) return;
    const skills = await res.json();
    if (!skills.length) return;
    grid.innerHTML = skills
      .map(
        (s) => `
      <div class="skill-card" style="--fill:${s.percent}%">
        <div class="lvl">${s.level}</div>
        <div class="name">${s.name}</div>
        <div class="bar"><div class="bar-fill"></div></div>
      </div>`
      )
      .join('');
  } catch (err) {
    // keep the static fallback markup already in the page
  }
}

// ---------- Load projects from the API (falls back to static HTML if it fails) ----------
async function loadProjects() {
  const grid = document.getElementById('projectGrid');
  if (!grid) return;
  try {
    const res = await fetch('/api/projects/');
    if (!res.ok) return;
    const projects = await res.json();
    if (!projects.length) return;
    grid.innerHTML = projects
      .map(
        (p) => `
      <div class="project">
        <div class="project-head">
          <span class="project-name">${p.name}</span>
          ${p.github_link ? `<a href="${p.github_link}" class="project-link" target="_blank" rel="noopener">github \u2192</a>` : ''}
        </div>
        <p class="project-desc">${p.description}</p>
        <div class="project-tags">${p.tags.map((t) => `<span>${t}</span>`).join('')}</div>
      </div>`
      )
      .join('');
  } catch (err) {
    // keep the static fallback markup already in the page
  }
}

loadSkills();
loadProjects();

// ---------- Clock / date ----------
function pad(n) {
  return String(n).padStart(2, '0');
}

function updateClocks() {
  const now = new Date();
  const hhmm = `${pad(now.getHours())}:${pad(now.getMinutes())}`;
  const hhmmss = `${hhmm}:${pad(now.getSeconds())}`;

  const sbTime = document.getElementById('sbTime');
  if (sbTime) sbTime.textContent = hhmm;

  const splashClock = document.getElementById('splashClock');
  if (splashClock) splashClock.textContent = hhmmss;

  const homeClock = document.getElementById('homeClock');
  if (homeClock) homeClock.textContent = hhmm;

  const homeDate = document.getElementById('homeDate');
  if (homeDate) {
    const days = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT'];
    const months = ['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC'];
    homeDate.textContent = `${days[now.getDay()]} \u00B7 ${pad(now.getDate())} ${months[now.getMonth()]} ${now.getFullYear()}`;
  }
}
updateClocks();
setInterval(updateClocks, 1000);

// ---------- Splash screen ----------
const splash = document.getElementById('splash');
const enterBtn = document.getElementById('enterBtn');
if (enterBtn && splash) {
  enterBtn.addEventListener('click', () => {
    splash.classList.add('hidden');
    splash.style.display = 'none'; // works even before style.css defines .hidden
    document.body.classList.add('entered');
  });
}

// ---------- Theme toggle ----------
const themeToggle = document.getElementById('themeToggle');
if (themeToggle) {
  themeToggle.addEventListener('click', () => {
    const current = document.documentElement.getAttribute('data-theme');
    const next = current === 'dark' ? 'light' : 'dark';
    document.documentElement.setAttribute('data-theme', next);
    try {
      localStorage.setItem('theme', next);
    } catch (e) {
      // localStorage unavailable — theme just won't persist across visits
    }
  });
}

// ---------- Toast on load ----------
const toast = document.getElementById('toast');
if (toast) {
  setTimeout(() => toast.classList.add('show'), 600);
  setTimeout(() => toast.classList.remove('show'), 3200);
}
