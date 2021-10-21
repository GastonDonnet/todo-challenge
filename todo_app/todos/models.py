from django.db import models
from django.db.models.fields import BLANK_CHOICE_DASH

# Create your models here.


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Task(BaseModel):
    name = models.CharField(max_length=200, blank=True)
    description = models.TextField(blank=True)
    done = models.BooleanField(default=False)
