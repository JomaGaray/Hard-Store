from django.forms import ModelForm
from .models import Producto,Categoria,ImagenProducto

class ProductoForm(ModelForm):

	class Meta:
		model = Producto
		fields = ('nombre','descripcion','precio','categoria')

class ImagenForm(ModelForm):

	class Meta:
		model = ImagenProducto
		fields = ('imagen',)

class CategoriaForm(ModelForm):

	class Meta:
		model = Categoria
		fields = ('nombre',)

