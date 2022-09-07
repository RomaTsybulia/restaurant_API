from rest_framework import serializers

from restaurant.models import Dish, Category, Menu


class DishSerializer(serializers.ModelSerializer):
    model = Dish
    fields = ("id", "name", "description", "price", "category")


class CategorySerializer(serializers.ModelSerializer):
    dishes = DishSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ("id", "name", "dishes")


class MenuSerializer(serializers.ModelSerializer):
    categories = serializers.SlugRelatedField(
        many=True, read_only=True, slug_field="name"
    )

    class Meta:
        model = Menu
        fields = ("id", "content", "restaurant", "categories")
