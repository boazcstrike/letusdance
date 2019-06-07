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

# 2nd part React Frontend
python manage.py startapp frontend
mkdir -p ./frontend/src/components
mkdir -p ./frontend/{static,templates}/frontend

add frontend to INSTALLED_APPS

root directory
```
npm init -y
npm i -D webpack webpack-cli
npm i -D @babel/core babel-loader @babel/preset-env @babel/preset-react babel-plugin-transform-class-properties
npm i react react-dom prop-types
```

## create .babelrc
```
{
    "presets": ["@babel/preset-env","@babel/preset-react"],
    "plugins": ["transform-class-properties"]
}
```

## create webpack.config.js
```
module.exports = {
    module: {
        rules:[
            {
                test: /\.js$/,
                exclude: /node_modules/,
                use: {
                    loader: "babel-loader"
                }
            }
        ]
    }
}
```

## add to package.json
```
    "scripts": {
        "dev": "webpack --mode development ./letusdance/frontend/src/index.js --output ./letusdance/frontend/static/frontend/main.js",
        "build": "webpack --mode production ./letusdance/frontend/src/index.js --output ./letusdance/frontend/static/frontend/main.js",
        "watch": "webpack --mode development --watch ./letusdance/frontend/src/index.js --output ./letusdance/frontend/static/frontend/main.js"
    },
```

create frontend > src > index.js
```
import App from './components/App'
```

create frontend > src > components > App.js
```
import React, {Component} from 'react'
import ReactDOM from 'react-dom'

class App extends Component {
    reder(){
        return <h1>Hi I'm alive.</h1>
    }
}

ReactDOM.render(<App />, document.getElementById('app'))
```

## create frontend > templates > frontend > index.html
```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>React App</title>
</head>
<body>
    <div id="app"></div>
    {% load static %}
    <script src="{% static "frontend/main.js" %}"></script>
</body>
</html>
```

## frontend > views.py
```
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'frontend/index.html')
```

## inside frontend > urls.py
```
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index)
]
```

## add in mainfolder > urls.py
    path('', include('frontend.urls')

## run and serve
```
npm run dev # or just run npm run watch to watch the files
python manage.py runserver # if you did not run this yet
```

from here the react app should work, if not, some things are left out, review again

React works, things should display from the App.js. Voila

# Happy Django React App! :D *** updated as of 6/7/2019