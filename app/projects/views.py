from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import (
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy
from django.urls import reverse

from .models import Project


class ProjectListView(ListView):
    """
    Listing all the projects in database
    """
    model = Project
    template_name = 'project_list.html'


class ProjectDetailView(DetailView):
    """
    Printing the details of a single project
    """
    model = Project
    template_name = 'project_details.html'


class ProjectCreateView(CreateView):
    """
    Creating a new project in the system
    """
    model = Project
    template_name = 'project_create.html'
    fields = ('title', 'subtitle', 'description', 'due_date', 'user')


class ProjectUpdateView(UpdateView):
    """
    Updating an existing project in the system
    """
    model = Project
    template_name = 'project_update.html'
    fields = ('subtitle', 'description')


class ProjectDeleteView(DeleteView):
    """
    Deleting an existing project in the system
    """
    model = Project
    template_name = 'project_details.html'
    success_url = reverse_lazy('projects:all-projects-list')
