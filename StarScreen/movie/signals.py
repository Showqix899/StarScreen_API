

from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Movie
from logs.models import Log

@receiver(post_save, sender=Movie)
def log_movie(sender, instance, **kwargs):
    action="created"
    Log.objects.create(
        action=action,
        data={
            "movie_id": str(instance.id), #must make the UUID a string
            "movie_title": instance.title, 
        })
    print("movie created")