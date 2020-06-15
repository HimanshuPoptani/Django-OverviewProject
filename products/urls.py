from django.urls import path
from . import views

urlpatterns = [
    path('' , views.function),
    path('new', views.new)
]
