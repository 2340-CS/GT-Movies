from django.shortcuts import render
from django.http import HttpResponse;
from rest_framework import views, permissions
from rest_framework.response import Response
from django.contrib.auth.models import User
from . import serializers


class ListUsers(views.APIView): 

    permission_classes = [permissions.AllowAny]

    def get(self, request):
        all_users = User.objects.all()
        print(all_users)
        serializer = serializers.UserSerializer(data=all_users, many=True)
        if (serializer.is_valid()):
            return Response(serializer.data)
        else:
            return Response("Error retrieving user list.")
        
class ListMovies(views.APIView): 

    permission_classes = [permissions.AllowAny]

    def get(self, request): 
        all_movies = Movie.objects.all()
        serializer = serializers.MovieSerializer(all_movies, many=True)
        if (serializer.is_valid()):
            return Response(serializer.data)
        else:
            return Response("Error retrieving user list.")
        
class RegisterUser(views.APIView):

    permission_classes = [permissions.AllowAny]

    # Only adds users if they don't already exist
    def post(self, request):

        user_serializer = serializers.UserSerializer(data=request.data)

        if (user_serializer.is_valid()):
            username = request.query_params.get("username")
            if username not in User.objects.all().filter(username=username):
                user_serializer.save()
                return Response(user_serializer.validated_data)
        else:
            return Response('User not created sucessfully')
        
class LoginUser(views.APIView): 

    permission_classes = [permissions.AllowAny]

    






