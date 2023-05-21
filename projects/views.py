from django.shortcuts import render
from django.http import HttpResponse

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
    return render(request, 'projects/projects.html', {'projectList': projectList})

def project(request, pk):
    projectObj = None
    for project in projectList:
        if project['id'] == pk:
            projectObj = project
            break
    return render(request, 'projects/single-project.html', {'projectObj': projectObj})

