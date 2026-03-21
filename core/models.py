from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    github_link = models.URLField(blank=True, null=True)
    image = models.ImageField
    
    def __str__(self):
        return self.title

# Create your models here.
