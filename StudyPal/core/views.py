from django.shortcuts import render
from .models import Notes, Tasks
from django.views.generic import ListView

def DashBoardView(request):
    notes = Notes.objects.all()
    tasks = Tasks.objects.all()
    return render(request, 'core/dashboard.html', {
        'notes': notes,
        'tasks': tasks
    })

class NotesView(ListView):
    model = Notes
    template_name = 'core/notes.html'
    context_object_name = 'notes'

class TaskView(ListView):  
    model = Tasks
    template_name = 'core/tasks.html'
    context_object_name = 'tasks'
