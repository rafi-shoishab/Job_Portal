from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home, name='home'),
    path('add_job/', views.add_job, name='add_job'),
    path('all_job/', views.all_job, name='all_job'),
    path('browse_job/', views.browse_job, name='browse_job'),
<<<<<<< HEAD
    path('single_job_view/', views.single_job_view, name='single_job_view'),
    path('edit_job/<int:job_id>', views.edit_job, name='edit_job'),
    path('delete_job/<int:job_id>', views.delete_job, name='delete_job'),
=======
    path('single_job_view/<int:job_id>', views.single_job_view, name='single_job_view'),
    path('edit_job/<int:job_id>', views.edit_job, name='edit_job'),
    path('delete_job/', views.delete_job, name='delete_job'),
>>>>>>> 3b42806 (edit,brows,single done.)
    path('about_us/', views.about_us, name='about_us'),
]
