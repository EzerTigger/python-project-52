from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.CreateUserView.as_view(), name='create_user'),
    path('<int:pk>/delete/', views.DeleteUserView.as_view(), name='delete'),
    path('<int:pk>/update/', views.UpdateUserView.as_view(), name='update'),
    path('', views.UsersListView.as_view(), name='users'),

]
