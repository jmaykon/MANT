from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    ROLES = (
        ('admin', 'Admin'),
        ('tecnico', 'Técnico'),
        ('usuario', 'Usuario'),
    )
    role = models.CharField(max_length=10, choices=ROLES, default='usuario')

    def __str__(self):
        return f"{self.username} ({self.role})"
