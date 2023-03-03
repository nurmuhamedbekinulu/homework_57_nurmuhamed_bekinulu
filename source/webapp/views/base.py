from django.shortcuts import render
from django.core.handlers.wsgi import WSGIRequest
from webapp.models import Task
from django.views.generic import TemplateView, RedirectView


# def index_view(request: WSGIRequest):
#     tasks = Task.objects.exclude(is_deleted=True)
#     context = {
#         'tasks': tasks
#     }
#     return render(request, 'index.html', context=context)

class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = Task.objects.exclude(is_deleted=True)
        return context
    
class IndexRedirectView(RedirectView):
    pattern_name = 'index'