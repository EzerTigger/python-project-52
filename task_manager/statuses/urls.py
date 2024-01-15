from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.CreateStatusView.as_view(), name='create_status'),
]