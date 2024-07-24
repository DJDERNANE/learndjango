
from django.urls import path
from . import views

urlpatterns = [
    path('account/', views.signup),
    path('account/details', views.userInfo),
    path('account/update', views.updateUserInfo),
    path('account/delete', views.deleteUser),
]