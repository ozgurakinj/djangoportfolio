from django.contrib.auth.forms import UsernameField
from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from .forms import *
from django.views.decorators.cache import never_cache 
from register import *

# Create your views here.

def index(response):
        if response.user.is_authenticated:
                logged_in_user = Profile.objects.get(username=response.user)
        else:
                logged_in_user = ""
        return render(response, "main/index.html", {"response":response, "logged_in_user":logged_in_user})

def profile(response):
        if response.user.is_authenticated:
                return HttpResponseRedirect('/profile/{}'.format(response.user.username))
        else:
                return HttpResponseRedirect('/')

@never_cache
def user(response, username):
        if Profile.objects.filter(username=username):
                user = Profile.objects.get(username=username)
                education = Education.objects.filter(owner=user).order_by('-start_year')
                work = Experience.objects.filter(owner=user).order_by('-start_year')
                language = Language.objects.filter(owner=user).order_by('-rating')
                hobby = Hobby.objects.filter(owner=user)
                skills = Skill.objects.filter(owner=user).order_by('-rating')
                certificate = Certificate.objects.filter(owner=user).order_by('-year')
                educationform = EducationForm()
                workform = WorkForm()
                certificateform = CertificateForm()
                hobbyform = HobbyForm()
                if response.user.is_authenticated:
                        logged_in_user = Profile.objects.get(username=response.user)
                else:
                        logged_in_user = ""
                edit_profile_form = EditProfileForm(initial={"username":user.username, "avatar" : user.avatar, "name" : user.name, "title" : user.title, "bio" : user.biography, "location" : user.location,})
                return render(response, "main/user.html", {
                        "logged_in_user":logged_in_user,
                        "response":response,"user":user,
                        "education":education, "work":work,
                        "language":language, "hobby":hobby,
                        "skills":skills,"certificate":certificate,
                        "edit_profile_form":edit_profile_form,
                        "educationform": educationform,
                        "workform": workform,
                        "hobbyform": hobbyform,
                        "certificateform" : certificateform,
                        })
        else:
                return HttpResponse("Profile Not Found")

def edit(response):
        if response.method == 'POST':
                if response.user.is_authenticated:                
                        form = EditProfileForm(response.POST, response.FILES)
                        if 'submit-clear' in response.POST:
                                profile = Profile.objects.get(username=response.user.username)
                                profile.avatar.delete()
                                profile.save()
                                return HttpResponseRedirect('/profile/{}#editmodal'.format(response.user.username))
                        if form.is_valid():
                                profile = Profile.objects.get(username=response.user.username)
                                if response.FILES:
                                        profile.avatar = response.FILES['avatar']
                                profile.color = response.POST['form-color']
                                profile.name = form.cleaned_data['name'].strip()
                                profile.title = form.cleaned_data['title'].strip()
                                profile.biography = form.cleaned_data['bio'].strip()
                                profile.location = form.cleaned_data['location'].strip()
                                profile.save()
                                return HttpResponseRedirect('/profile/{}'.format(response.user.username))
                        else:
                                print(form.cleaned_data)
                                print(form.errors)
                                return HttpResponseRedirect('/one/{}'.format(response.user.username))
                else:
                        return HttpResponseRedirect('/two/{}'.format(response.user.username))
        else:
                return HttpResponseRedirect('/three/{}'.format(response.user.username))

def add(response):
         if response.method == 'POST':
                if response.user.is_authenticated:                
                        if 'submit-addeducation' in response.POST:
                                form = EducationForm(response.POST)
                                if form.is_valid():
                                        print(form.cleaned_data)
                                        edu = Education()
                                        edu.owner = Profile.objects.get(username=response.user.username)
                                        edu.start_year = form.cleaned_data['start_year']
                                        edu.end_year = form.cleaned_data['end_year']
                                        edu.department = form.cleaned_data['department']
                                        edu.school = form.cleaned_data['school']
                                        edu.is_highschool = form.cleaned_data['is_highschool']
                                        edu.save()
                                        return HttpResponseRedirect('/profile/{}'.format(response.user.username))
                        if 'submit-addwork' in response.POST:
                                form = WorkForm(response.POST)
                                if form.is_valid():
                                        work = Experience()
                                        work.owner = Profile.objects.get(username=response.user.username)
                                        work.start_year = form.cleaned_data['start_year']
                                        work.end_year = form.cleaned_data['end_year']
                                        work.position = form.cleaned_data['position']
                                        work.firm = form.cleaned_data['firm']
                                        work.save()
                                        return HttpResponseRedirect('/profile/{}'.format(response.user.username))
                        if 'submit-addskill' in response.POST:
                                form = SkillForm(response.POST)
                                if form.is_valid():
                                        skill = Skill()
                                        skill.owner = Profile.objects.get(username=response.user.username)
                                        skill.name = form.cleaned_data['name']
                                        skill.rating = form.cleaned_data['rating']
                                        skill.save()
                                        return HttpResponseRedirect('/profile/{}'.format(response.user.username))
                        if 'submit-addlang' in response.POST:
                                form = LanguageForm(response.POST)
                                if form.is_valid():
                                        lang = Language()
                                        lang.owner = Profile.objects.get(username=response.user.username)
                                        lang.name = form.cleaned_data['name']
                                        lang.rating = form.cleaned_data['rating']
                                        lang.save()
                                        return HttpResponseRedirect('/profile/{}'.format(response.user.username))
                        if 'submit-addhobby' in response.POST:
                                form = HobbyForm(response.POST)
                                if form.is_valid():
                                        hobby = Hobby()
                                        hobby.owner = Profile.objects.get(username=response.user.username)
                                        hobby.name = form.cleaned_data['name']
                                        hobby.description = form.cleaned_data['description']
                                        hobby.save()
                                        return HttpResponseRedirect('/profile/{}'.format(response.user.username))
                        if 'submit-addcert' in response.POST:
                                form = CertificateForm(response.POST)
                                if form.is_valid():
                                        cert = Certificate()
                                        cert.owner = Profile.objects.get(username=response.user.username)
                                        cert.type = form.cleaned_data['type']
                                        cert.description = form.cleaned_data['description']
                                        cert.year = form.cleaned_data['year']
                                        cert.save()
                                        return HttpResponseRedirect('/profile/{}'.format(response.user.username))
                        