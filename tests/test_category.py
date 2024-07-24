import pytest
from rest_framework.test import APIClient
from django.urls import reverse
from product.models.category import Category


@pytest.mark.django_db
def test_create_category():
    # Cria uma categoria de teste
    category = Category.objects.create(name="Electronics", slug="electronics")

    # Verifica os atributos da categoria
    assert category.name == "Electronics"
    assert category.slug == "electronics"
    assert category.active is True


@pytest.mark.django_db
def test_category_list():
    client = APIClient()
    url = reverse("category-list")

    # Cria categorias de teste
    Category.objects.create(name="Electronics", slug="electronics")
    Category.objects.create(name="Books", slug="books")

    # Faz uma requisição GET para o endpoint da lista de categorias
    response = client.get(url)

    # Verifica a resposta
    assert response.status_code == 200
    assert len(response.data) == 4


@pytest.mark.django_db
def test_create_category_api():
    client = APIClient()
    url = reverse("category-list")

    # Dados para a nova categoria
    data = {"name": "Clothing", "slug": "clothing"}

    # Faz uma requisição POST para criar uma nova categoria
    response = client.post(url, data, format="json")

    # Verifica a resposta
    assert response.status_code == 201
    assert Category.objects.count() == 1
    assert Category.objects.get(name="Clothing").slug == "clothing"
