# bullriding_25
New Solution vor Swiss Bullriding Championship 2025

## Datenbank löschen und neue Migration

Windows
``` Window
Get-ChildItem -Path . -Recurse -Include "migrations" | Remove-Item -Recurse -Force
```
Linux
``` Linux
find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
find . -path "*/migrations/*.pyc" -delete
```

## Neuaufbau der Datenbank

```Code
python manage.py makemigrations
python manage.py migrate
```

## Erstellen Admin User

```Code
python manage.py createsuperuser
```
