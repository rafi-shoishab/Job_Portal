from django.urls import path
from . import views 

urlpatterns = [
    path('add_job/', views.add_job, name='add_job'), # 'url rout show: '/name/' ..... name='url name used in {% url %}'
    path('browse_job/', views.browse_job, name='browse_job'),
    path('delete_job/<int:job_id>', views.delete_job, name='delete_job'),
    path('single_job_view/<int:job_id>', views.single_job_view, name='single_job_view'),
    path('edit_job/<int:job_id>', views.edit_job, name='edit_job'),
]
