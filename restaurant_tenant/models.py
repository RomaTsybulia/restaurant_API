from django.db import models
from django_tenants.models import TenantMixin, DomainMixin


class Restaurant(TenantMixin):
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)

    auto_create_schema = True

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "categories"


class Dish(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    price = models.FloatField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Menu(models.Model):
    name = models.TextField()
    restaurant = models.ForeignKey(
        Restaurant,
        unique=True,
        on_delete=models.CASCADE
    )
    categories = models.ForeignKey(Category, related_name="menu", on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Domain(DomainMixin):
    pass
