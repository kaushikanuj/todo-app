from django import forms
from .models import TodoApp


class TodoForm(forms.ModelForm):
    class Meta:
        model = TodoApp
        fields = '__all__'
