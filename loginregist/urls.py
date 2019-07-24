from django.urls import path
from loginregist import views

app_name = 'loginregist'

urlpatterns = [
    path('login', views.login, name='login'),
    path('loginlogic', views.loginlogic,name='loginlogic'),
    path('regist', views.regist, name='regist'),
    path('registlogic', views.registlogic, name='registlo'),
    path('getcapthca', views.getcapthca, name='getcapthca'),
    path('checkname',views.checkname,name='checkname'),
    path('checkcode',views.checkcode,name='checkcode'),

]