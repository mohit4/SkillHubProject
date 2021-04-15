from django.db import models


class BaseModel(models.Model):
    """
    BaseModel abstract class with primitive fields
    """
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True