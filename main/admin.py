from django.contrib import admin
from .models import Certificate, Education, Experience, Hobby, Language, Skill, Profile

class EducationInline(admin.StackedInline):
    model = Education
    extra = 1
class ExperienceInline(admin.StackedInline):
    model = Experience
    extra = 1
class HobbyInline(admin.StackedInline):
    model = Hobby
    extra = 1
class LanguageInline(admin.StackedInline):
    model = Language
    extra = 1
class SkillInline(admin.StackedInline):
    model = Skill
    extra = 1
class CertificateInline(admin.StackedInline):
    model = Certificate
    extra = 1


class ProfileAdmin(admin.ModelAdmin):
    inlines = [
        EducationInline,
        ExperienceInline,
        HobbyInline,
        LanguageInline,
        SkillInline,
        CertificateInline,
    ]


admin.site.register(Profile, ProfileAdmin)
admin.site.register(Experience)
admin.site.register(Education)
admin.site.register(Skill)
admin.site.register(Hobby)
admin.site.register(Language)
admin.site.register(Certificate)