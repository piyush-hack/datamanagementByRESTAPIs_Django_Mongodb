## GO TO MASTER BRANCH FOR FILES INCLUDING PROJECT
## Endpoints of API


Get all pizzas [Method : GET]
```bash
api/pizzas
```
Create pizza [Method : POST]
```bash
api/pizzas
```
Filter all pizzas [Method : GET]
```bash
api/pizzas?title="mytitle"&size="mysize"
```
Get all pizzas [Method : GET]
```bash
api/pizzas
```
Edit pizzas [Method : PUT]
```bash
api/pizzas/:id
```
Delete pizzas [Method : DELETE]
```bash
api/pizzas/:id
```
Delete all pizzas [Method : DELETE]
```bash
api/pizzas
```

## ...START PROJECT...

## Install Django REST framework


```python
pip install djangorestframework
```

Now open settings.py and add Django REST framework to the INSTALLED_APPS array here.

```python
INSTALLED_APPS = [
    ...
    # Django REST framework 
    'rest_framework',
]
```

## Connect Django project to MongoDB database



```python
pip install djongo
```

So open settings.py and change declaration of DATABASES:
```python
DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': 'pizza_db',
        'HOST': '127.0.0.1',
        'PORT': 27017,
    }
}
```

## Startapp 
```python
python manage.py startapp tutorials
```
Don’t forget to add this app to INSTALLED_APPS array in settings.py:
```python
INSTALLED_APPS = [
    ...
    # Tutorials application 
    'tutorials.apps.TutorialsConfig',
]
```

You also need to add a middleware class to listen in on responses:
```python
MIDDLEWARE = [
    ...
    # CORS
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
]
```
Next, set CORS_ORIGIN_ALLOW_ALL and add the host to CORS_ORIGIN_WHITELIST:
```python
CORS_ORIGIN_ALLOW_ALL = False
CORS_ORIGIN_WHITELIST = (
    'http://localhost:8081',
)
```

## Define the django model

```python
from django.db import models


class Tutorial(models.Model):
    title = models.CharField(max_length=70, blank=False, default='')
    size= models.CharField(max_length=200,blank=False, default='')
    toppings= models.CharField(max_length=200,blank=False, default='')
```
Don't Forget to migrate changes:

```python
python manage.py makemigrations

python manage.py migrate
```

## Create Serializer class for Data Model

```python
tutorials/serializers.py
```

## create urls.py of app as

```python
/api/tutorials: GET, POST, DELETE
/api/tutorials/:id: GET, PUT, DELETE
/api/tutorials/published: GET
```

also add urls.py in main directory
```python
DjangoRestApiMongoDB/urls.py
```

## Create views.py for urls.py

```python
tutorials/views.py
```

## Start mongodb in shell
```python
>>mongod
```

### Start main server
```python
python manage.py runserver 8080
```

## For proper access Create home template

```python
DjangoRestApiMongoDB/tutorials/templates/tutorials/tutorials.html
```

Add as template in settings.py
```python
...
    'DIRS': ["templates"],
...
```




## NOW YOU ARE ALL DONE.
