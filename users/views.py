import os

from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

from .forms import CustomUserCreationForm
from .forms import ProfileUpdateForm

def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Benutzer nach Registrierung automatisch anmelden
            return redirect('home')  # Umleitung zur Startseite (später anpassen)
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):
    """Profil anzeigen & bearbeiten"""
    user = request.user

    if request.method == "POST":
        form = ProfileUpdateForm(request.POST, request.FILES, instance=user)  # request.FILES sicherstellen!
        if form.is_valid():
            form.save()  # Speichert sowohl das Bild als auch die restlichen Formulardaten
            return redirect("profile")
    else:
        form = ProfileUpdateForm(instance=user)

    return render(request, "users/profile.html", {"form": form})

@login_required
def delete_profile_picture(request):
    """Löscht das Profilbild des angemeldeten Benutzers und setzt ein Platzhalterbild"""
    user = request.user
    if user.profile_picture:
        # Lösche die Datei vom Server
        file_path = os.path.join(settings.MEDIA_ROOT, str(user.profile_picture))
        if os.path.exists(file_path):
            os.remove(file_path)
        
        # Setze das Profilbild auf None (damit der Platzhalter angezeigt wird)
        user.profile_picture = None
        user.save()
    
    return redirect('profile')

