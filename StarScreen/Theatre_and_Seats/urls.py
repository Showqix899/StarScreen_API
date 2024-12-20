from django.urls import path


from .views import TheatreAdminView,TheatreListView,TheaterDetailsView,SeatAdminView,SeatDetailsView,SeatListView,ScheduleSetUpAdminView

urlpatterns = [

    #theatre paths
    path("theatre-add/",TheatreAdminView.as_view(),name='theatre-add/'), #post theatre
    path("theatre-list/",TheatreListView.as_view(),name='theatre-list/'),# get theatre
    path("theatre-update/<str:pk>/",TheatreAdminView.as_view(),name='theatre-update/'), #theatre patch and put
    path("theatre-delete/<str:pk>/",TheatreAdminView.as_view(),name="theatre-delete"), #theatre delete
    path("theatre-detail/<str:pk>/",TheaterDetailsView.as_view(),name='theatre-detail/'), #theatre details 


    #seat paths
    path("seat-add/",SeatAdminView.as_view(),name='seat-add'), #post seat
    path("seat-list/",SeatListView.as_view(),name='seat-list'), #get seat
    path("seat-update/<str:pk>/",SeatAdminView.as_view(),name='seat-update'), #seat put and patch
    path("seat-delete/<str:pk>/",SeatAdminView.as_view(),name='seat-delete'), # seat delete
    path("seat-detail/<str:pk>/",SeatDetailsView.as_view(),name="seat-details"),#seat details

    #schedule
    path('schedule/', ScheduleSetUpAdminView.as_view(), name='schedule-create'),  # POST for creating schedules
    path('schedule/<str:pk>/', ScheduleSetUpAdminView.as_view(), name='schedule-detail'),  # PUT, PATCH, DELETE

   
]
