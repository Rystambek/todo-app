from django.urls import path
from .views import TaskListView, TaskView

urlpatterns = [
    path("tasks/", TaskListView.as_view()),
    path("tasks/<int:id>/", TaskView.as_view()),
]
