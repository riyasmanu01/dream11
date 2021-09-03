from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('manageplayer',views.manageplayer,name='manageplayer'),
    path('addplayers',views.addplayers,name='addplayers'),
]