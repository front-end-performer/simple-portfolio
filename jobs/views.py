from django.shortcuts import render
from .models import Job

# Create your views here.

def home(request):
    # grabbing all objects from JObs
    jobs = Job.objects
    return render(request, 'jobs/home.html', { 'jobs': jobs})
