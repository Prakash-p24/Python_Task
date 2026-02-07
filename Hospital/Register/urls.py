
from django.urls import path
from . import views

urlpatterns = [
    
    path("",views.Index),
    path("Register/success",views.Home),
    path("get-slots/", views.get_available_slots, name="get_slots"),
]