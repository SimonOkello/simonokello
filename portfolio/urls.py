from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name="index"),
	path('projects/', views.projects, name="projects"),
	path('project/<slug:slug>/', views.project_info, name="project"),
	path('profile/', views.profile, name="profile"),

	#CRUD PATHS

	path('create_project/', views.createProject, name="create_project"),
	path('update_project/<slug:slug>/', views.updateProject, name="update_project"),
	path('delete_project/<slug:slug>/', views.deleteProject, name="delete_project"),


	path('send_email/', views.sendEmail, name="send_email"),
]