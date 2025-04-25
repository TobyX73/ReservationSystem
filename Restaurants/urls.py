from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RestaurantViewSet

router = DefaultRouter()
router.register(r'restaurants', RestaurantViewSet, 'restaurant')

urlpatterns = [
    path('api/v1/', include(router.urls)),
]