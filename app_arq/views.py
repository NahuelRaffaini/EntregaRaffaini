from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.db.models import Q
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Proyecto, Trabajador

# Create your views here.

def inicio(req):

    return render(req, "inicio.html")


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/app_arq')  
        else:
            messages.error(request, 'Credenciales inválidas. Por favor, inténtelo de nuevo.')
    
    return render(request, 'login.html')

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('/app_arq/login')


def filtrar_proyectos(request):
    query = request.GET.get('q')
    proyectos = Proyecto.objects.filter(
        Q(titulo__icontains=query) 
    ) if query else Proyecto.objects.all()

    return render(request, 'proyect_list.html', {'proyectos': proyectos})


class ProyectoCreateView(LoginRequiredMixin, CreateView):
    model = Proyecto
    fields = '__all__' 
    template_name = 'proyect_create.html'
    success_url = '/app_arq/lista_proyecto/'
    login_url = '/app_arq/login/'
    context_object_name = "proyecto"
    
    def form_valid(self, form):
        proyecto = form.save(commit=False)
        proyecto.user = self.request.user
        proyecto.save()
        return super().form_valid(form)

class ProyectoUpdateView(LoginRequiredMixin, UpdateView):
    model = Proyecto
    template_name = 'proyect_update.html'
    fields = '__all__' 
    success_url = '/app_arq/lista_proyecto/'
    login_url = '/app_arq/login/'
    context_object_name = "proyecto"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class ProyectoDeleteView(LoginRequiredMixin, DeleteView):
    model = Proyecto
    template_name = 'estudiante_delete.html'
    success_url = '/app_arq/lista_proyecto/'
    login_url = '/app_arq/login/'
    
    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)

class ProyectoListView(LoginRequiredMixin, ListView):
    model = Proyecto
    template_name = "proyect_list.html"
    context_object_name = "proyectos"
    login_url = '/app_arq/login/'


class TrabajadorCreate(CreateView):
    model = Trabajador
    fields = '__all__' 
    template_name = "trabajador_create.html"
    success_url = '/app-coder/trabajador_list'