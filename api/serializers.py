from rest_framework import serializers
from datetime import date
from .models import Autor, Categoria, Livro


class AutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Autor
        fields = '__all__'


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'


class LivroSerializer(serializers.ModelSerializer):
    # NESTED: leitura
    autor = AutorSerializer(read_only=True)
    categoria = CategoriaSerializer(read_only=True)

    # PK para escrita
    autor_id = serializers.PrimaryKeyRelatedField(
        write_only=True,
        source='autor',
        queryset=Autor.objects.all()
    )
    categoria_id = serializers.PrimaryKeyRelatedField(
        write_only=True,
        source='categoria',
        queryset=Categoria.objects.all()
    )

    class Meta:
        model = Livro
        fields = [
            'id',
            'titulo',
            'ano_publicacao',
            'preco',
            'estoque',
            'disponivel',
            'autor',
            'autor_id',
            'categoria',
            'categoria_id'
        ]
        read_only_fields = ['id']

    # -------- VALIDAÇÕES -------- #

    def validate_preco(self, value):
        if value < 0:
            raise serializers.ValidationError('O preço não pode ser negativo.')
        return value

    def validate_estoque(self, value):
        if value < 0:
            raise serializers.ValidationError('O estoque não pode ser negativo.')
        return value

    def validate_ano_publicacao(self, value):
        atual = date.today().year
        if not (1900 <= value <= atual):
            raise serializers.ValidationError(
                f'O ano_publicacao deve estar entre 1900 e {atual}.'
            )
        return value

    def validate(self, data):
        # validação cruzada opcional
        estoque = data.get('estoque', getattr(self.instance, 'estoque', None))
        disponivel = data.get('disponivel', getattr(self.instance, 'disponivel', None))

        if estoque == 0 and disponivel is True:
            raise serializers.ValidationError(
                'Um livro com estoque 0 não pode estar marcado como disponível.'
            )
        return data
