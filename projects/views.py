from django.shortcuts import redirect, render
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from projects.utils import paginateProjects, searchProject
from .models import Project, Review, Tag
from .forms import ProjectForm, ReviewForm
# Create your views here.


def projects(request):
    projects,search_query = searchProject(request)
    custom_range,projects,paginator = paginateProjects(request,projects,3)
    context = {
        'projects':projects,
        'search_query':search_query,
        'paginator':paginator,
        'custom_range':custom_range
    }
    return render(request, 'projects/projects.html',context)

def project(request, pk):
    project = Project.objects.get(id = pk)
    # review = Review.objects.get(project = project, owner = request.user.profile)
    form = ReviewForm()
    
    if request.method == 'POST':
        # form = ReviewForm(request.POST, instance = review)
        form = ReviewForm(request.POST)
        review = form.save(commit=False)
        review.project = project
        review.owner = request.user.profile
        review.save()
        project.getVoteCount
        messages.success(request, "Your review was successfully submitted!")
        return redirect('project', pk=pk)
    context = {
        'project':project,
        'form':form
    }
    return render(request, 'projects/single-project.html',context)


@login_required(login_url="login")
def createProject(request):
    profile = request.user.profile
    form = ProjectForm()
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.owner = profile
            project.save()
            form.save_m2m()
            return redirect('projects')

    context = {
        'form':form
    }
    return render(request, 'projects/project_form.html', context)


@login_required(login_url="login")
def updateProject(request, pk):
    profile = request.user.profile
    project = profile.project_set.get(id = pk)
    form = ProjectForm(instance=project)
    if request.method == 'POST':
        newTags = request.POST.get('newtags').replace(',',' ').split()
        form = ProjectForm(request.POST,request.FILES,instance=project)
        if form.is_valid():
            form.save()
            for tag in newTags:
                tag, created = Tag.objects.get_or_create(name=tag)
                project.tags.add(tag)
            return redirect('projects')

    context = {
        'form':form,
        'project':project
    }
    return render(request, 'projects/project_form.html', context)

@login_required(login_url="login")
def deleteProject(request, pk):
    profile = request.user.profile
    project = profile.project_set.get(id = pk)
    if request.method == 'POST':
        project.delete()
        return redirect('account')
    context = {
        'object':project.title
    }
    return render(request,'projects/delete_template.html', context)

