from django.db import models
from products.models import Product


class Status(models.Model):
    name = models.CharField(max_length=80, blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "Статус: %s" % self.id

    class Meta:
        verbose_name = "Статус"
        verbose_name_plural = "Список статусів"


class Order(models.Model):
    customer_name = models.CharField(max_length=80, blank=True, null=True, default=None)
    customer_email = models.EmailField(blank=True, null=True, default=None)
    customer_phone = models.CharField(max_length=48, blank=True, null=True, default=None)
    status = models.ForeignKey(Status, on_delete="CASCADE")
    comments = models.TextField(blank=True, null=True, default=None)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "Замовлення: %s %s" % (self.id, self.status.name)

    class Meta:
        verbose_name = "Замовлення"
        verbose_name_plural = "Список замовлень"


class ProductInOrder(models.Model):
    order = models.ForeignKey(Order, blank=True, null=True, default=None, on_delete="CASCADE")
    product = models.ForeignKey(Product, blank=True, null=True, default=None, on_delete="CASCADE")
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "Товар: %s" % self.product.name

    class Meta:
        verbose_name = "Товар у замовлені"
        verbose_name_plural = "Список товарів у замовленні"
