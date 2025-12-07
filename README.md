# Restaurant Billing System (Django)

Backend-focused Django app to manage a restaurant menu, capture customer orders with tax/service/discounts, and render printable receipts.

## Quick start
```bash
# Activate the virtual environment
.venv\Scripts\activate

# Run the server
python manage.py runserver
```
Open http://127.0.0.1:8000/ to create orders and view receipts.

## Admin (optional)
```bash
python manage.py createsuperuser
```
Log in at http://127.0.0.1:8000/admin/ to manage menu items and orders.

## Notes
- Sample menu items are seeded via migration (`orders/migrations/0002_seed_menu.py`).
- Order form supports percent or flat discounts plus adjustable tax and service charge per order.
- Receipts show itemized totals and include a print button.
