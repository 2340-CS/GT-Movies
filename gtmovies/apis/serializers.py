from rest_framework import serializers
from apis.models import *
from django.contrib.auth.models import User

from django.contrib.auth import authenticate

# Class for serializing user
class UserSerializer(serializers.ModelSerializer):
    class Meta: 
        model = User
        fields = ['id', 'username', 'email', 'password']
