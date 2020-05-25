from django.shortcuts import render
from django.core.mail import send_mail
from django.shortcuts import redirect
from django.contrib import messages
from django.urls import reverse
from accounts.models import Token
import sys
from django.contrib import auth, messages
from accounts.authentication import PasswordlessAuthenticationBackend

# Create your views here.

def send_login_email(request):
    email = request.POST['email']
    token = Token.objects.create(email=email)
    url = request.build_absolute_uri(
        reverse('login') + '?token=' + str(token.uid)
    )
    message_body = f'Use this link to log in:\n\n{url}'
    send_mail(
        'Your login link for Superlists',
        message_body,
        'noreply@superlists',
        [email],
    )
    messages.success(
        request,
        "Check your email, we've sent you a link you can use to log in."
    )
    return redirect('/')

def login(request):
    # print('login view', file=sys.stderr)
    # uid = request.GET.get('uid')
    # user = auth.authenticate(uid=uid)
    # if user is not None:
    #     auth.login(request, user)
    user = PasswordlessAuthenticationBackend().authenticate(uid=request.GET.get('token'))
    print(user)
    if user:
        auth.login(request, user)
    return redirect('/')


# def authenticate(self, uid):
#     print('test')
#     try:
#         token = Token.objects.get(uid=uid)
#         return User.objects.get(email=token.email)
#     except User.DoesNotExist:
#         return User.objects.create(email=token.email)
#     except Token.DoesNotExist:
#         return None
#
# def get_user(self, email):
#     try:
#         return User.objects.get(email=email)
#     except User.DoesNotExist:
#         return None
