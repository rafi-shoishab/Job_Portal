from django.urls import path
from . import views

urlpatterns = [
    path('applied/', views.apply, name='apply'), 
] 