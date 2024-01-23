from django.urls import path
from . import views

urlpatterns = [
    # path('create/', views.CreateStatusView.as_view(), name='create_status'),
    # path('<int:pk>/delete/', views.DeleteStatusView.as_view(),
        # name='delete_status'),
    path('', views.LabelsList.as_view(), name='label_list'),
    #path('<int:pk>/update/', views.UpdateStatusView.as_view(),
        # name='update_status'),
]
