from django.db import models
from negocios.models import *
# Create your models here.
class Promo(models.Model):
	class Meta:
		verbose_name='Promo'
		verbose_name_plural='Promos'

	#Relations
	negocio = models.ForeignKey(
			Negocio,
			blank=False,
			null=True
		)
	#Fields
	name = models.CharField(
			'nombre',
			max_length=250,
			blank=False
		)

	article = models.URLField(
			'articulo',
			blank=False,
		)

	discountP = models.IntegerField(
			'descuento porcentaje',
			blank=True
		)

	discountC = models.IntegerField(
			'descuento cantidad',
			blank=True
		)