from django.db import models

class Autor(models.Model):
    nome = models.CharField(max_length=200)
    email = models.EmailField(null=True, blank=True)
    nacionalidade = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.nome


class Categoria(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Livro(models.Model):
    titulo = models.CharField(max_length=200)
    ano_publicacao = models.IntegerField()
    preco = models.DecimalField(max_digits=8, decimal_places=2)
    estoque = models.IntegerField()

    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)

    disponivel = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.titulo} ({self.autor.nome})"
