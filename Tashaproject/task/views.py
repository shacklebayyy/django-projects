from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
tasks = ["buy groceries", "watch football", "visit a friend"]

def Tasks(request):
    return render(request, 'task.html',{
        "tasks": tasks
    })

def add(request):
    return render(request, "add.html")