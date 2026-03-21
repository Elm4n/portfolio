from django.shortcuts import render, get_object_or_404
from .models import Project

def home(request):
    return render(request, 'core/home.html')

def projects(request):
    all_projects = Project.objects.all()
    return render(request, 'core/projects.html', {'projects': all_projects})

def project_detail(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    return render(request, 'core/project_detail.html', {'project':project})

def about(request):
    return render(request, 'core/about.html')

# Create your views here.
