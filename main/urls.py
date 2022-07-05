from django.urls import path
from django.urls.conf import include
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
 path("", views.index, name="index"),
    path("profile/<str:username>/", views.user, name="user"),
    path("profile/", views.profile, name="profile"),
    path("edit/", views.edit, name="edit"),
    path("add/", views.add, name="add"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
