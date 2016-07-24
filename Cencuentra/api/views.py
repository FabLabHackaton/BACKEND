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
