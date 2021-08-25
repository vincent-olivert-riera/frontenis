from django.urls import path

from . import views

urlpatterns = [
    path("v1/login", views.Login.as_view()),
    path("v1/logout", views.Logout.as_view()),
]
