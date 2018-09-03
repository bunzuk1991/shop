from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=80, blank=True, null=True, default=None)
    description = models.TextField(blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "Номенклатура: %s, Опис: %s" % (self.name, self.description)

    class Meta:
        verbose_name = "Номенклатура"
        verbose_name_plural = "Список номенклатури"


class ProductImage(models.Model):
    product = models.ForeignKey(Product, blank=True, null=True, default=None, on_delete="CASCADE")
    image = models.ImageField(upload_to="product_images/")
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "Картинка: %s" % self.id

    class Meta:
        verbose_name = "Картинка"
        verbose_name_plural = "Список картинок товарів"