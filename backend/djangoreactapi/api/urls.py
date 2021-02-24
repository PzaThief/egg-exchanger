from django.urls import path
from . import views

urlpatterns = [
    path("api/unit/", views.UnitListCreate.as_view()),
]