from rest_framework import serializers
from .models import Barbero, Cliente, Reserva
from django.contrib.auth.models import User

class BarberoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Barbero
        fields = '__all__'
class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

class ReservaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reserva
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
