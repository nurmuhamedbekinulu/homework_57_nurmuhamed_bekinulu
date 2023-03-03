from django import forms
from django.forms import widgets
from django.core.exceptions import ValidationError
from webapp.models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = {'title', 'description', 'status', 'completion_date'}
        labels = {
            'title': 'Заголовок',
            'description': 'Описание',
            'status': 'Статус',
            'completion_date': 'Выполнить до"'
        }

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if len(title) < 2:
            raise ValidationError('Заголовок должен быть длиннее 2 символов')
        return title
