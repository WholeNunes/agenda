from django.db import models
from django.utils import timezone

# Create your models here.
"""
CONTATOS
nome: STR * (obrigatÃ³rio)
sobrenome: STR (opcional)
telefone: STR * (obrigatÃ³rio)
email: STR (opcional)
data_criacao: DATETIME (automÃ¡tico)
descricao: texto
categoria: CATEGORIA (outro model)

 CATEGORIA
 nome: STR * (obrigatÃ³rio)
"""
#Herança models
#blank=true --> opcional

class Categoria(models.Model):
    nome = models.CharField(max_length=255)

    def __str__(self):
        return self.nome

class Contato(models.Model):
    nome = models.CharField(max_length=255)
    sobrenome = models.CharField(max_length=255, blank=True)
    telefone = models.CharField(max_length=255)
    email = models.CharField(max_length=255, blank=True)
    data_criacao = models.DateTimeField(default=timezone.now)
    descricao = models.TextField(blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)
    mostrar = models.BooleanField(default=True)
    foto = models.ImageField(blank=True, upload_to='fotos/%Y/%m')

    def __str__(self):
        return self.nome
