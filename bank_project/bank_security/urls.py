
from django.contrib import admin
from django.urls import path, include

from bank_security import views

app_name = 'bank_security'

urlpatterns = [
    path('', views.home, name='home'),
    path('login', views.log_in, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.log_out, name='logout'),

]