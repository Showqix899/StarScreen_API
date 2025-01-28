from django.db.models.signals import post_save
from django.dispatch import receiver

from logs.models import Log
from reviews.models import Review


@receiver(post_save, sender=Review)
def review_log(sender, instance, created, **kwargs):
    action = "created" if created else "updated"
    Log.objects.create(
        action=f"Review {action}", 
        data={
            "review_id": str(instance.id),  # Ensure the UUID is serialized as a string
            "review_text": instance.review
        }
    )

    print(f"Review log created")
        

