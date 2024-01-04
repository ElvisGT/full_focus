from django.shortcuts import render,redirect
from django.http import HttpResponse
from . import forms
from .models import Task

# Create your views here.
def tasks(request):
    # Get tasks
    tasks = Task.objects.values()
    if request.method == 'GET':
        formTask = {
            "formTask":forms.FormTask(),
            "tasks":tasks
            }
        return render(request,'tasks.html',formTask)
    else:
        #Comprobar si existe la tarea
        task = Task.objects.filter(name=request.POST['name'].capitalize())
        if not task:
            Task.objects.create(name=request.POST['name'].capitalize())
        else:
            task.update(active=True)
        
        return redirect('tasks')
        
def deleteTask(request,id):
    task = Task.objects.filter(id=id)
    task.update(active=False)
    return redirect('tasks')

def task_detail(request,id):
    task = Task.objects.filter(id = id)
    return render(request,'task_detail.html',{
        'name':task.get()
    })