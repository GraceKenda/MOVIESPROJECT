from django.urls import path
from . import views

app_name = 'movapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('create_movie', views.create_movie, name='create_movie'),
    path('login/', views.login_user, name='login_user'),
    path('logout/', views.logout_user, name='logout_user'),
    path('register/', views.register, name='signup'),




]
