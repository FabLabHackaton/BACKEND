# -*- encoding: utf-8 -*-
from rest_framework import generics, status, filters, permissions
from .serializers import *

#MyUser Views
class UserView(generics.ListAPIView):

    queryset = User.objects.all()
    serializer_class = DefaultUserSerializer


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):

    queryset = User.objects.all()
    serializer_class = UserSerializer


#User views
class UserRegisterView(generics.CreateAPIView):

    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer
    permission_classes = [permissions.AllowAny]


# class NegocioRegisterView(generics.CreateAPIView):

#     queryset = Negocio.objects.all()
#     serializer_class = UserRegisterSerializer
#     permission_classes = [permissions.AllowAny]


# class NegocioView(generics.ListAPIView):

#     queryset = User.objects.all()
#     serializer_class = DefaultUserSerializer


class NegocioView(generics.ListCreateAPIView):

	queryset = Negocio.objects.all()
	serializer_class = DefaultNegocioSerializer


class NegocioDetailView(generics.RetrieveUpdateDestroyAPIView):

	queryset = Negocio.objects.all()
	serializer_class = NegocioSerializer



