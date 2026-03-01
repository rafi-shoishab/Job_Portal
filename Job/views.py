from django.shortcuts import get_object_or_404, render, redirect 
from django.contrib import messages 
from .models import Job 

# Create your views here.

def home(request):
    
    return render(request, 'Jobs/index.html') 

def add_job(request):
    
    if request.method == "POST":
        title = request.POST.get('title')
        name = request.POST.get('company_name')
        logo = request.FILES.get('company_logo')
        address = request.POST.get('location')
        type = request.POST.get('type')
        opening = request.POST.get('openings')
        category = request.POST.get('category')
        job_details = request.POST.get('description')
        skill = request.POST.get('skill')
        package = request.POST.get('salary')
        submit = request.POST.get('deadline')
        
        Job.objects.create (
            job_title = title,
            company_name = name,
            company_logo = logo,
            job_location = address,
            job_type = type,
            vacancy = opening,
            category = category,
            job_description = job_details,
            skills = skill,
            salary = package,
            deadline = submit
        ) 
        
        messages.success(request, 'Job added succesfully!')
        
        return redirect(all_job)


    return render(request, 'Jobs/add_job.html')

def all_job(request):
    
    all_jobs = Job.objects.all()
    
    context = {
        'jobs': all_jobs
    }
    
    return render(request, 'Jobs/all_job.html', context) 

def browse_job(request):
    
    return render(request, 'Jobs/browse_job.html')

def single_job_view(request):
    
    return render(request, 'Jobs/single_job_view.html')

def edit_job(request):
    
    return render(request, 'Jobs/edit_job.html')

def delete_job(request):
    
    return render(request, 'Jobs/edit_job.html')

def about_us(request):
    
    return render(request, 'Jobs/about_us.html')