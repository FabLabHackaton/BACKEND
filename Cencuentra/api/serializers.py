# -*- encoding:utf-8 -*-
from rest_framework import serializers
from users.models import *

#Default Serializers
#user
class DefaultUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'is_admin']


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

