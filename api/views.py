from rest_framework import generics
from .models import Autor, Categoria, Livro
from .serializers import AutorSerializer, CategoriaSerializer, LivroSerializer

# ----- AUTOR -----
class AutorListCreateView(generics.ListCreateAPIView):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer

class AutorDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer


# ----- CATEGORIA -----
class CategoriaListCreateView(generics.ListCreateAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class CategoriaDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer


# -------- LIVRO -------- #

class LivroListCreateView(generics.ListCreateAPIView):
    serializer_class = LivroSerializer

    def get_queryset(self):
        qs = Livro.objects.select_related("autor", "categoria").all()
        params = self.request.GET

        # filtro por categoria
        categoria = params.get("categoria")
        if categoria:
            qs = qs.filter(categoria_id=categoria)

        # filtro por autor
        autor = params.get("autor")
        if autor:
            qs = qs.filter(autor_id=autor)

        # filtro por disponibilidade
        disponivel = params.get("disponivel")
        if disponivel:
            d = disponivel.lower()
            if d in ["true", "1", "yes", "sim", "y"]:
                qs = qs.filter(disponivel=True)
            elif d in ["false", "0", "no", "nao", "n"]:
                qs = qs.filter(disponivel=False)

        return qs


class LivroDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Livro.objects.select_related("autor", "categoria").all()
    serializer_class = LivroSerializer
