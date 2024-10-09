from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    full_name = models.CharField(max_length=150)  # Campo para el nombre completo
    email = models.EmailField(unique=True)
    
    # Se hereda username y password de AbstractUser, entre otros campos
