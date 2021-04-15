from datetime import datetime

from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

from skillhub.models import BaseModel


class Project(BaseModel):
    """
    Project class is the leading entity of Projects app
    """
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    
    start_date = models.DateTimeField(null=True, blank=True)
    end_date = models.DateTimeField(null=True, blank=True)
    due_date = models.DateTimeField(null=True, blank=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='projects')

    def __str__(self):
        return f"@{self.user.username}/{self.title}"
    
    def isDelayed(self):
        return True if datetime.now() > self.due_date else False
    
    def get_absolute_url(self):
        return reverse("projects:project-details", kwargs={"pk": self.pk})
    