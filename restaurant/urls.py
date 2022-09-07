from django.urls import path, include
from rest_framework import routers

from restaurant.views import DishViewSet, CategoryViewSet, MenuViewSet

router = routers.DefaultRouter()
router.register("dishes", DishViewSet)
router.register("categories", CategoryViewSet)
router.register("menu", MenuViewSet)

urlpatterns = [
    path("", include(router.urls))
]

app_name = "restaurant_tenant"
