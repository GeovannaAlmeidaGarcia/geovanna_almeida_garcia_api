from django.urls import path
from .views import LivrosListView
from django.http import JsonResponse

def api_root(request):
    return JsonResponse({
        "message": "API online!",
        "endpoints": {
            "livros": "/api/livros/"
        }
    })

urlpatterns = [
    path('', api_root),                 # ← agora /api/ funciona
    path('livros/', LivrosListView.as_view()),
]
