from django.urls import path
from webapp.views.base import IndexView, IndexRedirectView
from webapp.views.tasks import add_view, TaskDetail, TaskUpdateView, delete_view, confirm_delete


urlpatterns = [
    path("",  IndexView.as_view(), name='index'),
    path("task/", IndexRedirectView.as_view(), name='articles_index_redirect'),
    path("task/add/", add_view, name='task_add'),
    path("task/<int:pk>", TaskDetail.as_view(), name='task_detail'),
    path("task/<int:pk>/update/", TaskUpdateView.as_view(), name='task_update'),
    path("task/<int:pk>/delete/", delete_view, name='task_delete'),
    path("task/<int:pk>/confirm_delete/",
         confirm_delete, name='confirm_delete'),
]
