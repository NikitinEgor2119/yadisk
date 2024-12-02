from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('download_selected/', views.download_selected_files, name='download_selected_files'),
]
