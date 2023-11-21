from django.db import models
from django.contrib.auth.models import AbstractUser

class Person(AbstractUser):
    # Nuevos campos adicionales
    cuil = models.CharField(max_length=20, null=True, blank=True)

    # Solución para evitar conflictos con los campos heredados
    groups = None  # Asignación de None a los campos que causan conflicto
    user_permissions = None

    class Meta:
        db_table = "Users"
