from django.urls import path
from .views import LivrosListView

urlpatterns = [
    path('livros/', LivrosListView.as_view()),
]
