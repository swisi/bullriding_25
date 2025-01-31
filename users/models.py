import os
import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser

def profile_picture_path(instance, filename):
    """Generiert einen eindeutigen Dateipfad für Profilbilder mit einer UUID"""
    ext = filename.split('.')[-1]  # Dateiendung extrahieren
    filename = f"{uuid.uuid4()}.{ext}"  # UUID als Dateiname
    return os.path.join("profile_pics/", filename)  # Datei speichern in "profile_pics/"

class CustomUser(AbstractUser):
    """Erweitertes Benutzer-Modell mit GUID für Profilbilder"""
    email = models.EmailField(unique=True)
    profile_picture = models.ImageField(upload_to=profile_picture_path, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True, verbose_name="Adresse")
    zip_code = models.CharField(max_length=10, blank=True, null=True, verbose_name="Postleitzahl")
    city = models.CharField(max_length=100, blank=True, null=True, verbose_name="Ort")
    mobile = models.CharField(max_length=20, blank=True, null=True, verbose_name="Mobiltelefon")

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.username})"
