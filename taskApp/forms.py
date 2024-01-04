from django import forms

class FormTask(forms.Form):
    name = forms.CharField(max_length=250,label="Nombre de la tarea")