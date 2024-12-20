from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TicketViewSet

# Create a router and register the viewset
router = DefaultRouter()
router.register(r'tickets', TicketViewSet, basename='ticket')

urlpatterns = [
    path('', include(router.urls)),  # Include all router-generated URLs
]
