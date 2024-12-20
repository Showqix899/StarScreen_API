from django.urls import path

from .views import AdminMovieApiView,ListOfMovies,MovieDetailsView


urlpatterns = [
    path('movie-add/',AdminMovieApiView.as_view(),name='movie-add'),#to post method admin only
    path('movie-update/<str:pk>/',AdminMovieApiView.as_view(),name='movie-update'), #for put and patch method admin only
    path('movie-delete/<str:pk>/',AdminMovieApiView.as_view(),name='movie-delete'), #for delete method admin only
    path('get-movie/',ListOfMovies.as_view(),name='get-movie'), #for get method user/admin
    path('movie-details/<str:id>/',MovieDetailsView.as_view(),name='movie-details'), #for get method user/admin
]
