
from django.urls import path
from . import views
import product

urlpatterns = [
    path('product/', views.index),
]