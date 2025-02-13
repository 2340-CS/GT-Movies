from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='moviesapp.index'),
    path('about', views.about, name='moviesapp.about')
]
