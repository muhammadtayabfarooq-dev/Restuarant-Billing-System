# Restaurant Billing System (Django)

This project is a backend-focused Django application for managing restaurant billing. It provides menu management, order creation, automated pricing calculations, and printable receipts. The interface is intentionally simple, using basic HTML and CSS to keep the emphasis on Django and backend logic.

---

## Overview

The system allows restaurants to:

* Manage menu items through the Django admin panel.
* Create orders by selecting item quantities.
* Apply tax percentage, service charges, and discounts (either fixed amount or percentage).
* Automatically calculate subtotal, service charge, discount, tax, and final total.
* View recent orders.
* Print clean, receipt-style order summaries.
* Load a predefined sample menu using a seed migration.

---

## Technologies Used

* Python 3
* Django 4.2
* HTML/CSS templates (no JavaScript build tools required)
* SQLite database by default

  * Can be replaced with PostgreSQL or MySQL by updating the `DATABASES` configuration in `restaurant/settings.py`

---

## Project Structure (High-Level)

```
restaurant/
│
├── restaurant/urls.py              # URL routes
│
├── orders/
│   ├── models.py                   # MenuItem, Order, OrderItem and pricing logic
│   ├── views.py                    # Order creation and receipt rendering
│   ├── migrations/
│       ├── 0002_seed_menu.py       # Seeds sample menu items
│
└── templates/                      # Base layout, order form, and receipt templates
```

---

## Getting Started (Windows, PowerShell)

Activate the virtual environment:

```
.\venv\Scripts\Activate.ps1
```

Apply database migrations:

```
python manage.py migrate
```

Start the development server:

```
python manage.py runserver
```

After running the server, open the project in your browser:

```
http://127.0.0.1:8000/
```

This will allow you to create orders and view or print receipts.

---

## Admin Access (Optional)

Create a superuser account:

```
python manage.py createsuperuser
```

Access the Django admin panel:

```
http://127.0.0.1:8000/admin/
```

The admin panel can be used to manage menu items and review orders.

---

## Common Django Commands

```
python manage.py runserver
python manage.py migrate
python manage.py createsuperuser
python manage.py collectstatic
```

---

## Deployment Notes

* Update `ALLOWED_HOSTS` in `restaurant/settings.py` for production.
* Configure the `DATABASES` setting if using PostgreSQL or MySQL.
* Run `python manage.py collectstatic` before deployment.
* Serve static files using a web server such as Nginx or via a CDN.
* Use a process manager such as Gunicorn when deploying to production.

---

## Data and Defaults

* Sample menu data is provided through the migration file:
  `orders/migrations/0002_seed_menu.py`
* Each order stores its tax percentage, service charge percentage, and discount value.
* Final totals are calculated as model properties.
* The receipt page includes a simple print layout for convenience.

---

## Author

**Muhammad Tayab Farooq**
Email: **[muhammadtayabfarooq@gmail.com](mailto:muhammadtayabfarooq@gmail.com)**
Experience: **2 years working with Python and Django**
