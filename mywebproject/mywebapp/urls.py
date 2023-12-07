from django.urls import path
from .views import index, categoria_form, producto_form, cliente_form, search_productos

urlpatterns = [
    path('', index, name='index'),
    path('categoria_form/', categoria_form, name='categoria_form'),
    path('producto_form/', producto_form, name='producto_form'),
    path('cliente_form/', cliente_form, name='cliente_form'),
    path('search_productos/', search_productos, name='search_productos'),
]
