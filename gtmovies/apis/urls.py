from django.urls import path, include
from . import views  # Ensure views is properly imported
from rest_framework import routers

urlpatterns = [
    path('user-list', views.ListUsers.as_view(), name="ListUsers"),
    path('register-user', views.RegisterUser.as_view(), name="RegisterUser")
]