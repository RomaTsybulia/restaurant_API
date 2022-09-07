from django.contrib import admin

from restaurant.models import Menu, Dish, Category

admin.site.register(Dish)
admin.site.register(Category)
admin.site.register(Menu)
