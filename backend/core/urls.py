from django.urls import path
from . import views

urlpatterns = [
    path('buscar_pontos/', views.buscar_pontos, name='buscar_pontos'),
    path('pontos/', views.pontos_coleta, name='pontos_coleta'),
    path('logout/', views.logout_view, name='logout'),
    path('adicionar_local/', views.adicionar_local, name='adicionar_local'),
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
]
