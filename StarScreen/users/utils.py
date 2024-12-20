from django.contrib.auth.tokens import default_token_generator  # Generates secure tokens
from django.core.mail import send_mail  # Used to send email
from django.conf import settings  # For email settings



def generate_verification_token(user):

    return default_token_generator.make_token(user) #generates a unique token

def send_verification_email(user_email,token):

    subject="verify your email address" #email subject
    message=f"""
    Hello,
    Please verify your email by clicking the link below:
    http://127.0.0.1:8000/user/verify-email/?email={user_email}&token={token}
    """ # Email message containing the verification link

    from_email=settings.DEFAULT_FROM_EMAIL # sender email from from django.conf import setting
    send_mail(subject,message,from_email,[user_email])

def get_client_ip(request):

    x_forwarded_for=request.Meta.get('HTTP_X_FORWARDED_FOR')

    if x_forwarded_for:
        ip=x_forwarded_for.split(',')[0]
    else:
        ip=request.META.get('REMOTE_ADDR')

    return ip