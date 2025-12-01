from django.urls import path
from django.http import JsonResponse
from .views import (
    AutorListCreateView, AutorDetailView,
    CategoriaListCreateView, CategoriaDetailView,
    LivroListCreateView, LivroDetailView
)

def api_root(request):
    return JsonResponse({
        "message": "API online!",
        "endpoints": {
            "autores": "/api/autores/",
            "categorias": "/api/categorias/",
            "livros": "/api/livros/"
        }
    })


urlpatterns = [
    path('', api_root),

    # AUTOR
    path('autores/', AutorListCreateView.as_view()),
    path('autores/<int:pk>/', AutorDetailView.as_view()),

    # CATEGORIA
    path('categorias/', CategoriaListCreateView.as_view()),
    path('categorias/<int:pk>/', CategoriaDetailView.as_view()),

    # LIVROS
    path('livros/', LivroListCreateView.as_view()),
    path('livros/<int:pk>/', LivroDetailView.as_view()),
]
