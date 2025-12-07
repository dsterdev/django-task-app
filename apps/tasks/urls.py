from django.urls import path
from apps.tasks import views
from django.contrib.auth.views import LogoutView, LoginView

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('tasks/', views.TaskListView.as_view(), name='tasks_list'),
    path('tasks/create', views.TaskCreateView.as_view(), name='create_tasks'),
    path('tasks/<int:pk>/detail', views.TaskDetailView.as_view(), name='detail_tasks'),
    path('tasks/<int:pk>/complate', views.complete_task, name='complete_tasks'),
    path('tasks/<int:pk>/delete', views.TaskDeleteview.as_view(), name='delete_tasks'),
    path('tasks/completed', views.TaskCompletedListView.as_view(), name='completed_tasks'),
]
