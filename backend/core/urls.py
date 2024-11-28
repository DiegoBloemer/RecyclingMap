from django.urls import path
from . import views

urlpatterns = [
    path('adicionar_local/', views.adicionar_local, name='adicionar_local'),
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
]
