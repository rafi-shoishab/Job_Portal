from django.db import models 
from accounts.models import RecruiterProfile

# Create your models here.
class Job(models.Model):
    
    CATEGORY_CHOICES = (
        ('part_time', 'Part Time'), #
        ('full_time', 'Full Time'),
        ('intern', 'Internship'),
        ('contract', 'Contractual')
    )
    
    TYPE_CHOICES = (
        ('remote','Remote'),
        ('onsite', 'On-Site'),
        ('hybrid', 'Hybrid')
    )
    
    recruiter = models.ForeignKey(RecruiterProfile, on_delete=models.CASCADE)
    job_title = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    company_logo = models.ImageField(upload_to='company_logos/', null=True, blank=True)
    job_location = models.CharField(max_length=100)
    job_type = models.CharField(max_length=30, choices=TYPE_CHOICES)
    vacancy = models.IntegerField()
    category = models.CharField(max_length=30, choices=CATEGORY_CHOICES)
    job_description = models.TextField()
    skills = models.CharField(max_length=100)
    salary = models.IntegerField()
    deadline = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self): 
        return self.job_title 