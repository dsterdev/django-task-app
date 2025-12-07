from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'important']        
        exclude = ['user']
        widgets = {
            'title' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Escribe el titulo de la tarea'}),
            'description' : forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Escribe la dscripcion de la tarea'}),
            'important' : forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }