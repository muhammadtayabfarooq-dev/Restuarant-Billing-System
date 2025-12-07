# **Restaurant Billing System (Django)**

A backend-focused **Django application** for restaurant billing. It allows creating menu items, taking orders, applying tax/service/discounts, and generating clean printable receipts. Frontend is intentionally simple (pure HTML/CSS) to highlight server-side logic.

---

## **⭐ Features**

* **Menu Management (Admin Panel)**

  * Item code, name, price, active/inactive toggle.

* **Order Form**

  * Add item quantities.
  * Apply **tax %**, **service charge %**, and **discount** (percent or fixed amount).

* **Automatic Price Calculations**

  * Subtotal
  * Service charge
  * Discount
  * Tax
  * **Final total**

* **Order History**

  * Recent orders list.

* **Printable Receipt**

  * Clean PDF-style layout with browser print support.

* **Seed Data Included**

  * A migration that loads a starter menu for demo/testing.

---

## **🛠 Tech Stack**

* **Python 3**
* **Django 4.2**
* HTML/CSS templates (no JS build tools)
* SQLite (default)

  * Compatible with PostgreSQL/MySQL (update `DATABASES` in `restaurant/settings.py`)

---

## **📂 Project Structure (High Level)**

```
restaurant/
│
├── restaurant/urls.py              # Main routes
│
├── orders/
│   ├── models.py                   # MenuItem, Order, OrderItem + pricing logic
│   ├── views.py                    # Order processing + receipt rendering
│   ├── migrations/
│       ├── 0002_seed_menu.py       # Preloads sample menu items
│
└── templates/                      # Base layout, order form, receipt
```

---

## **🚀 Quick Start (Windows, PowerShell)**

### **1. Activate virtual environment**

```
.\venv\Scripts\Activate.ps1
```

### **2. Apply migrations**

```
python manage.py migrate
```

### **3. Run the server**

```
python manage.py runserver
```

Open:
👉 **[http://127.0.0.1:8000/](http://127.0.0.1:8000/)**
to create orders and print receipts.

---

## **🔐 Admin Panel (Optional)**

### Create superuser

```
python manage.py createsuperuser
```

### Access admin

👉 **[http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)**
Manage menu items and orders.

---

## **📘 Common Commands**

```
python manage.py runserver
python manage.py migrate
python manage.py createsuperuser
python manage.py collectstatic
```

---

## **🛠 Deployment Notes**

* Set `ALLOWED_HOSTS` in `restaurant/settings.py`
* Configure `DATABASES` for production PostgreSQL/MySQL
* Run:

  ```
  python manage.py collectstatic
  ```
* Serve static files via Nginx/CDN
* Use a process manager (Gunicorn, etc.)

---

## **📦 Data & Defaults**

* Sample menu items loaded via:
  `orders/migrations/0002_seed_menu.py`
* Orders include per-order:

  * Tax %
  * Service charge %
  * Discount
* Final totals are computed properties.
* Receipt page includes a browser print button.

---

## **👤 Author**

**Muhammad Tayab Farooq**
**Email:** [muhammadtayabfarooq@gmail.com](mailto:muhammadtayabfarooq@gmail.com)
**Experience:** 2 years in Django & Python development
