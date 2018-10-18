from django.urls import path
from . import views
urlpatterns = [
        path('', views.index, name='index'),
        path('another', views.another, name='another'),
        path('login', views.login, name="login"),
        path('logOut', views.logOut, name='logOut'),
    ]
