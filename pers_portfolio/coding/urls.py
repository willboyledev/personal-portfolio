from django.contrib import admin
from django.urls import path
from coding import views


urlpatterns = [
    path('', views.coding, name='coding'),
]