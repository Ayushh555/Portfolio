# Portfolio — Django (backend + frontend, one server)

## Folder structure
```
portfolio_backend/
├── manage.py
├── requirements.txt
├── core/
│   ├── models.py              # Project, Skill, ContactMessage
│   ├── serializers.py
│   ├── views.py                # API views + home view
│   ├── admin.py
│   ├── urls.py                  # /api/... routes
│   ├── templates/
│   │   └── index.html          # the HTML page
│   └── static/
│       ├── css/style.css
│       └── js/script.js
└── portfolio_backend/
    ├── settings.py
    └── urls.py                  # '/' -> home page, '/api/' -> API, '/admin/' -> admin
```

## Setup
```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py seed_data          # loads sample projects/skills
python manage.py createsuperuser    # create your admin login
python manage.py runserver
```

Open http://127.0.0.1:8000/  → the portfolio site itself (HTML+CSS+JS all served by Django).
Open http://127.0.0.1:8000/admin/  → manage Projects, Skills, and read Contact Messages.

## API Endpoints
- GET  /api/projects/
- GET  /api/skills/
- POST /api/contact/   → { "name": "...", "email": "...", "message": "..." }  (rate-limited: 5/hour)

## How it fits together
- `core/templates/index.html` is rendered by the `home` view in `core/views.py` at `/`.
- `core/static/css/style.css` and `core/static/js/script.js` are linked from the template using
  `{% static %}` tags, so Django serves them automatically — no separate frontend server needed.
- `script.js` calls the API using a relative path (`/api/...`) since everything is on the same server now.

## Before deploying
- Set `DEBUG = False`
- Set a real `SECRET_KEY`
- Set `ALLOWED_HOSTS`
- Run `python manage.py collectstatic` (for production static file serving)
