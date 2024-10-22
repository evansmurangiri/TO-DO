from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
from  django.urls import reverse

tasks=["Clean", "wash"]

class NewTaskForm(forms.Form):
    task=forms.CharField(label="New Task")

# Create your views here.
def index(request):
    return render(request, "Task/index.html",{
        "tasks":tasks
    })
def add(request):
    if request.method == "POST" :
        form =NewTaskForm(request.POST)
        if form.is_valid():
            task=form.cleaned_data["task"]
            tasks.append(task)
            return HttpResponseRedirect(reverse("Task:index"))


    return render(request, "Task/add.html",{
        "form":NewTaskForm()
    })