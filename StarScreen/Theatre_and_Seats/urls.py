from django.urls import path,include
from rest_framework.routers import DefaultRouter


from .views import (TheatreAdminView,SeatAdminView,ScheduleSetUpAdminView,)

router= DefaultRouter()
router.register(r'theatre',TheatreAdminView)
router.register(r'seat',SeatAdminView)
router.register(r'schedule',ScheduleSetUpAdminView)

urlpatterns = [

    path('',include(router.urls)),

   
]
