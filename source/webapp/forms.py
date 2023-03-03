from django import forms
from django.forms import widgets


class TaskForm(forms.Form):
    title = forms.CharField(max_length=200, required=True, label='Заголовок')
    description = forms.CharField(
        max_length=3000, required=True, label='Описание', widget=widgets.Textarea)
    status = forms.CharField(max_length=200, required=True, label='Статус')
