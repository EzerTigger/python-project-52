from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.CreateTaskView.as_view(), name='create_task'),
    # path('<int:pk>/delete/', views.DeleteStatusView.as_view(),
    #      name='delete_status'),
    path('', views.TasksList.as_view(), name='task_list'),
    # path('<int:pk>/update/', views.UpdateStatusView.as_view(),
    #      name='update_status'),
]