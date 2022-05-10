from django.contrib import admin
from .models import Categoria, Contato

#Colocando os campos para mostrar no site
class ContatoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'sobrenome', 'telefone', 'email',
                    'data_criacao', 'categoria', 'mostrar')
#Adicionando link aos campos colocados acima
    list_display_links = ('id', 'nome', 'sobrenome')
#Adicionando filtragem por campo
   # list_filter = ('nome', 'sobrenome')
    list_per_page = 10
#Adicionando campo de pesquisa
    search_fields = ('nome', 'sobrenome')
    list_editable = ('telefone', 'mostrar')



admin.site.register(Categoria)
admin.site.register(Contato, ContatoAdmin)