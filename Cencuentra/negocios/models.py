from django.db import models
from django.core.validators import RegexValidator
# Create your models here.
class Negocio(models.Model):

	class Meta:
		verbose_name='Negocio'
		verbose_name_plural='Negocios'

	name = models.CharField(
		'nombre',
		max_length=255,
		blank=False
		)

	phone_regex = RegexValidator(
		regex=r'^\+?1?\d{10,15}$',
		message="El numero tiene que tener este formato '55-5555-5555'."
	)

	phone_number = models.CharField(
		validators=[phone_regex],
		blank=False,
		max_length=13,
	)

	opening = models.TimeField(
		'apertura',
		blank=False
	)
	closing = models.TimeField(
		'clausura',
		blank=False
	)
	lat = models.CharField(
		'latitud',
		max_length=500,
		blank=True
	)
	lon = models.CharField(
		'longitud',
		max_length=500,
		blank=True
	)