from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.dispatch import receiver
from django.utils.timezone import now

from .models import User
from logs.models import Log
from .utils import get_client_ip

@receiver(user_logged_in)
def log_login(sender, request, user, **kwargs):
    Log.objects.create(
        user=user,
        action="Login",
        data={
            "ip_address": get_client_ip(request),
            "user_agent": request.META.get('HTTP_USER_AGENT', 'Unknown')
        },
        timestamp=now()
    )
    print("loged in")

@receiver(user_logged_out)
def log_logout(sender, request, user, **kwargs):
    Log.objects.create(
        user=user,
        action="Logout",
        data={
            "ip_address": get_client_ip(request),
            "user_agent": request.META.get('HTTP_USER_AGENT', 'Unknown')
        },
        timestamp=now()
    )
