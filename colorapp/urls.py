from django.contrib import admin
from django.urls import path, include
from colorapp import views

urlpatterns = [
   path('extract_colors/', views.extract_colors, name='extract_colors')
]
