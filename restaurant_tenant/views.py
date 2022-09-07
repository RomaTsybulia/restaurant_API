from rest_framework import viewsets

from restaurant_tenant.models import Restaurant, Category,  Menu, Dish
from restaurant_tenant.serializers import (
    RestaurantSerializer,
    CategorySerializer,
    MenusSerializer,
    DishSerializer,
)


class RestaurantViewSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class DishViewSet(viewsets.ModelViewSet):
    queryset = Dish.objects.all()
    serializer_class = DishSerializer


class MenusViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenusSerializer
