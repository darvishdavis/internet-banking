from django.urls import path, include

from bank_body import views

app_name = 'bank_body'

urlpatterns = [
    path('', views.new, name='new'),
    path('form/', views.fill_form, name='fill_form'),

]