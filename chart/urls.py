from django.contrib import admin
from django.urls import path
from  chart import views
from  . import views

app_name= 'chart'

urlpatterns=[
    path('', views.home, name='home'),
    path('covid19_chart/', views.home, name='covid19_chart'),

]