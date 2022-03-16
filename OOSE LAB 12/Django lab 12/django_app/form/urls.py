from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = "form"),
    path('enterform/', views.player, name = "enterform"),
]