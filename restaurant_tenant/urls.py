from django.urls import path, include
from rest_framework import routers

from restaurant_tenant.views import (
    RestaurantViewSet, CategoryViewSet, MenusViewSet, DishViewSet
)

router = routers.DefaultRouter()
router.register("restaurants", RestaurantViewSet)
router.register("categories", CategoryViewSet)
router.register("dishes", DishViewSet)
router.register("menu", MenusViewSet)

urlpatterns = [
    path("", include(router.urls)),
]

app_name = "public"
