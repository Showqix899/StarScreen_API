from django.urls import path

from .views import LogView

urlpatterns = [
    path('', LogView.as_view({'get': 'list'})),
    path('<int:pk>/', LogView.as_view({'get': 'retrieve'})),
]