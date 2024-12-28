from django.urls import path


from .views import ReviewCreateView,ReviewUpdateView,ReviewDeleteView,ReviewDetailsView,ReviewListView

urlpatterns = [
    path('review-create/', ReviewCreateView.as_view(), name='review-create'),
    path('review-list/', ReviewListView.as_view(), name='review-list'),
    path('review-update/<str:pk>/', ReviewUpdateView.as_view(), name='review-update'),
    path('review-delete/<str:pk>/', ReviewDeleteView.as_view(), name='review-delete'),
    path('review-details/<str:pk>/', ReviewDetailsView.as_view(), name='review-detials'),

    
    
]
