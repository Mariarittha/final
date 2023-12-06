from django.contrib import messages
from django.views.generic import ListView,CreateView,DeleteView,DetailView, UpdateView,TemplateView
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.messages import views
from django.contrib.auth.mixins import LoginRequiredMixin
from requests import request
from .forms import EstadiaForm, ProdutosForm, HospedeForm, FilomenasForm
from .models import estadia, Produtos, filomenas, hospede

# não logado

class Home(generic.TemplateView):
    template_name = "nao/home.html"


# logado

class Home2(generic.TemplateView):
    template_name = "logado/home2.html"

class forms(generic.TemplateView):
    template_name = "logado/forms.html"

class perfil(generic.TemplateView):
    template_name = "logado/perfil.html"

#CRUDS

# CRUD de Estadia
class ListarEstadia(LoginRequiredMixin, generic.ListView):
    model = estadia
    template_name = 'estadia/listar.html'
    context_object_name = 'estadias'
    paginate_by = 5
    
class ListarEstadianao( generic.ListView):
    model = estadia
    template_name = 'estadia/listar_nao.html'
    context_object_name = 'estadias'
    paginate_by = 5

class Detalharestadialog(generic.DetailView):
    model = estadia
    template_name = 'estadia/detalhar_logado.html'

class DetalharEstadia(generic.DetailView):
    model = estadia
    template_name = 'estadia/detalhar.html'


class CriarEstadia(LoginRequiredMixin, views.SuccessMessageMixin, generic.CreateView):
    model = estadia
    form_class = EstadiaForm
    template_name = 'estadia/form.html'
    success_url = reverse_lazy("filomenas:home")
    success_message = "Estadia cadastrada com sucesso!"

class AtualizarEstadia(LoginRequiredMixin, views.SuccessMessageMixin, generic.UpdateView):
    model = estadia
    form_class = EstadiaForm
    success_url = reverse_lazy("reservas:home")
    success_message = "Estadia atualizada com sucesso!"

class ApagarEstadia(LoginRequiredMixin, generic.DeleteView):
    model = estadia
    success_url = reverse_lazy("reservas:home")
    
    
# CRUD de perfil do hospede 

class Detalharhospede(generic.DetailView):
    model = hospede

class Criarhospede(LoginRequiredMixin, views.SuccessMessageMixin, generic.CreateView):
    model = hospede
    form_class = HospedeForm
    template_name = 'perfil/form_hospede.html'
    success_url = reverse_lazy("filomenas:home")
    success_message = "Hospede cadastrado com sucesso!"

class Atualizarhospede(LoginRequiredMixin, views.SuccessMessageMixin, generic.UpdateView):
    model = hospede
    form_class = HospedeForm
    success_url = reverse_lazy("reservas:home")
    success_message = "Perfil atualizado com sucesso, {{ request.user.username }}!" 

class Apagarhospede(LoginRequiredMixin, generic.DeleteView):
    model = hospede
    success_url = reverse_lazy("reservas:home")
    
# CRUD de perfil filomenas

class Detalharfilomena(generic.DetailView):
    model = hospede
    template_name = 'filomenas/detalhar_filo.html'


class Criarfilomena(LoginRequiredMixin, views.SuccessMessageMixin, generic.CreateView):
    model = filomenas
    form_class = FilomenasForm
    template_name = 'filomenas/form.html'
    success_url = reverse_lazy("filomenas:home")
    success_message = "filomena cadastrada com sucesso!"

class Atualizarfilomena(LoginRequiredMixin, views.SuccessMessageMixin, generic.UpdateView):
    model = filomenas
    form_class = FilomenasForm
    success_url = reverse_lazy("reservas:home")
    success_message = "Perfil atualizado com sucesso, {{ request.user.username }}!" 

class Apagarfilomena(LoginRequiredMixin, generic.DeleteView):
    model = filomenas
    success_url = reverse_lazy("reservas:home")
