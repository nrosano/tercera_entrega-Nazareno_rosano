from django import forms
from .models import Categoria, Producto, Cliente

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre']

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'categoria', 'precio']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Personaliza el queryset para mostrar nombres de categorías en lugar de IDs
        self.fields['categoria'].queryset = Categoria.objects.all()

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'email']


class ProductoSearchForm(forms.Form):
    categoria = forms.ModelChoiceField(queryset=Categoria.objects.all(),
                                       empty_label='Todas las Categorías', required=False, label='Categoría')

    def filter_productos(self, queryset):
        categoria = self.cleaned_data.get('categoria')

        if categoria:
            queryset = queryset.filter(categoria=categoria)

        return queryset