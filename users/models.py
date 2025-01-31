import os
import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser

def user_profile_picture_path(instance, filename):
    """Erstellt einen eindeutigen Dateipfad für das Profilbild."""
    ext = filename.split('.')[-1]  # Dateiendung extrahieren
    new_filename = f"{uuid.uuid4()}.{ext}"  # UUID als Dateiname
    return os.path.join('profile_pics/', new_filename)  # Speichert unter 'profile_pics/'

class CustomUser(AbstractUser):
    """Erweitertes Benutzer-Modell mit Profilbild & Bio"""
    profile_picture = models.ImageField(upload_to=user_profile_picture_path, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.username
