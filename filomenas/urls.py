from django.urls import path
from . import views

app_name = "filomenas"

urlpatterns = [
    # nao logado
    path('', views.Home.as_view(), name='home'),
    path('filo/', views.filomena_nao.as_view(), name="filomena_nao"),

    # logado
    path('home2/', views.Home2.as_view(), name='home2'),    
    path('perfil/', views.Perfil.as_view(), name="perfil"),
    path('fil/', views.filomena_logado.as_view(), name="filomena_logado"),
    
    #listar
    path('listar/', views.ListarEstadia.as_view(), name="listar_log"),
    path('listarfilo/', views.ListarEstadiafilo.as_view(), name="listar_filo"),
    path('listar_nao/', views.ListarEstadianao.as_view(), name="listar_nao"),

    #detalhar
    path('detalhar_log/<int:pk>/', views.Detalharestadialog.as_view(), name="detalhar_log"),
    path('detalhar/<int:pk>/', views.DetalharEstadia.as_view(), name="detalhar"),

    #criar
    path('criar/', views.CriarEstadia.as_view(), name="criar"),
    path('criar_hospede/', views.Criarhospede.as_view(), name="criar_hospede"),
    path('criar_filomena/', views.Criarfilomena.as_view(), name="criar_filomena"),
    path('forms/', views.forms.as_view(), name="forms"),
 
    #apagar
    path('apagar/<int:pk>/', views.Apagarfilomena.as_view(), name='apagar'),
    path('apagarestadia/<int:pk>/', views.ApagarEstadia.as_view(), name='apagarestadia'),

    #atualizar
    path('atualizar/<int:pk>/', views.AtualizarEstadia.as_view(), name="atua"),
    path('atualizar_hosp/<int:pk>/', views.Atualizarhospede.as_view(), name="atuar_hospede"),
]