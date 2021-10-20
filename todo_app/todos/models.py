from django.db import models

# Create your models here.


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Task(BaseModel):
    name = models.CharField(max_length=200)
    description = models.TextField()
    done = models.BooleanField()
