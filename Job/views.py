from django.shortcuts import get_object_or_404, render, redirect # db access
from django.contrib import messages # for message sweet alert
from .models import Job # model class 
from django.db.models import Q # for query 

# Create your views here.

def home(request):
    
    return render(request, 'Jobs/index.html') 

def add_job(request):
    
    if request.method == "POST":
        title = request.POST.get('title') # variable = request.POST.get('html name')
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
            job_title = title, # modelname = variable
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

    sort = request.GET.get('sort')

    if sort == 'asc':
        all_jobs = Job.objects.filter().order_by('job_title')
    
    elif sort =='desc':
        all_jobs = Job.objects.filter().order_by('-job_title')

    else:
        all_jobs = Job.objects.all()
    
    context_dict = {
        'jobs': all_jobs # dict = { 'key' : variable}
    }
    
    return render(request, 'Jobs/all_job.html', context_dict) 

def browse_job(request):

    query = request.GET.get('q')

    if query:
        all_jobs = Job.objects.filter( 
            Q(job_title__icontains = query) |
            Q(company_name__icontains = query)
        )

    else:
        all_jobs = Job.objects.all()
    
    context_dict = {
        'jobs' : all_jobs,
        'query' : query
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


def delete_job(request, job_id):

    job = Job.objects.filter(id=job_id)
    job.delete()
    return redirect('all_job')

def about_us(request):
    
    return render(request, 'Jobs/about_us.html')