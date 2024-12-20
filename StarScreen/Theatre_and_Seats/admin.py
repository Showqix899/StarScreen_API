from django.contrib import admin

# Register your models here.
#from .models
from .models import Theatre,Seat,Schedule

admin.site.register(Theatre)
admin.site.register(Seat)
admin.site.register(Schedule)
