from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_index, name='index'),
    path('accounts/login/', views.view_login, name='login'),
    path('accounts/logout/', views.view_logout, name='logout'),
    path('scraping/', views.view_scraping, name='scraping'),
]
