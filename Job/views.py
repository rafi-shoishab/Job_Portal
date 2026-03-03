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
    
    context_dict = {
        'jobs': all_jobs 
    }
    
    return render(request, 'Jobs/all_job.html', context_dict) 

def browse_job(request):
    
    all_jobs = Job.objects.all()
    
<<<<<<< HEAD
    return render(request, 'Jobs/single_job_view.html')

def edit_job(request, job_id):
=======
    context_dict = {
        'jobs' : all_jobs
    }
    
    return render(request, 'Jobs/browse_job.html', context_dict)

def single_job_view(request, job_id):
    job_data = get_object_or_404(Job, id=job_id)
    
    context_dict = {
        'job' : job_data
    }
    
    return render(request, 'Jobs/single_job_view.html', context_dict)

def edit_job(request, job_id): 
    job_data = get_object_or_404(Job, id=job_id)
    
    if request.method == 'POST':
        job_data.job_title = request.POST.get('title')
        job_data.company_name = request.POST.get('company_name')
        job_data.company_logo = request.FILES.get('company_logo')
        job_data.job_location = request.POST.get('location')
        job_data.job_type = request.POST.get('type')
        job_data.vacancy = request.POST.get('openings')
        job_data.category = request.POST.get('category')
        job_data.job_description = request.POST.get('description')
        job_data.skills = request.POST.get('skill')
        job_data.salary = request.POST.get('salary')
        job_data.deadline = request.POST.get('deadline')
        
        job_data.save()
        
        return redirect('all_job')
        
    context = {
        'job' : job_data 
    }
    
    return render(request, 'Jobs/edit_job.html', context)
>>>>>>> 3b42806 (edit,brows,single done.)

    job_data = get_object_or_404(Job, id=job_id)

    if request.method =='POST':
        job_data.job_title = request.POST.get('title')
        job_data.company_name = request.POST.get('company_name')
        if request.FILES.get('company_logo'):
            job_data.company_logo = request.FILES.get('company_logo')
        job_data.job_location = request.POST.get('location')
        job_data.job_type = request.POST.get('type')
        job_data.vacancy = request.POST.get('openings')
        job_data.category = request.POST.get('category')
        job_data.job_description = request.POST.get('description')
        job_data.skills = request.POST.get('skill')
        job_data.salary = request.POST.get('salary')
        job_data.deadline = request.POST.get('deadline')
        
        job_data.save()

        return redirect('all_job')
    
    context_dict = {
        'job' : job_data
    }
    return render(request, 'Jobs/edit_job.html', context_dict)


def delete_job(request, job_id):

    job = Job.objects.filter(id=job_id)
    job.delete()
    return redirect('all_job')

def about_us(request):
    
    return render(request, 'Jobs/about_us.html')