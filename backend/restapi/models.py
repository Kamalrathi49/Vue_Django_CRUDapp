from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=99)
    description = models.TextField()
    created_by = models.CharField(max_length=99)

    def __str__(self) -> str:
        return self.title