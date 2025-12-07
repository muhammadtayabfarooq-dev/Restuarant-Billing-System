from django.db import migrations


def seed_menu(apps, schema_editor):
    MenuItem = apps.get_model("orders", "MenuItem")
    items = [
        ("A1", "Margherita Pizza", 12.50),
        ("A2", "Pepperoni Pizza", 13.50),
        ("A3", "Veggie Delight", 11.00),
        ("B1", "Caesar Salad", 8.50),
        ("B2", "Greek Salad", 9.00),
        ("C1", "Grilled Chicken", 14.00),
        ("C2", "Steak Frites", 18.00),
        ("C3", "Penne Alfredo", 13.00),
        ("D1", "Iced Tea", 3.00),
        ("D2", "Fresh Lemonade", 3.50),
        ("D3", "Espresso", 2.75),
        ("E1", "Chocolate Cake", 6.00),
        ("E2", "Cheesecake", 6.50),
    ]
    for code, name, price in items:
        MenuItem.objects.update_or_create(code=code, defaults={"name": name, "price": price, "is_active": True})


def remove_menu(apps, schema_editor):
    MenuItem = apps.get_model("orders", "MenuItem")
    MenuItem.objects.all().delete()


class Migration(migrations.Migration):
    dependencies = [
        ("orders", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(seed_menu, remove_menu),
    ]
