
from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.index),
    path('products/<str:product_id>', views.get_by_id),
]