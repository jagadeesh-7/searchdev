
from django.urls import path, include

from . import views
urlpatterns = [
    path('', views.projects, name = 'projects' ),
    path('projects/project/<str:pk>/', views.project, name = 'project' ),
    path('projects/update-project/<str:pk>/', views.updateProject, name = 'update-project' ),
    path('create-project/', views.createProject, name = 'create-project' ),
    path('delete-project/<str:pk>/', views.deleteProject, name = 'delete-project' ),
]
