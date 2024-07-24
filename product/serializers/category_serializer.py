from rest_framework import serializers
from product.models.category import Category  # Importa o modelo Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category  # Define que este serializer é para o modelo Category
        fields = [
            "id",  # Campo de ID da categoria
            "name",  # Campo de nome da categoria
            "description",  # Descrição da categoria
            "slug",  # Campo de slug da categoria
            "active",  # Campo ativo da categoria (se a categoria está ativa ou não)
        ]

    def validate_name(self, value):
        """
        Valida se o nome da categoria tem pelo menos 3 caracteres.
        """
        if len(value) < 3:  # Verifica se o comprimento do nome é menor que 3 caracteres
            raise serializers.ValidationError("O nome deve ter pelo menos 3 caracteres.")  # Levanta um erro de validação se a condição for atendida
        return value  # Retorna o nome validado
