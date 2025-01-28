from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Ticket
from logs.models import Log

@receiver(post_save, sender=Ticket)
def ticket_saved(sender, instance, created, **kwargs):
    
    action = "created" if created else "updated"
    data = {"ticket": instance.id, "user": instance.user.id, "movie": instance.schedule.movie.title}
    Log.objects.create(action=action, data=data)
    
    print(f"Log {instance.id}: {action}")
    
    