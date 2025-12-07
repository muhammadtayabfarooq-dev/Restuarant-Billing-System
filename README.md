Restaurant Billing System (Django)

What it is:

Backend-focused Django app for restaurant billing. Manage a menu, capture orders with per-order tax, service, and discounts, and render printable receipts. Frontend is lightweight HTML/CSS to keep focus on server-side logic.
Key features:

Menu management via Django admin: item code, name, price, active flag.
Order form: set tax %, service %, discount (amount or percent), and item quantities.
Pricing computed on the backend: subtotal, service charge, discount, tax, total.
Recent orders list and printable receipt page (with a browser print button).
Seed migration loads a starter menu for demos.
Tech stack:

Python 3, Django 4.2, HTML/CSS templates (no JS build step), SQLite by default (swap in Postgres/MySQL via DATABASES in restaurant/settings.py).
Project structure (high level):

restaurant/urls.py — routes for order intake and receipts.
orders/models.py — MenuItem, Order, OrderItem with pricing logic.
orders/views.py — order intake handling and receipt rendering.
templates/ — base layout, order form, receipt pages.
orders/migrations/0002_seed_menu.py — seeds sample menu items.
Quick start (Windows, PowerShell):

Activate venv: ..venv\Scripts\Activate.ps1
Apply migrations (safe to rerun): python manage.py migrate
Run server: python manage.py runserver
Open http://127.0.0.1:8000/ to create orders and view receipts.
Admin (optional):

Create superuser: python manage.py createsuperuser
Login: http://127.0.0.1:8000/admin/ to manage menu and orders.
Common commands:

Run server: python manage.py runserver
Run migrations: python manage.py migrate
Create admin user: python manage.py createsuperuser
Collect static for deployment: python manage.py collectstatic
Deployment notes:

Set ALLOWED_HOSTS in restaurant/settings.py.
Configure DATABASES for your production DB.
Run collectstatic and serve static files via your web server/CDN.
Use a process manager (e.g., gunicorn + nginx) in production.
Data and defaults:

Sample menu items seeded by orders/migrations/0002_seed_menu.py.
Orders store per-order tax, service, and discount values; totals are derived properties.
Receipt page includes a print action.
Author:
Muhammad Tayab Farooq — 2 years of Django experience
Contact: muhammadtayabfarooq@gmail.com
