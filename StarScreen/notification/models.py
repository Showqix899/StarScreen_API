from django.db import models

# Create your models here.



from users.models  import User

class Notification(models.Model):
    NOTIFICATION_TYPES = [
        ('INFO', 'Information'),
        ('ALERT', 'Alert'),
        ('MESSAGE', 'Message'),
    ]

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='notifications',
        help_text="The user to whom the notification belongs."
    )
    title = models.CharField(
        max_length=255,
        help_text="Title or summary of the notification."
    )
    message = models.TextField(
        blank=True,
        null=True,
        help_text="Optional detailed message of the notification."
    )
    notification_type = models.CharField(
        max_length=10,
        choices=NOTIFICATION_TYPES,
        default='INFO',
        help_text="Type of notification (e.g., Information, Alert, etc.)."
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        help_text="Timestamp when the notification was created."
    )
    is_read = models.BooleanField(
        default=False,
        help_text="Flag to indicate if the notification has been read."
    )
    link = models.URLField(
        blank=True,
        null=True,
        help_text="Optional link for more details or action."
    )

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Notification"
        verbose_name_plural = "Notifications"

    def __str__(self):
        return f"{self.title} ({'Read' if self.is_read else 'Unread'})"
