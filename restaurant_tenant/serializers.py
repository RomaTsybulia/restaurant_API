from rest_framework import serializers

from restaurant_tenant.models import Restaurant, Category, Dish, Menu


class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ("id", "name", "type", "description")


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("id", "name")


class DishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dish
        fields = ("id", "name", "description", "price", "category")


class MenusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ("name", "restaurant", "categories")
