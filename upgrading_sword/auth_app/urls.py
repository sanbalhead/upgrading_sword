from atexit import register
from telnetlib import LOGOUT
from unicodedata import name
from xml.etree.ElementInclude import include
from auth_app.urls import *
from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('login/', views.login_view, name="login"),
    path('register/', views.register_user, name="register"),
    path('logout/', LogoutView.as_view(), name="Logout")
]