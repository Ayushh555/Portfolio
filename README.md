<div align="center">

# 🖥️ Ayush Chandel — Developer Portfolio

**A dark, code-editor-themed, phone-home-screen-style portfolio — built as a single deployable Django project.**

[![Django](https://img.shields.io/badge/Django-6.1-092E20?style=flat&logo=django&logoColor=white)](https://www.djangoproject.com/)
[![DRF](https://img.shields.io/badge/Django%20REST-Framework-red?style=flat&logo=django&logoColor=white)](https://www.django-rest-framework.org/)
[![Python](https://img.shields.io/badge/Python-3.13-3776AB?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](#license)

[Live Demo](#) · [Report Bug](../../issues) · [Request Feature](../../issues)

</div>

---

## 📱 About

This isn't your typical scrolling portfolio. It's designed like a **phone's home screen** — status bar, app icons, a dock, and full-page "apps" for Resume, Skills, Projects, About, Internship, and Contact, all wrapped in a **dark code-editor aesthetic**.

Everything — frontend, REST API, and admin panel — runs from **one Django project**. No separate frontend server, no build step. Clone it, migrate it, run it.

## ✨ Features

- 🎨 **Phone-style UI** — splash screen, home screen with app grid, dock navigation, and `:target`-based page routing (no JS framework needed)
- 🌗 **Dark / light theme toggle** with `localStorage` persistence
- ⚡ **Django REST Framework API** for Projects, Skills, and Contact messages
- 🛡️ **Rate-limited contact form** (5 requests/hour) with honeypot spam protection
- 📧 **Email notifications** on new contact form submissions
- 🔧 **Admin-editable site info** — update your location and "currently learning" status straight from the Django admin, no code changes needed
- 🖼️ Fully responsive — optimized for small phones, tablets, and desktop
- 🗂️ Clean, self-documenting Django app structure

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Backend | Python, Django, Django REST Framework |
| Frontend | HTML5, CSS3 (custom properties / theming), Vanilla JavaScript |
| Database | SQLite (dev) |
| Admin | Django Admin |

## 📂 Project Structure

```
portfolio_backend/
├── manage.py
├── requirements.txt
├── core/
│   ├── models.py              # Project, Skill, ContactMessage, SiteInfo
│   ├── serializers.py
│   ├── views.py                # API views + home view
│   ├── admin.py
│   ├── urls.py                  # /api/... routes
│   ├── templates/
│   │   └── index.html          # the entire single-page app
│   └── static/
│       ├── css/style.css
│       ├── js/script.js
│       ├── img/                # profile photo, background
│       └── files/               # resume PDF
└── portfolio_backend/
    ├── settings.py
    └── urls.py                  # '/' -> home page, '/api/' -> API, '/admin/' -> admin
```
## 🖼️ Screenshots

<img width="1854" height="892" alt="Screenshot_19-8-2026_13310_127 0 0 1" src="https://github.com/user-attachments/assets/871eb166-cad5-409f-8e3b-653ccac275d4" />
<img width="1859" height="878" alt="Screenshot_19-8-2026_13327_127 0 0 1" src="https://github.com/user-attachments/assets/e00bb6d0-c355-4950-8e0f-eeec5d244a79" />
<img width="457" height="290" alt="Screenshot_19-8-2026_13342_127 0 0 1" src="https://github.com/user-attachments/assets/6b609ebf-1df9-4af2-9245-682387d8f94a" />
<img width="1135" height="923" alt="Screenshot_19-8-2026_131055_127 0 0 1" src="https://github.com/user-attachments/assets/c535794b-c81e-44c2-bb24-ff09abc194f1" />

```

### Installation

```bash
# Clone the repo
git clone https://github.com/Ayushh555/<repo-name>.git
cd <repo-name>

# Install dependencies
pip install -r requirements.txt

# Set up the database
python manage.py makemigrations core
python manage.py migrate

# Create an admin login
python manage.py createsuperuser

# Run the dev server
python manage.py runserver
```




## 👨‍💻 About Me

I'm a **Python/Django developer** who learns by building and breaking things. I'm currently looking for my first full-time developer role.

- 📍 Based in Himachal Pradesh, India
- 💼 [LinkedIn](https://linkedin.com/in/ayush-chandel-a2b726252)
- 🐙 [GitHub](https://github.com/Ayushh555)
- ✉️ ayushchandel95@gmail.com


---

<div align="center">

Built 🔧 by **Ayush Chandel**

</div>
