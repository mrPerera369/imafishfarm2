from django.urls import path
from . import views

app_name = 'sold'

urlpatterns = [
    path('', views.index, name='index'),
    # Add more paths as needed
]
