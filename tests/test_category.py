import pytest
from rest_framework.test import APIClient
from django.urls import reverse
from product.models.category import Category

@pytest.mark.django_db
def test_create_category():
    """
    Test that a Category instance can be created successfully and has the expected attributes.
    """
    # Create a test category
    category = Category.objects.create(name="Electronics", slug="electronics")

    # Check that the attributes are set correctly
    assert category.name == "Electronics"
    assert category.slug == "electronics"
    assert category.active is True

@pytest.mark.django_db
def test_category_list():
    """
    Test that the list of categories can be retrieved and includes the correct number of items.
    """
    client = APIClient()
    url = reverse("category-list")  # Get the URL for the category list endpoint

    # Create test categories
    Category.objects.create(name="Electronics", slug="electronics")
    Category.objects.create(name="Books", slug="books")

    # Make a GET request to the category list endpoint
    response = client.get(url)

    # Check that the response status is 200 OK and the number of categories is correct
    assert response.status_code == 200
    assert len(response.data) == 4

@pytest.mark.django_db
def test_create_category_api():
    """
    Test that a new Category can be created via the API.
    """
    client = APIClient()
    url = reverse("category-list")  # Get the URL for the category list endpoint

    # Data for the new category
    data = {"name": "Clothing", "slug": "clothing"}

    # Make a POST request to create a new category
    response = client.post(url, data, format="json")

    # Check that the response status is 201 Created and the category is saved in the database
    assert response.status_code == 201
    assert Category.objects.count() == 1
    assert Category.objects.get(name="Clothing").slug == "clothing"
