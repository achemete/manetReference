# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import redirect, render, get_object_or_404

from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.utils import timezone
# Create your views here.

from .models import Section, Sectionright
from django.views.generic import TemplateView 

from .forms import PostSection, SignUpForm, PostSectionr

class HomePageView(TemplateView):
	template_name = "backend/home.html"

class AlgsPageView(TemplateView):
	template_name = "backend/algs.html"

class BiblioPageView(TemplateView):
	template_name = "backend/biblio.html"

class RefPageView(TemplateView):
	template_name = "backend/b-algs.html"

class SignUpPageView(TemplateView):
	template_name = "backend/signup.html"

class BackendPageView(TemplateView):
	template_name = "backend/backend.html"

class OperationsPageView(TemplateView):
	template_name = "backend/operations.html"

# def index(request):
#     sections = Section.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
#     return render(request, 'backend/index.html', {'sections': sections})

def home_list(request):
	sections = Section.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	sectionsR = Sectionright.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'backend/home.html', {'sections': sections, 'sectionsR': sectionsR})

def home_detail(request, pk):
	section = get_object_or_404(Section, pk=pk)
	return render(request, 'backend/home_detail.html', {'section': section})

def homeR_detail(request, pk):
	sectionR = get_object_or_404(Sectionright, pk=pk)
	return render(request, 'backend/homeR_detail.html', {'sectionR': sectionR})

def homeSection_new(request):
	if request.method == "POST":
		form = PostSection(request.POST)
		if form.is_valid():
			section = form.save(commit=False)
			section.author = request.user
			section.published_date = timezone.now()
			section.save()
			return redirect('home_detail', pk=section.pk)
	else:
		form = PostSection()
	return render(request, 'backend/section_edit.html', {'form': form})

def homeSectionRight_new(request):
	if request.method == "POST":
		form = PostSectionr(request.POST)
		if form.is_valid():
			sectionR = form.save(commit=False)
			sectionR.author = request.user
			sectionR.published_date = timezone.now()
			sectionR.save()
			return redirect('homeR_detail', pk=sectionR.pk)
	else:
		form = PostSectionr()
	return render(request, 'backend/section_edit.html', {'form': form})

def section_edit(request, pk):
	section = get_object_or_404(Section, pk=pk)
	if request.method == "POST":
		form = PostSection(request.POST, instance=section)
		if form.is_valid():
			section = form.save(commit=False)
			section.author = request.user
			section.published_date = timezone.now()
			section.save()
			return redirect('home_detail', pk=section.pk)
	else:
		form = PostSection(instance=section)
	return render(request, 'backend/section_edit.html', {'form': form})

def section_remove(request, pk):
	section = get_object_or_404(Section, pk=pk)
	section.delete()
	return redirect('home_list')

def sectionR_edit(request, pk):
	section = get_object_or_404(Sectionright, pk=pk)
	if request.method == "POST":
		form = PostSectionr(request.POST, instance=section)
		if form.is_valid():
			section = form.save(commit=False)
			section.author = request.user
			section.published_date = timezone.now()
			section.save()
			return redirect('homeR_detail', pk=section.pk)
	else:
		form = PostSectionr(instance=section)
	return render(request, 'backend/sectionR_edit.html', {'form': form})

def sectionR_remove(request, pk):
	section = get_object_or_404(Sectionright, pk=pk)
	section.delete()
	return redirect('home_list')

def algSection_new(request):
	if request.method == "POST":
		form = PostSection(request.POST)
		if form.is_valid():
			section = form.save(commit=False)
			section.author = request.user
			section.published_date = timezone.now()
			section.save()
			return redirect('home_list')#, pk=section.pk)
	else:
		form = PostSection()
	return render(request, 'backend/section_edit.html', {'form': form})

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home_list')
    else:
        form = SignUpForm()
    return render(request, 'backend/signup.html', {'form': form})

def list_users(request):
	user = User.objects.all()
	return render(request, 'backend/list_users.html', {'user': user})
