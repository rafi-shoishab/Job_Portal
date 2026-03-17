# import necessary modules 

from django.shortcuts import render, redirect, get_object_or_404
# render → use to render HTML template with context
# redirect → use to redirect user to another URL
# get_object_or_404 → to fetch a single object from database.

from .models import CustomUser, RecruiterProfile, JobseekerProfile 
#
from django.contrib.auth import authenticate, login, logout
#
from django.contrib import messages 
#
from Jobs.models import Job
#
from django.contrib.auth.decorators import login_required
#




# Create your views here.

def home(request):
    
    return render(request, 'accounts/index.html')
    # just render the homepage template
    # no context needed
    
def register(request):
    
    if request.method == 'POST':
        user_name = request.POST.get('username') # 
        fname = request.POST.get('first_name') 
        lname = request.POST.get('last_name') 
        mail = request.POST.get('email')
        role = request.POST.get('role') 
        pro_pic = request.FILES.get('profile_photo')
        pass_word = request.POST.get('password')
        confrim_password = request.POST.get('re_password')
        
        if pass_word != confrim_password:
            messages.error(request, 'password unmatched')
            return redirect ('register')
        
        if CustomUser.objects.filter(email = mail).exists():
            messages.error(request, 'email already exists')
            return redirect('register')
        
        if CustomUser.objects.filter(username = user_name).exists():
            messages.error(request, 'username not available')
            return redirect('register')
        
        user = CustomUser.objects.create_user(
            username = user_name, # 
            email = mail,
            password = pass_word,            
        )
        
        user.first_name = fname 
        user.last_name = lname
        user.role = role
        user.display_picture = pro_pic # 
        
        user.save() 
        
        if role == 'recruiter':
            RecruiterProfile.objects.create(user = user)
        elif role == 'job_seeker':
            JobseekerProfile.objects.create(user = user)
        
        messages.success(request, 'registered successfully') 
        return redirect ('login') 
        
    return render(request, 'accounts/register.html') 

def log_in(request):
    if request.method == 'POST':
        email_username = request.POST.get('email_username') #
        pass_word = request.POST.get('password') 
        
        # Try email first, then username
        try:
            user_input = CustomUser.objects.get(email = email_username) #
            user_name = user_input.username
        except CustomUser.DoesNotExist: #
            user_name = email_username #
            
        user = authenticate(request, username = user_name, password = pass_word) #
            
        if user is not None:
            login(request, user)
            messages.success(request, 'Login successful!')
            return redirect('home')
        else:
            messages.error(request, 'Invalid credentials')
    
    return render(request, 'accounts/login.html')

@login_required
def profile(request):
    if request.user.role == 'recruiter':
        # ✅ Fixed: recruiterprofile lowercase + .recruiterprofile
        all_jobs = Job.objects.filter(recruiter=request.user.recruiterprofile)
    else:
        # ✅ Fixed: Job.objects.none()
        all_jobs = Job.objects.none()
    
    sort = request.GET.get('sort')
    if sort == 'asc':
        all_jobs = all_jobs.order_by('job_title')
    elif sort == 'desc':
        all_jobs = all_jobs.order_by('-job_title')
    # Default: all_jobs remains as-is (recruiter's jobs or empty)
    
    context = {
        'jobs': all_jobs, # dict = { 'key' : variable}
        }
    return render(request, 'accounts/profile.html', context)

@login_required
def log_out(request):
    
    logout(request)
    messages.success(request, 'logout done')
    return redirect('login') 
