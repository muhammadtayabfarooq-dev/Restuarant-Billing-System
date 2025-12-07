from django.db import models
from django.core.validators import MinValueValidator


class MenuItem(models.Model):
    code = models.CharField(max_length=8, unique=True)
    name = models.CharField(max_length=128)
    price = models.DecimalField(max_digits=8, decimal_places=2, validators=[MinValueValidator(0)])
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["code"]

    def __str__(self) -> str:
        return f"{self.code} - {self.name}"


class Order(models.Model):
    DISCOUNT_PERCENT = "percent"
    DISCOUNT_AMOUNT = "amount"
    DISCOUNT_CHOICES = [
        (DISCOUNT_PERCENT, "Percent"),
        (DISCOUNT_AMOUNT, "Flat amount"),
    ]

    customer_name = models.CharField(max_length=128, blank=True)
    tax_rate = models.DecimalField(max_digits=5, decimal_places=2, default=5.00, validators=[MinValueValidator(0)])
    service_charge_rate = models.DecimalField(max_digits=5, decimal_places=2, default=10.00, validators=[MinValueValidator(0)])
    discount_value = models.DecimalField(max_digits=8, decimal_places=2, default=0, validators=[MinValueValidator(0)])
    discount_type = models.CharField(max_length=10, choices=DISCOUNT_CHOICES, default=DISCOUNT_AMOUNT)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self) -> str:
        return f"Order #{self.pk or 'new'}"

    @property
    def subtotal(self):
        return sum(item.subtotal for item in self.items.all())

    @property
    def service_charge(self):
        return (self.subtotal * self.service_charge_rate) / 100

    @property
    def discount_amount(self):
        base = self.subtotal + self.service_charge
        if self.discount_type == self.DISCOUNT_PERCENT:
            return (base * self.discount_value) / 100
        return min(self.discount_value, base)

    @property
    def tax(self):
        taxable_base = self.subtotal + self.service_charge - self.discount_amount
        return (taxable_base * self.tax_rate) / 100

    @property
    def total(self):
        return self.subtotal + self.service_charge + self.tax - self.discount_amount


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name="items", on_delete=models.CASCADE)
    menu_item = models.ForeignKey(MenuItem, on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    unit_price = models.DecimalField(max_digits=8, decimal_places=2, validators=[MinValueValidator(0)])

    class Meta:
        verbose_name = "Order item"
        verbose_name_plural = "Order items"

    @property
    def subtotal(self):
        return self.unit_price * self.quantity

    def __str__(self) -> str:
        return f"{self.menu_item.name} x {self.quantity}"

# Create your models here.
