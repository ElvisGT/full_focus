from . import views
from django.urls import path

urlpatterns = [
    path("",views.tasks,name="tasks"),
    path("task_detail/<int:id>",views.task_detail,name="task_detail"),
    path("delete/<int:id>",views.deleteTask,name="deleteTask")
]