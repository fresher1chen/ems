from django.contrib import admin
from django.urls import path,include
from admin01 import views

app_name = 'admin01'
urlpatterns = [

    path('addemp/', views.addemp, name='addemp'),
    path('addlogic/', views.addlogic, name='addlogic'),
    path('emplist/', views.emplist, name='emplist'),
    path('updateemp/', views.updateemp, name='updateemp'),
    path('updatelogic/', views.updatelogic, name='updatelogic'),
    path('delete/', views.delete, name='delete'),

]
