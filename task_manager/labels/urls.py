from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.CreateLabelView.as_view(), name='create_label'),
    # path('<int:pk>/delete/', views.DeleteStatusView.as_view(),
        # name='delete_status'),
    path('', views.LabelsList.as_view(), name='label_list'),
    path('<int:pk>/update/', views.UpdateLabelView.as_view(),
         name='update_label'),
]
