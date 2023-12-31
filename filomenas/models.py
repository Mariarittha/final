from django.db import models
from operator import mod
from django.db import models

class Produtos(models.Model):
    nome = models.CharField(max_length=120)
    preco = models.FloatField()
    imagem = models.ImageField()
    descricao_produto = models.CharField(max_length=1000)

class hospede(models.Model):
    nome = models.CharField(max_length=120)
    profissao = models.CharField(max_length=120)
    email = models.EmailField(null=True)
    idade = models.IntegerField()
    imagem_perfil = models.ImageField(null=True)
    telefone = models.CharField(max_length=20, null=True)
    formulario_enviado = models.BooleanField(default=False)

class filomenas(models.Model):
    nome = models.CharField(max_length=120)
    idade = models.IntegerField()
    descricao = models.CharField(max_length=1000)
    imagem_filo = models.ImageField(null=True)
    email = models.EmailField(null=True)
    telefone = models.CharField(max_length=20, null=True)

class estadia(models.Model):
    imagem = models.ImageField(null=True)
    duracao = models.IntegerField()
    nome_estadia = models.CharField(max_length=200)
    descricao_estadia = models.CharField(max_length=1000)
    localizacao = models.CharField(max_length=500)
    valor = models.DecimalField(verbose_name=("valor"), decimal_places=2, max_digits=6)    
    programacao = models.CharField(max_length=1000, null=True)
