from django.shortcuts import render
from django.core.handlers.wsgi import WSGIRequest
from webapp.models import Task


def index_view(request: WSGIRequest):
    tasks = Task.objects.exclude(is_deleted=True)
    context = {
        'tasks': tasks
    }
    return render(request, 'index.html', context=context)
