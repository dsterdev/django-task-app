from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import  CreateView
from django.urls import reverse_lazy



# Create your views here.
class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('signin')
    template_name = 'auth/signup.html'
    
    def form_valid(self, form):
        return super().form_valid(form)