from django.urls import path, re_path, include
from main import views

app_name = 'main'

urlpatterns = [
    path("", views.onrrr)
]
