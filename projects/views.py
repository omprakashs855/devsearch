from django.shortcuts import render
from django.http import HttpResponse
from .models import Project

projectList = [
    {
        "id":"1",
        "title": "Ecommerce Website",
        "description": "Fully functional ecommerce website"
    },
    {
        "id":"2",
        "title": "Portfolio Website",
        "description": "This was a project where I build out my portfolio"
    },
    {
        "id":"3",
        "title": "Social Network",
        "description": "Awesome open source project I am still working on"
    }
]

def projects(request):
    page = "Hello, you are on the projects page"
    return render(request, 'projects/projects.html', {'projectList': Project.objects.all()})

def project(request, pk):
    projectObj = Project.objects.get(id=pk)
    # tags = projectObj.tags.all()
    # return render(request, 'projects/single-project.html', {'project': projectObj, 'tags': tags})
    return render(request, 'projects/single-project.html', {'project': projectObj})

