from django.contrib import admin
from .models import Autor, Categoria, Livro

@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'email', 'nacionalidade')
    search_fields = ('nome',)

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome',)
    search_fields = ('nome',)

@admin.register(Livro)
class LivroAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'autor', 'categoria', 'estoque', 'preco', 'disponivel')
    list_filter = ('categoria', 'disponivel')
    search_fields = ('titulo', 'autor__nome')
