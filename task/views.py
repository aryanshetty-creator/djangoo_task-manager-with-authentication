from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth.views import LoginView

# Login view
class CustomLoginView(LoginView):
    template_name = 'users/login.html'


# Home view
@login_required
def home(request):
    return render(request, 'tasks/home.html')  # Use a proper template path

# Task list view
@login_required
def task_list(request):
    tasks = Task.objects.filter(user=request.user)  # Show tasks for the logged-in user
    return render(request, 'tasks/task_list.html', {'tasks': tasks})

# Add task view
@login_required
def add_task(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        Task.objects.create(user=request.user, title=title, description=description)
        return redirect('task_list')
    return render(request, 'tasks/add_task.html')

# Edit task view
@login_required
def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    if request.method == 'POST':
        task.title = request.POST.get('title')
        task.description = request.POST.get('description')
        task.completed = 'completed' in request.POST
        task.save()
        return redirect('task_list')
    return render(request, 'tasks/edit_task.html', {'task': task})

# Delete task view
@login_required
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    if request.method == 'POST':
        task.delete()
        return redirect('task_list')
    return render(request, 'tasks/delete_task.html', {'task': task})
