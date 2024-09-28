from django.contrib.auth import views as auth_views
from django.urls import path

from . import views

urlpatterns = [
    path('', views.frontpage, name="frontpage"),
    path('signup/', views.signup, name="signup"),
    path('logout/', views.user_logout, name = "logout"), #Changed from tutorial which used older version
    path('login/', views.user_login, name = "login"),
]