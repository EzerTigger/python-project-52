from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('users/create/', views.CreateUserView.as_view(), name='create_user'),
    path('users/', views.UsersListView.as_view(), name='users')
]
