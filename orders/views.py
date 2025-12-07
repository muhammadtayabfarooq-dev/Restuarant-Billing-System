from decimal import Decimal
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.contrib import messages

from .models import MenuItem, Order, OrderItem


def _parse_items_from_request(request):
    """
    Expect inputs like quantity-<menu_code>. Return list of (MenuItem, quantity).
    """
    items = []
    for key, value in request.POST.items():
        if not key.startswith("quantity-"):
            continue
        code = key.split("quantity-", 1)[1]
        try:
            qty = int(value)
        except ValueError:
            qty = 0
        if qty > 0:
            item = MenuItem.objects.filter(code=code, is_active=True).first()
            if item:
                items.append((item, qty))
    return items


def order_intake(request):
    menu = MenuItem.objects.filter(is_active=True).order_by("code")

    if request.method == "POST":
        customer_name = request.POST.get("customer_name", "").strip()
        tax_rate = Decimal(request.POST.get("tax_rate") or "0")
        service_rate = Decimal(request.POST.get("service_charge_rate") or "0")
        discount_value = Decimal(request.POST.get("discount_value") or "0")
        discount_type = request.POST.get("discount_type") or Order.DISCOUNT_AMOUNT

        parsed_items = _parse_items_from_request(request)
        if not parsed_items:
            messages.error(request, "Please add at least one item with quantity.")
            return redirect("order_intake")

        order = Order.objects.create(
            customer_name=customer_name,
            tax_rate=tax_rate,
            service_charge_rate=service_rate,
            discount_value=discount_value,
            discount_type=discount_type,
        )

        for item, qty in parsed_items:
            OrderItem.objects.create(
                order=order,
                menu_item=item,
                quantity=qty,
                unit_price=item.price,
            )

        messages.success(request, "Order created successfully.")
        return redirect(reverse("order_receipt", args=[order.id]))

    orders = Order.objects.prefetch_related("items__menu_item")[:10]
    context = {"menu": menu, "orders": orders}
    return render(request, "orders/order_intake.html", context)


def order_receipt(request, order_id):
    order = get_object_or_404(Order.objects.prefetch_related("items__menu_item"), pk=order_id)
    return render(request, "orders/receipt.html", {"order": order})
