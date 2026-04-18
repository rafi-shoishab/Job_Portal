# Job Portal 
## 🏗 Project Structure Overview
```   
Job_portal/
│
├── Job_portal/            # Project settings & root routing
│   ├── settings.py        # Django project settings
│   ├── urls.py            # Project URL routing
│   ├── asgi.py
│   └── wsgi.py
│
├── Jobs/                  # Django Job App: Logic & Models
│   ├── models.py          # Job model data schema
│   ├── views.py           # CRUD logic
│   ├── urls.py            # App URLs
│   ├── forms.py           # Job forms Input handling
│   └── migrations/        # Database history
├── accounts/              # Django Accounts App: Logic & Models
│   ├── models.py          # Accounts model data schema
│   ├── views.py           # CRUD logic
│   ├── urls.py            # App URLs
│   ├── forms.py           # Job forms Input handling
│   └── migrations/        # Database history
│
├── templates/             # HTML templates
│    ├── Jobs
│    │      ├── index.html
│    │      ├── job_create.html
│    │      ├── job_update.html
│    │      └── job_list.html
│    │
│    ├── accounts
│    │      ├── index.html
│    │      ├── job_create.html
│    │      ├── job_update.html
│    │      └── job_list.html
│    │
│    └── applications
│           ├── index.html
│           ├── job_create.html
│           ├── job_update.html
│           └── job_list.html
│
├── static/                # CSS / JS / Images files 
│
├── manage.py              # Django CLI
└── requirements.txt       # Dependencies
```
## 1. set up Django
### 1.0 Clone Repository
```
git clone https://github.com/rafi-shoishab/django-job_portal.git
cd django-job_portal
```
### 1.1 Create Virtual Environment

Mac/Linux
```
python3 -m venv .venv
source .venv/bin/activate
```
Windows
```
python -m venv .venv
.venv\Scripts\activate
```
### 1.2 Install Dependencies
```
pip install -r requirements.txt
pip install django
pip install pillow
```
### Step 1.3 — Create Django Project

```
django-admin startproject Name_ID_JobPortal 
```

### Step 1.4 — Create Django App

```
python manage.py startapp acounts
```

### Step 1.5 — Register App in Project settings.py

File: `Name_ID_JobPortal/settings.py`

Add the app inside `INSTALLED_APPS`:

```python
INSTALLED_APPS = [
    ...
    'accounts',
]
```

### Step 1.6 — Configure Template Directory in project settings.py

File: `Name_ID_JobPortal/settings.py`

Update the `TEMPLATES` section:

```python
TEMPLATES = [
{
...
'DIRS': [ (BASE_DIR / 'templates')],
... 
}
]
```

### Step 1.7 — Create App URL Configuration

Create file: `accounts/urls.py`

```python
from django.urls import path
from . import views

urlpatterns = [
    path(' ', views.home, name='home'),
]
```

### Step 1.8 — Connect App URLs to Project URLs

File: `Name_ID_JobPortal/urls.py`
```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),
]
```

### Step 1.9 — Create View in app

File: `accounts/views.py`

```python
from django.http import HttpResponse

def hello(request):
    return HttpResponse("Hello Django")
```
### Step 1.10 — Create HTML Template

File: `templates/accounts/index.html`

```html
<!DOCTYPE html>
<html>
<head>
    <title>Django Home</title>
</head>
<body>
    <h1>Hello Django Template 🎉</h1>
</body>
</html>
```

### Step 1.11 — Create View to Render Template

File: `accounts/views.py`

```python
from django.shortcuts import render

def home(request):
    return render(request, "accounts/index.html")
```


## ⚡ 1. Setup Django (Run Project)
Clone Repository
```
git clone https://github.com/rafi-shoishab/django-crud-job_portal.git
cd django-crud-job_portal
```
Create Virtual Environment
Mac / Linux
```
python3 -m venv .venv
source .venv/bin/activate
```
Windows
```
python -m venv .venv
.venv\Scripts\activate
```
Install Dependencies
```
pip install -r requirements.txt
```
Apply Migrations
```
python manage.py migrate
```
Run Development Server
```
python manage.py runserver
```
Open Browser
```
http://127.0.0.1:8000
```

## 🧩 2. Creating Job Model

Models represent database tables in Django.

📄 job_portal/models.py
```
from django.db import models

class Job(models.Model):
    title = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    salary = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return self.title
```

## 🛠 3. Register Model in Admin Panel

📄 job_portal/admin.py
```
from django.contrib import admin
from .models import Job

admin.site.register(Job)
```
Now jobs can be managed from the Django admin panel.

## 🌐 4. URL Routing

### App URLs

📄 job_portal/urls.py
```
from django.urls import path
from . import views

urlpatterns = [
    path('', views.job_list, name='job_list'),
    path('create/', views.job_create, name='job_create'),
    path('update/<int:id>/', views.job_update, name='job_update'),
    path('delete/<int:id>/', views.job_delete, name='job_delete'),
]
```

### Project URLs

📄 core/urls.py
```
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('job_portal.urls')),
]
```

## 📄 5. CRUD Views Implementation

📄 job_portal/views.py

### all_job 
```
from django.shortcuts import render, redirect
from .models import Job

def job_list(request):
    jobs = Job.objects.all()
    return render(request, 'job_list.html', {'jobs': jobs})
```
### add_job
```
def job_create(request):
    if request.method == "POST":
        title = request.POST.get('title')
        company = request.POST.get('company')
        location = request.POST.get('location')
        salary = request.POST.get('salary')
        description = request.POST.get('description')

        Job.objects.create(
            title=title,
            company=company,
            location=location,
            salary=salary,
            description=description
        )

        return redirect('job_list')

    return render(request, 'job_create.html')
```
### edit job
```
def job_update(request, id):
    job = Job.objects.get(id=id)

    if request.method == "POST":
        job.title = request.POST.get('title')
        job.company = request.POST.get('company')
        job.location = request.POST.get('location')
        job.salary = request.POST.get('salary')
        job.description = request.POST.get('description')
        job.save()

        return redirect('job_list')

    return render(request, 'job_update.html', {'job': job})
```
### delete job 
```
def job_delete(request, id):
    job = Job.objects.get(id=id)
    job.delete()
    return redirect('job_list') 
```
## 🎨 6. Template Example

📄 templates/job_list.html
```
<h1>Job Listings</h1>

<a href="{% url 'job_create' %}">
    Add New Job
</a>

<ul>
{% for job in jobs %}
    <li>
        {{ job.title }} - {{ job.company }}

        <a href="{% url 'job_update' job.id %}">Edit</a>

        <a href="{% url 'job_delete' job.id %}">Delete</a>
    </li>
{% endfor %}
</ul>
```

## 🔁 Django CRUD Workflow
```
User Request
     ↓
urls.py
     ↓
views.py
     ↓
Database (Model)
     ↓
Template Rendering
     ↓
HTTP Response
```
## 🛠 Django Admin Panel

Apply Migrations
```
python manage.py migrate
```
Create Superuser
```
python manage.py createsuperuser
```
Login Admin Panel
```
http://127.0.0.1:8000/admin/
```
## 🔧 Git Workflow (Quick Guide)
First Time
```
git add .

git commit -m "initial commit"

git push -u origin main
```
Daily Workflow
```
git pull

git add .

git commit -m "update message"

git push
```
📄 Recommended .gitignore
```
.venv/

venv/

__pycache__/

*.pyc

db.sqlite3

.DS_Store
.vscode/
media/
```

## 👨‍💻 Author

Rafiur Rahman Shoishab

## GitHub:
https://github.com/rafi-shoishab

## 📜 License

This project is created for educational purposes to demonstrate CRUD operations in Django.
