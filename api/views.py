from django.views import View
from django.http import JsonResponse
from .models import Task

def to_dict(task: Task) -> dict:
    return {
        "id": task.id,
        "title": task.title,
        "description": task.description,
        "done": task.done,
        "created": task.created,
        "updated": task.updated,
    }


class TaskListView(View):
    def get(self, request):
        tasks = Task.objects.all()
        return JsonResponse([to_dict(task) for task in tasks], safe=False, status=200)
