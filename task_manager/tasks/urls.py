from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.CreateTaskView.as_view(), name='create_task'),
    path('<int:pk>/delete/', views.DeleteTaskView.as_view(),
         name='delete_task'),
    path('', views.TasksList.as_view(), name='task_list'),
    path('<int:pk>/update/', views.UpdateTaskView.as_view(),
         name='update_task'),
    path('<int:pk>/', views.TaskDetail.as_view(), name='task_detail')
]
