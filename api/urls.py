from django.urls import path
from .views import TaskListView,TaskIdView,TaskDoneView,TaskUndoneView

urlpatterns = [
    path("tasks/", TaskListView.as_view()),
    path('task/<int:id>',TaskIdView.as_view()),
    path('task/<int:id>/done',TaskDoneView.as_view()),
    path('task/<int:id>/undone',TaskUndoneView.as_view())
]
