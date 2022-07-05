from django import forms
from django.db.models.fields.files import ImageField
from django.forms import widgets
from django.forms.widgets import ClearableFileInput, FileInput, RadioSelect, Widget
from django.utils.html import word_split_re


class EditProfileForm(forms.Form):

    avatar = forms.ImageField(required=False, widget=forms.FileInput)
    name = forms.CharField()
    title = forms.CharField(required=False)
    bio = forms.CharField(required=False, widget=forms.Textarea(attrs={'rows': 8, 'maxlength':220}))
    location = forms.CharField(required=False)
    
    class Meta:
        fields = ["username", "avatar", "name", "title", "bio", "location"]

class EducationForm(forms.Form):
    start_year = forms.IntegerField(widget=forms.TextInput(attrs={'maxlength':4}))
    end_year = forms.IntegerField(widget=forms.TextInput(attrs={'maxlength':4}))
    department = forms.CharField(max_length=50, required=False)
    school = forms.CharField(max_length=50)
    is_highschool = forms.BooleanField(required=False)

    class Meta:
        fields = ["start_year", "end_year", "department", "school", "is_highschool"]

class WorkForm(forms.Form):
    start_year = forms.IntegerField(widget=forms.TextInput(attrs={'maxlength':4}))
    end_year = forms.IntegerField(widget=forms.TextInput(attrs={'maxlength':4}))
    position = forms.CharField(max_length=50)
    firm = forms.CharField(max_length=50)

    class Meta:
        fields = ["start_year", "end_year", "position", "firm"]

class SkillForm(forms.Form):
    name = forms.CharField(max_length=50)
    beginner = 1
    elementary = 2
    intermediate = 3
    advanced = 4
    expert = 5
    rating_choices = [
        (beginner, 'Beginner'),
        (elementary, 'Elementary'),
        (intermediate, 'Intermediate'),
        (advanced, 'Advanced'),
        (expert, 'Expert'),
    ]
    rating = forms.IntegerField(widget=forms.RadioSelect(choices=rating_choices))
    
    class Meta:
        fields = ["name", "rating"]

class LanguageForm(forms.Form):
    name = forms.CharField(max_length=50)
    beginner = 1
    elementary = 2
    intermediate = 3
    advanced = 4
    native = 5
    rating_choices = [
        (beginner, 'Beginner'),
        (elementary, 'Elementary'),
        (intermediate, 'Intermediate'),
        (advanced, 'Advanced'),
        (native, 'Native'),
    ]
    rating = forms.IntegerField()
    
    class Meta:
        fields = ["name", "rating"]

class HobbyForm(forms.Form):
    name = forms.CharField(max_length=50)
    description = forms.CharField(max_length=400)
    
    class Meta:
        fields = ["name", "description"]


class CertificateForm(forms.Form):
    certificate = 'certificate'
    award = 'award'
    type_choices = [
        (certificate, 'Certificate'),
        (award, 'Award'),
    ]
    type = forms.ChoiceField(choices=type_choices)
    description = forms.CharField(max_length=400)
    year = forms.IntegerField()

    class Meta:
        fields = ["type", "description", "year"]