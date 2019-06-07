# Let Us Dance
###### Django

Install postman, django, python 3.7.2, pip, pipenv

Create a folder for the whole environment -> cd/
Load the subshell # pipenv shell

Install the environment:
```
pipenv install django djangorestframework django-rest-knox
pipenv install django
pipenv install djangorestframework
pipenv install django-rest-knox
```

Create a project folder and initialize the project
```
django-admin startproject projectname
python manage.py startapp appname
```
- add rest_framework, appname to INSTALLED_APPS
- configure SQL or db connection

## Models.py and Migrations

from django.db import models
```
class Lead(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    message = models.CharField(max_length=500, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
```

Create and run the migration from the created model
```
python manage.py makemigrations leads
python manage.py migrate
```

## Serializers (converts to JSON)
in the app folder, create a serializer.py
```
from rest_framework import serializers
from dances.models import Dance

# Dance serializer
class DanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dance
        fields = '__all__'
```

## API (Viewsets and permissions)
allows us to CRUD without having explicit instructions
```
from dances.models import Dance
from rest_framework import viewsets, permissions
from .serializers import DanceSerializer

# Dance Viewset
class DanceViewSet(viewsets.ModelViewSet):
    queryset = Dance.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = DanceSerializer
```

## urls.py in mainfoldername
```
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', include('dances.urls'))
]
```

## urls.py in appfoldername
```
from rest_framework import routers
from .api import DanceViewSet

router = routers.DefaultRouter()
router.register('api/dances', DanceViewSet, 'dances')

urlpatterns = router.urls
```

## Test it in postman
GET request
http://localhost---/*

POST request
-> Headers -> Content-Type -> Application->json
http://localhost---/api/NameOfApi/
Input all
```
{
    "example_field_name": "example content",
    "example_field_name": "example content",
}
```