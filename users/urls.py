
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views




urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='listings/items_list.html'), name='items_list'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/home.html'), name='logout'),

]
