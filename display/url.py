from django.urls import path, include
from display import views

urlpatterns = [
    path("", views.home, name="index"),
    path("profile", views.profile, name="profile"),
    path("skill", views.skill, name="skill"),
    path("project", views.project, name="project"),
    path("project2/<str:pk>", views.project2, name="project2"),
    path("education", views.education, name="education"),
]