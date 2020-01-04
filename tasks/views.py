from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Task
from .forms import TaskForm


# Create your views here.
def home(request):
    tasks = Task.objects.all()
    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()

        return redirect('/')

    context = {
        'tasks': tasks,
        'form': form,
    }
    return render(request, 'tasks/list.html', context)


def update_task(request, pk):
    task = Task.objects.get(pk=pk)
    form = TaskForm(instance=task)

    if request.method=='POST':
        form = TaskForm(request.POST, instance=task)  # We need instance because it wont create new item instead
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {
        'form': form,
    }
    return render(request, 'tasks/update.html', context)


def delete_task(request, pk):
    task = Task.objects.get(pk=pk)

    if request.method == 'POST':
        task = Task.objects.get(pk=pk)
        task.delete()
        return redirect('/')

    context = {
        'task': task
    }

    return render(request, 'tasks/delete.html', context)