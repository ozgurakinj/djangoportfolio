from django.core.files import storage
from django.db import models, reset_queries
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ForeignKey, OneToOneField
from django.contrib.auth.models import User
from portfolio.storage import OverwriteStorage
from django_resized import ResizedImageField
import os


def photo_path(instance, filename):
    basefilename, file_extension= os.path.splitext(filename)
    return 'avatar/{username}_avatar{ext}'.format(username=instance.user.username, ext=file_extension)


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=CASCADE)
    username = models.CharField(max_length=50)
    avatar = ResizedImageField(null=True, blank=True, size=[400, 400], crop=['middle', 'center'], storage=OverwriteStorage(), upload_to=photo_path)
    name = models.CharField(max_length=150)
    title = models.CharField(max_length=150)
    biography = models.TextField(max_length=220)
    location = models.CharField(max_length=50)
    color_blue = 'primary'
    color_red = 'danger'
    color_green = 'success'
    color_yellow = 'warning'
    color_cyan = 'info'
    color_grey = 'secondary'
    color_choices = [
        (color_blue, 'Blue'),
        (color_red, 'Red'),
        (color_green, 'Green'),
        (color_yellow, 'Yellow'),
        (color_cyan, 'Cyan'),
        (color_grey, 'Grey'),
    ]
    color = models.CharField(max_length=20, choices=color_choices,default=color_blue)
    
    def __str__(self):
        return self.user.username


class Education(models.Model):
    start_year = models.IntegerField()
    end_year = models.IntegerField()
    department = models.CharField(max_length=50, blank=True)
    school = models.CharField(max_length=50)
    is_highschool = models.BooleanField()
    owner = models.ForeignKey(Profile,  on_delete=models.CASCADE)

    def __str__(self):
        return self.owner.username + " Education " +str(self.pk)

class Experience(models.Model):
    start_year = models.IntegerField()
    end_year = models.IntegerField()
    position = models.CharField(max_length=50)
    firm = models.CharField(max_length=50)
    owner = models.ForeignKey(Profile,  on_delete=models.CASCADE)

    def __str__(self):
        return self.owner.username + " Experience " +str(self.pk)

class Skill(models.Model):
    name = models.CharField(max_length=50)
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
    rating = models.IntegerField(choices=rating_choices,default=beginner)
    owner = models.ForeignKey(Profile,  on_delete=models.CASCADE)
    
    def __str__(self):
        return self.owner.username + " Skill " +str(self.pk)


class Language(models.Model):
    name = models.CharField(max_length=50)
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
    rating = models.IntegerField(choices=rating_choices,default=beginner)
    owner = models.ForeignKey(Profile,  on_delete=models.CASCADE)
    def __str__(self):
        return self.owner.username + " Language " +str(self.pk)


class Hobby(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=400)
    owner = models.ForeignKey(Profile,  on_delete=models.CASCADE)
    
    def __str__(self):
        return self.owner.username + " Hobby " +str(self.pk)


class Certificate(models.Model):
    certificate = 'certificate'
    award = 'award'
    type_choices = [
        (certificate, 'Certificate'),
        (award, 'Award'),
    ]
    type = models.CharField(max_length=50, choices=type_choices,default=certificate)
    description = models.CharField(max_length=400)
    year = models.IntegerField()
    owner = models.ForeignKey(Profile,  on_delete=models.CASCADE)
    def __str__(self):
        return self.owner.username + " Certificate " +str(self.pk)