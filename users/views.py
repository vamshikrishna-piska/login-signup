from rest_framework import generics
from django.contrib.auth.models import User
from .serializers import RegisterSerializer
from rest_framework.permissions import AllowAny
from django.shortcuts import render

class RegisterView(generics.CreateAPIView):
    queryset=User.objects.all()
    permission_classes=[AllowAny]
    serializer_class=RegisterSerializer

def auth_page(request):
    return render(request,'auth.html')