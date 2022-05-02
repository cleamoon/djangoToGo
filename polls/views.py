from django.shortcuts import render, redirect
from polls.models import Project, Manager

def show_projects(request):
    projects = Project.objects.all().order_by('id')
    return render(request, 'projects.html', {'projects': projects})

def show_managers(request):
    try:
        proj_id = int(request.GET.get('proj_id'))
        managers = []
        if proj_id:
            project = Project.objects.only('name').get(id=proj_id)
            managers = Manager.objects.filter(proj_id=project).order_by('id')
        return render(request, 'managers.html', {
            'project': project,
            'managers': managers
        })
    except (ValueError, Project.DoesNotExist):
        return redirect('/')
