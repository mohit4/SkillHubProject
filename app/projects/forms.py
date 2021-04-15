from django.forms import ModelForm

from .models import Project


class ProjectForm(ModelForm):
    """
    Form class for creating and editing a Project
    """
    class Meta:
        model = Project
        fields = ['title', 'subtitle', 'description', 'due_date', 'user']
