from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=100)
    birth_date = models.DateField()
    cpf = models.CharField(max_length=14, unique=True)  # formato 000.000.000-00

    def __str__(self):
        return f"{self.name} - {self.cpf}"