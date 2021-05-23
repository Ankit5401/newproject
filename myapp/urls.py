from myapp import views
from django.contrib import admin
from django.urls import path
from django.urls.conf import include 

urlpatterns = [
    path("", views.index, name='home')
]
