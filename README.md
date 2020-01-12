#  Django Project

understanding django framework

## Prerequisites
```
Django 1.11.27
```

```
Python 2.7.15+
```
```
Linux(Ubuntu)
```
## Installing
Create Virtual environment

* **install virtual environment**
```$ sudo apt install virtualenv```
* **install python 2.7**
```$ virtualenv env -p python2```
* **activate virtual environment**
```$ source bin/activate```
* **to see what modules you have installed**
```$ pip freeze```
* **install django**
```$ pip install Django==1.11.27```
* *to deactivate virtual environment*
```$ deactivate```

Install git 

* **Installing git on ubuntu**
```$ sudo apt install git```

Runnning project

```$ cd env ```

```$ git clone https://github.com/Mayur290/django-definitive-guide.git```

```$ cd django-definitive-guide```

```$ python manage.py migrate```

```$ python manage.py makemigrations```

```$ python manage.py runserver```

## urls available

*shows homepage*
```http://127.0.0.1:8000/```

*HttpResponse of hello world*
```http://127.0.0.1:8000/hello```

*simple python current time*
```http://127.0.0.1:8000/Time```

*shows 2 digits future time you want to know*
```http://127.0.0.1:8000/time_ahead/(\d{1,2})/```

*shows current time with django filters*
```http://127.0.0.1:8000/curr```

*book search form*
```http://127.0.0.1:8000/search-form```

```http://127.0.0.1:8000/```

## Credits

> **The Definitive Guide to Django: Web Development Done Right**
> 
> *by Adrian Holovaty (Author), Jacob Kaplan-Moss (Author)* 

*[Buy Book](https://www.amazon.com/Definitive-Guide-Django-Development-Right-ebook/dp/B004VJ46OM/ref=sr_1_1?keywords=the+definitive+guide+to+django&qid=1578764944&sr=8-1)*


