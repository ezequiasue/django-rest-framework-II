from rest_framework import serializers
from product.models import Category  

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            "id",  # Certifique-se de que o campo id está incluído
            "name",
            "description",
            "slug",
            "active",
        ]

    def validate_name(self, value):
        """
        Verifica se o nome da categoria tem pelo menos 3 caracteres.
        """
        if len(value) < 3:
            raise serializers.ValidationError("O nome deve ter pelo menos 3 caracteres.")
        return value
