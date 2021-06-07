from django.contrib import admin
from django.urls import path, include
from home import views


urlpatterns = [
    path('', views.index, name="login"),
    path('loginuser', views.login, name="loginuser"),
    path('loginuser', views.logout, name="logoutuser"),

]
