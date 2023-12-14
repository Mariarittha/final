from django.contrib import messages
from django.http import JsonResponse
from django.views import generic
from django.views.generic import ListView,CreateView,DeleteView,DetailView, UpdateView,TemplateView
from django.urls import reverse_lazy
from django_filters.views import FilterView
from .filter import EstadiaFilter
from django.contrib.messages import views
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import EstadiaForm, ProdutosForm, HospedeForm, FilomenasForm
from .models import estadia, Produtos, filomenas, hospede
from users.permissions import AdminPermission


# não logado

class Home(generic.TemplateView):
    template_name = "nao/home.html"
    
class filomena_nao(generic.TemplateView):
    template_name = "nao/filomena.html"

# logado

class Home2(generic.TemplateView):
    template_name = "logado/home2.html"

class forms(generic.TemplateView):
    template_name = "logado/forms.html"
    

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>....
#                                                                        CRUDS

# CRUD de Estadia
class ListarEstadia(LoginRequiredMixin, generic.ListView, FilterView):
    model = estadia
    template_name = 'estadia/listar.html'
    context_object_name = 'estadias'
    filterset_class = EstadiaFilter
    paginate_by = 3

class ListarEstadiafilo(LoginRequiredMixin, generic.ListView, FilterView):
    model = estadia
    template_name = 'filomenas/listar_estadia.html'
    context_object_name = 'estadias'
    filterset_class = EstadiaFilter
    paginate_by = 3
    
class ListarEstadianao( generic.ListView):
    model = estadia
    template_name = 'estadia/listar_nao.html'
    context_object_name = 'estadias'
    paginate_by = 3

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
    success_url = reverse_lazy("filomenas:listar_log")
    success_message = "Estadia cadastrada com sucesso!"

class AtualizarEstadia(AdminPermission, LoginRequiredMixin, views.SuccessMessageMixin, generic.UpdateView):
    model = estadia
    form_class = EstadiaForm
    template_name = "estadia/form.html"
    success_url = reverse_lazy("filomenas:listar_filo")
    success_message = "Estadia atualizada com sucesso!"
    
class Atualizarfilomena(AdminPermission, LoginRequiredMixin, views.SuccessMessageMixin, generic.UpdateView):
    model = filomenas
    form_class = FilomenasForm
    template_name = 'filomenas/form.html'
    success_url = reverse_lazy("filomenas:listar_filomena")
    success_message = "Perfil atualizado com sucesso, {{ request.user.username }}!" 


class ApagarEstadia(AdminPermission, LoginRequiredMixin, generic.DeleteView):
    model = estadia
    success_url = reverse_lazy("filomenas:listar_filo")
    success_message = "Estadia removida com sucesso!"

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>....
    
# CRUD de perfil do hospede 

class Perfil(LoginRequiredMixin,generic.TemplateView):
    model = hospede
    template_name = 'logado/perfil.html'
    
class Listarhospede(LoginRequiredMixin, generic.ListView):
    model = hospede
    template_name = 'logado/perfilinfo.html'
    context_object_name = 'hospedes'

class Detalharhospede(generic.DetailView):
    model = hospede
    template_name = "perfil/form_hospede.html"

class Criarhospede(LoginRequiredMixin, views.SuccessMessageMixin, generic.CreateView):
    model = hospede
    form_class = HospedeForm
    template_name = 'perfil/form_hospede.html'
    success_url = reverse_lazy("filomenas:perfil")
    success_message = "Hospede cadastrado com sucesso!"
       

class Atualizarhospede(LoginRequiredMixin, views.SuccessMessageMixin, generic.UpdateView):
    model = hospede
    form_class = HospedeForm
    template_name = "perfil/form_hospede.html"
    success_url = reverse_lazy("filomenas:listar_hospede")
    success_message = "Perfil atualizado com sucesso"

class Apagarhospede(AdminPermission, LoginRequiredMixin, generic.DeleteView):
    model = hospede
    success_url = reverse_lazy("filomenas:home")
  
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>....
  
# CRUD de perfil filomenas

class Detalharfilomena(generic.DetailView):
    model = filomenas
    template_name = 'filomenas/detalhar_filo.html'

class Listarfilomena(LoginRequiredMixin, generic.ListView):
    model = filomenas
    template_name = 'filomenas/listar_filomenas.html'
    context_object_name = 'filomenas'
    paginate_by = 3

class Criarfilomena(views.SuccessMessageMixin, generic.CreateView):
    model = filomenas
    form_class = FilomenasForm
    template_name = 'filomenas/form.html'
    success_url = reverse_lazy("filomenas:listar_filomena")
    success_message = "filomena cadastrada com sucesso!"

class CriarEstadia(LoginRequiredMixin, views.SuccessMessageMixin, generic.CreateView):
    model = estadia
    form_class = EstadiaForm
    template_name = 'estadia/form.html'
    success_url = reverse_lazy("filomenas:listar_filo")
    success_message = "Estadia cadastrada com sucesso!"

class Atualizarfilomena(AdminPermission, LoginRequiredMixin, views.SuccessMessageMixin, generic.UpdateView):
    model = filomenas
    form_class = FilomenasForm
    template_name = 'filomenas/form.html'
    success_url = reverse_lazy("filomenas:listar_filomena")
    success_message = "Perfil atualizado com sucesso, {{ request.user.username }}!" 

class Apagarfilomena(AdminPermission, LoginRequiredMixin, generic.DeleteView):
    success_message = "Filomena removida com sucesso!"
    model = filomenas
    success_url = reverse_lazy("filomenas:listar_filomena")
