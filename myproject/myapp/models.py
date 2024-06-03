from django.db import models

# Create your models here.
class Barbero(models.Model):
    name = models.CharField(max_length=60)
    phone = models.IntegerField()
    email = models.CharField(max_length=60)
    services = models.CharField(max_length=10)
    photo = models.CharField(max_length=60)

    def __str__(self):
        return f"{self.name} {self.phone} {self.email} {self.services}"
    

class Cliente(models.Model):
    name = models.CharField(max_length=60)
    email = models.CharField(max_length=60)
    password = models.CharField(max_length=60)

    def __str__(self):
        return f"{self.name} {self.email}"
    

class Reserva(models.Model):
    name = models.CharField(max_length=60)
    email = models.CharField(max_length=60)
    namebar = models.CharField(max_length=60)
    services = models.CharField(max_length=10)
    date = models.DateField()
    time = models.DateTimeField()
    photo = models.CharField(max_length=60)

    def __str__(self):
        return f"{self.name} {self.email} {self.namebar}"