from django.contrib import messages
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.messages import views
from django.contrib.auth.mixins import LoginRequiredMixin
from requests import request
from .forms import EstadiaForm, ProdutosForm, HospedeForm, FilomenasForm
from .models import estadia, Produtos, filomenas, hospede
from users.permissions import AdministradorPermission


# não logado

class Home(generic.TemplateView):
    template_name = "nao/home.html"

# logado

class Home2(generic.TemplateView):
    template_name = "logado/home2.html"

class forms(generic.TemplateView):
    template_name = "logado/forms.html"

class Perfil(generic.TemplateView):
    template_name = "logado/perfil.html"

#CRUDS

# CRUD de Estadia
class ListarEstadia(LoginRequiredMixin, generic.ListView):
    model = estadia
    template_name = 'estadia/listar.html'
    context_object_name = 'estadias'
    paginate_by = 5

class ListarEstadiafilo(LoginRequiredMixin, generic.ListView):
    model = estadia
    template_name = 'filomenas/listar_estadia.html'
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
    success_url = reverse_lazy("filomenas:listar_log")
    success_message = "Estadia cadastrada com sucesso!"

class AtualizarEstadia(LoginRequiredMixin, views.SuccessMessageMixin, generic.UpdateView):
    model = estadia
    form_class = EstadiaForm
    template_name = "estadia/form.html"
    success_url = reverse_lazy("filomenas:listar_filo")
    success_message = "Estadia atualizada com sucesso!"

class ApagarEstadia(LoginRequiredMixin, generic.DeleteView):
    model = estadia
    success_url = reverse_lazy("filomenas:listar_filo")
    success_message = "Estadia removida com sucesso!"
    template_name = "filomenas/apagar.html" 
    
# CRUD de perfil do hospede 

class Detalharhospede(generic.DetailView):
    model = hospede
    template_name = "perfil/form_hospede.html"

class Criarhospede(LoginRequiredMixin, views.SuccessMessageMixin, generic.CreateView):
    model = hospede
    form_class = HospedeForm
    template_name = 'perfil/form_hospede.html'
    success_url = reverse_lazy("filomenas:home")
    success_message = "Hospede cadastrado com sucesso!"

class Atualizarhospede(LoginRequiredMixin, views.SuccessMessageMixin, generic.UpdateView):
    model = hospede
    form_class = HospedeForm
    template_name = "perfil/form_hospede.html"
    success_url = reverse_lazy("filomenas:perfil")
    success_message = "Perfil atualizado com sucesso"

class Apagarhospede(LoginRequiredMixin, generic.DeleteView):
    model = hospede
    success_url = reverse_lazy("filomenas:home")
    
# CRUD de perfil filomenas

class Detalharfilomena(generic.DetailView):
    model = filomenas
    template_name = 'filomenas/detalhar_filo.html'

class Listarfilomena(LoginRequiredMixin, generic.ListView):
    model = filomenas
    context_object_name = 'filomenas'
    paginate_by = 5

class Criarfilomena(AdministradorPermission, LoginRequiredMixin, views.SuccessMessageMixin, generic.CreateView):
    model = filomenas
    form_class = FilomenasForm
    template_name = 'filomenas/form.html'
    success_url = reverse_lazy("filomenas:home")
    success_message = "filomena cadastrada com sucesso!"

class Atualizarfilomena(LoginRequiredMixin, views.SuccessMessageMixin, generic.UpdateView):
    model = filomenas
    form_class = FilomenasForm
    success_url = reverse_lazy("filomenas:home")
    success_message = "Perfil atualizado com sucesso, {{ request.user.username }}!" 

class Apagarfilomena(LoginRequiredMixin, generic.DeleteView):
    template_name = "reservas/apagar.html"
    success_message = "Filomena removida com sucesso!"
    model = filomenas
    success_url = reverse_lazy("filomenas:home")
