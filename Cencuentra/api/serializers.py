# -*- encoding:utf-8 -*-
from rest_framework import serializers
from users.models import *
from negocios.models import *
from promos.models import *

#Default Serializers
#user
class DefaultUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'is_admin']

class DefaultNegocioSerializer(serializers.ModelSerializer):
	
	user = DefaultUserSerializer(many=False, read_only=True)
	user_id = serializers.PrimaryKeyRelatedField(write_only=True, queryset=User.objects.all(), source='user')
	
	class Meta:
		model = Negocio
		fields = ['id', 'name', 'phone_number', 'opening','closing','lat','lon', 'user','user_id']
    
class DefaultPromoSerializer(serializers.ModelSerializer):

	negocio = DefaultNegocioSerializer(many=False, read_only=True)
	negocio_id = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Negocio.objects.all(), source='promo')
	
	class Meta:
		model = Promo
		fields = ['id', 'name', 'article', 'discountP','discountC','negocio','negocio_id']


#Registro Usuario
class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'is_admin']
        write_only_fields = ['password']

    def create(self, validate_data):
        my_user = User.objects.create(
            username = validate_data['username'],
            email = validate_data['email'],
            is_admin = validate_data['is_admin']
        )
        my_user.set_password(validate_data['password'])
        my_user.save()
        return my_user


#User Serializer
class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username', 'email','is_admin']
        read_only_fields = ['id']

class NegocioSerializer(serializers.ModelSerializer):
	
	user = DefaultUserSerializer(many=False, read_only=True)
	class Meta:
		model = Negocio
		fields = ['id', 'name', 'phone_number', 'opening','closing','lat','lon','user']


class PromoSerializer(serializers.ModelSerializer):

	negocio = DefaultNegocioSerializer(many=False, read_only=True)

	class Meta:
		model = Promo
		fields = ['id', 'name', 'article', 'discountP','discountC','negocio']

