from rest_framework import viewsets
from django.contrib.auth.models import User
from .models import Barbero, Cliente, Reserva
from .serializers import BarberoSerializer, ClienteSerializer, ReservaSerializer, UserSerializer

# Create your views here.
class BarberoViewSet(viewsets.ModelViewSet):
    queryset = Barbero.objects.all()
    serializer_class = BarberoSerializer

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class ReservaViewSet(viewsets.ModelViewSet):
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

