from rest_framework import serializers  # Import the serializers module from Django REST Framework
from product.models import Category  # Import the Category model from the product app

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category  # Define that this serializer is for the Category model
        fields = [
            "id",  # Category ID field
            "name",  # Category name field
            "description",  # Category description field
            "slug",  # Category slug field
            "active",  # Category active field (whether the category is active or not)
        ]

    def validate_name(self, value):
        """
        Validates if the category name has at least 3 characters.
        """
        if len(value) < 3:  # Check if the length of the name is less than 3 characters
            raise serializers.ValidationError("The name must have at least 3 characters.")  # Raise a validation error if the condition is met
        return value  # Return the validated name
