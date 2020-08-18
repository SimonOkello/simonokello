from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string
from django.views.decorators.csrf import csrf_exempt

from .forms import PostForm
from .filters import ProjectFilter

from .models import Project

# Create your views here.

@csrf_exempt
def index(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        message = request.POST['message']
        

        email = EmailMessage(
            request.POST['subject'],
            template,
            settings.EMAIL_HOST_USER,
            ['simonokello.dev@gmail.com']
        )

        email.fail_silently = False
        email.send()
    
    return render(request, 'portfolio/index.html', {})


def projects(request):
    posts = Project.objects.filter(active=True)
    myFilter = ProjectFilter(request.GET, queryset=posts)
    posts = myFilter.qs

    page = request.GET.get('page')

    paginator = Paginator(posts, 5)

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    context = {'posts': posts, 'myFilter': myFilter}
    return render(request, 'portfolio/projects.html', context)


def project_info(request, slug):
    post = Project.objects.get(slug=slug)

    context = {'post': post}
    return render(request, 'portfolio/project_detail.html', context)


def profile(request):
    return render(request, 'portfolio/profile.html')

# CRUD VIEWS


@login_required(login_url="index")
def createProject(request):
    form = PostForm()

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('index')

    context = {'form': form}
    return render(request, 'portfolio/project_form.html', context)


@login_required(login_url="index")
def updateProject(request, slug):
    project = Project.objects.get(slug=slug)
    form = PostForm(instance=project)

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
        return redirect('index')

    context = {'form': form}
    return render(request, 'portfolio/project_form.html', context)


@login_required(login_url="index")
def deleteProject(request, slug):
    project = Project.objects.get(slug=slug)

    if request.method == 'POST':
        post.delete()
        return redirect('index')
    context = {'item': post}
    return render(request, 'portfolio/delete.html', context)


