from django.shortcuts import render
from django.http import HttpResponse;
from rest_framework import views, permissions
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from . import serializers


class ListUsers(views.APIView): 

    permission_classes = [permissions.AllowAny]

    def get(self, request):
        all_users = User.objects.all()
        print(all_users)
        serializer = serializers.UserSerializer(all_users, many=True)
        return Response(serializer.data)
        
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

            username = user_serializer.validated_data['username']
            password = user_serializer.validated_data['password']
            email = user_serializer.validated_data['email']
            
            try:
                User.objects.get(username=username)
                return Response({
                    "error": "The username inputted is already in use"
                }, status=404)
            except User.DoesNotExist:
                User.objects.create_user(username=username, password=password, email=email)
                return Response(user_serializer.validated_data, status=200)
            
        return Response({
                    "error": "Bad data"
                }, status=404)
        
class LoginUser(views.APIView): 

    permission_classes = [permissions.AllowAny]

    # Authenticates User
    def post(self, request): 

        username = request.data.get("username")
        password = request.data.get("password")

        if not (username and password): 
            return Response({"error": "Username and password are required"}, status=400)

        user = authenticate(request, username=username, password=password)

        if user is not None: 
            login(request, user)
            return Response({"User sucessfully logged in"}, status="200")
        
        return Response({"Failed to login"}, status="404")


class LogoutUser(views.APIView): 

    permission_classes = [permissions.IsAuthenticated]

    # Logs out user
    def get(self, request): 
        if (request.user is not None and request.user.is_authenticated):
            logout(request)
            return Response({
                "message": "Successfully logged out", 
            }, status=200)
        else: 
            return Response({
                "error": "Failed to log out", 
            }, status=400)







