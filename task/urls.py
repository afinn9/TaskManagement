from django.urls import path
from . import views

urlpatterns = [
    path('update/<uuid>/', views.edit_task),
    path('add/', views.add_task),
    path('list/', views.view_task),
    path('is_valid/<uuid>/', views.manage_task_state),
]
