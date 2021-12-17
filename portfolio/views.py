from django.shortcuts import render
from django.http import HttpResponse
 
from portfolio.models import Project

# Create your views here.

def index(request):
    projects = Project.objects.all()  # query all objs in projects table in database
    # contxts sends information to template. every view func needs one
    context = {
        'projects': projects,
    }

    return render(request, 'portfolio/index.html', context)

def detail(request, pk):
    # perform query for object in projects table with primary key
    project = Project.objects.get(pk=pk)
    # assign project with primary key to context to
    # pass information to views template
    context = {
        'project': project
    }

    return render(request, 'portfolio/detail.html', context)
