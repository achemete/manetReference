# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import redirect, render, get_object_or_404

from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.utils import timezone
# Create your views here.

from django.contrib.auth.decorators import login_required
from .models import Section, Sectionright, Algoleft, Algoright
from django.views.generic import TemplateView 

from .forms import PostSection, SignUpForm, PostSectionr, PostAlgoLeft, PostAlgoRight#, BackHomeL, BackHomeR, BackAlgL, BackAlgR

####
## Template Views
####

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

####
## Home Views
####

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

####
## Algorithms Views
####

def algos_list(request):
	sections = Algoleft.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	sectionsR = Algoright.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'backend/algs.html', {'sections': sections, 'sectionsR': sectionsR})

def algol_detail(request, pk):
	section = get_object_or_404(Algoleft, pk=pk)
	return render(request, 'backend/algoL_detail.html', {'section': section})

def algor_detail(request, pk):
	sectionR = get_object_or_404(Algoright, pk=pk)
	return render(request, 'backend/algoR_detail.html', {'sectionR': sectionR})

def algLeft_new(request):
	if request.method == "POST":
		form = PostAlgoLeft(request.POST)
		if form.is_valid():
			section = form.save(commit=False)
			section.author = request.user
			section.published_date = timezone.now()
			section.save()
			return redirect('algol_detail', pk=section.pk) 
	else:
		form = PostAlgoLeft()
	return render(request, 'backend/algoLeft_edit.html', {'form': form})

def algRight_new(request):
	if request.method == "POST":
		form = PostAlgoRight(request.POST)
		if form.is_valid():
			section = form.save(commit=False)
			section.author = request.user
			section.published_date = timezone.now()
			section.save()
			return redirect('algor_detail', pk=section.pk) 
	else:
		form = PostAlgoRight()
	return render(request, 'backend/algoRight_edit.html', {'form': form})

def algLeft_edit(request, pk):
	section = get_object_or_404(Algoleft, pk=pk)
	if request.method == "POST":
		form = PostAlgoLeft(request.POST, instance=section)
		if form.is_valid():
			section = form.save(commit=False)
			section.author = request.user
			section.published_date = timezone.now()
			section.save()
			return redirect('algol_detail', pk=section.pk)
	else:
		form = PostAlgoLeft(instance=section)
	return render(request, 'backend/algoLeft_edit.html', {'form': form})

def algLeft_remove(request, pk):
	section = get_object_or_404(Algoleft, pk=pk)
	section.delete()
	return redirect('algos_list')

def algRight_edit(request, pk):
	section = get_object_or_404(Algoright, pk=pk)
	if request.method == "POST":
		form = PostAlgoRight(request.POST, instance=section)
		if form.is_valid():
			section = form.save(commit=False)
			section.author = request.user
			section.published_date = timezone.now()
			section.save()
			return redirect('algor_detail', pk=section.pk)
	else:
		form = PostAlgoRight(instance=section)
	return render(request, 'backend/algoRight_edit.html', {'form': form})

def algRight_remove(request, pk):
	section = get_object_or_404(Algoright, pk=pk)
	section.delete()
	return redirect('algos_list')

####
## Backend Views
####

# def home_list(request):
# 	sections = Section.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
# 	sectionsR = Sectionright.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
# 	return render(request, 'backend/backhome.html', {'sections': sections, 'sectionsR': sectionsR})

# def algos_list(request):
# 	sections = Algoleft.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
# 	sectionsR = Algoright.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
# 	return render(request, 'backend/backalgs.html', {'sections': sections, 'sectionsR': sectionsR})

def list_users(request):
	user = User.objects.all()
	return render(request, 'backend/list_users.html', {'user': user})

####
## Other Views
####

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

