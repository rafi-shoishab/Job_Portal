from django.shortcuts import render


# Create your views here.
def apply(request):
    return render(request, 'applications/apply.html')