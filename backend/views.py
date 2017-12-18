# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render

# Create your views here.
from django.utils import timezone
from .models import Section
from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView 
#from .forms import SectionForm

class HomePageView(TemplateView):
    template_name = "backend/home.html"

class AlgsPageView(TemplateView):
    template_name = "backend/algs.html"

class BiblioPageView(TemplateView):
    template_name = "backend/biblio.html"

class RefPageView(TemplateView):
    template_name = "backend/b-algs.html"

# def index(request):
#     sections = Section.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
#     return render(request, 'backend/index.html', {'sections': sections})

# def home_list(request):
#     sections = Section.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
#     return render(request, 'backend/home.html', {'sections': sections})

'''
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'backend/post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'backend/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'backend/post_edit.html', {'form': form})
'''
