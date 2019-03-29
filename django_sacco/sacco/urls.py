from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name ='sacco-home'),
    path('account/', views.account, name ='sacco-account'),
]
