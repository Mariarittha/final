from django.contrib import admin

from django.contrib import admin
from .models import Produtos, hospede, filomenas, estadia

@admin.register(Produtos)
class ProdutosAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'imagem', 'descricao_produto')

@admin.register(hospede)
class HospedeAdmin(admin.ModelAdmin):
    list_display = ['nome', 'profissao', 'email', 'idade', 'telefone', 'formulario_enviado']
    search_fields = ['nome', 'profissao', 'email', 'telefone']
    list_filter = ['formulario_enviado']
    
@admin.register(filomenas)  
class FilomenasAdmin(admin.ModelAdmin):
    list_display = ('nome', 'idade', 'descricao', "imagem_filo", "telefone")

@admin.register(estadia)
class EstadiaAdmin(admin.ModelAdmin):
    list_display = ('duracao', 'nome_estadia', 'descricao_estadia', 'localizacao', 'valor', 'programacao', 'imagem')