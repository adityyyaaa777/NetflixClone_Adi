# Netflix Clone — React + Django

Simple Netflix style streaming catalog with a React frontend and Django REST backend.

## Features

### User
* Browse movies and TV shows
* Featured hero section
* Search titles by name or genre
* View title details
* Responsive Netflix style layout

### Admin
* Django staff account authentication via JWT
* Create titles
* Update titles
* Delete titles
* Mark titles as featured
* Manage from the React admin panel
* Django Admin is also available

## Backend

```bash
cd backend
python -m venv venv
# Windows
venv\\Scripts\\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py seed_movies
python manage.py runserver
```

## Frontend

```bash
cd frontend
npm install
npm run dev
```

The frontend expects Django at `http://127.0.0.1:8000`. You can override it using:

```text
VITE_API_URL=http://your-backend/api
```

## Admin login

Create a Django superuser with `python manage.py createsuperuser`. Use that username and password in the React Admin Login. Django's staff flag allows CRUD access through the API.
