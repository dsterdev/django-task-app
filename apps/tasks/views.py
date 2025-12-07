from .models import Task
from .forms import TaskForm
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, ListView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import  get_object_or_404, redirect
from django.utils import timezone
# from django.shortcuts import render, redirect

# Create your views here.
class HomeView(TemplateView):
    template_name = "tasks/home.html"
    
class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = "tasks"
    template_name = "tasks/tasks_list.html"
    paginate_by = 4
    
    def get_queryset(self):
        return Task.objects.filter(user = self.request.user, date_completed__isnull = True).order_by('-important')
        
class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    form_class = TaskForm
    template_name = "tasks/create_task.html"
    success_url = reverse_lazy("tasks_list")
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
    def form_invalid(self, form):
        return messages.error(self.request, "Hubo un error al guardar los cambios")

class TaskDetailView(LoginRequiredMixin, UpdateView):
    model = Task
    form_class = TaskForm
    template_name = "tasks/task_detail.html"
    success_url = reverse_lazy("tasks_list")
    context_object_name = "task"
    
    def get_queryset(self):
        return Task.objects.filter(user = self.request.user)

@login_required  
def complete_task(request, pk):
    task = get_object_or_404(Task, pk = pk, user = request.user)
    if request.method == "POST":
        task.date_completed = timezone.now()
        task.save()
        return redirect('tasks_list')
    
class TaskDeleteview(LoginRequiredMixin,DeleteView):
    model = Task
    template_name = "tasks/confrim_delete_task.html"
    success_url = reverse_lazy("tasks_list")
    
    def get_queryset(self):
        return Task.objects.filter(user = self.request.user)
    
class TaskCompletedListView(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = "tasks"
    template_name = "tasks/tasks_list.html"
    paginate_by = 4
    
    def get_queryset(self):
        return Task.objects.filter(user = self.request.user, date_completed__isnull = False).order_by('-date_completed')
    
    