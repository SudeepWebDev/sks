from django.urls import path
from . import views

urlpatterns = [
    path("", views.members, name="members"),
    path("data/", views.show, name="show"),
    path("login/", views.login, name="login")
]
