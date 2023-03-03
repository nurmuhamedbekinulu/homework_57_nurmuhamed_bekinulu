from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, redirect, get_object_or_404
from webapp.models import Task
from static.classes.static import Static
from webapp.forms import TaskForm
from django.views.generic import TemplateView


# def add_view(request: WSGIRequest):
#     if request.method == "GET":
#         return render(request, 'task_create.html', context={'choices': Static.choices})

#     if request.POST.get('completion_date') != "":
#         completion_date = request.POST.get('completion_date')
#     else:
#         completion_date = None

#     task_data = {
#         'title': request.POST.get('title'),
#         'description': request.POST.get('description'),
#         'status': request.POST.get('status'),
#         'completion_date': completion_date
#     }
#     task = Task.objects.create(**task_data)
#     return redirect('task_detail', pk=task.pk)

def add_view(request: WSGIRequest):
    if request.method == "GET":
        form = TaskForm()
        return render(request, 'task_create.html', context={'choices': Static.choices, 'form': form})
    
    form = TaskForm(data=request.POST)
    if not form.is_valid():
        return render(request, 'task_create.html', context={'choices': Static.choices, 'form': form})
    else:
        task = form.save()
        return redirect('task_detail', pk=task.pk)


# def detail_view(request, pk):
#     task = get_object_or_404(Task, pk=pk)
#     return render(request, 'task.html', context={
#         'task': task
#     })

class TaskDetail(TemplateView):
    template_name = 'task.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['task'] = get_object_or_404(Task, pk=kwargs['pk'])
        return context


# def update_view(request, pk):
#     task = get_object_or_404(Task, pk=pk)
#     if request.method == "POST":
#         task.title = request.POST.get('title')
#         task.description = request.POST.get('description')
#         task.status = request.POST.get('status')
#         task.completion_date = request.POST.get('completion_date')
#         task.save()
#         return redirect('task_detail', pk=task.pk)
#     return render(request, 'task_update.html', context={'task': task, 'choices': Static.choices})

class TaskUpdateView(TemplateView):
    template_name = 'task_update.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['task'] = get_object_or_404(Task, pk=kwargs['pk'])
        context['form'] = TaskForm(instance=context['task'])
        return context
    
    def post(self, request, *args, **kwargs):
        task = get_object_or_404(Task, pk=kwargs['pk'])
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_detail', pk=task.pk)
        return render(request, 'task_update.html', context={'form': form,'task': task})


def delete_view(request, pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'task_confirm_delete.html', context={'task': task})


def confirm_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('index')
