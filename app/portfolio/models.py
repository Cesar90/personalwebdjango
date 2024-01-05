from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to="projects")
    created = models.DateTimeField(auto_now_add=True) #This execute once time
    updated = models.DateTimeField(auto_now=True) #This execute each update time

    class Meta:
        verbose_name = "Project"
        verbose_name_plural = "Project"
        ordering = ["-created"]

    def __str__(self):
        return self.title
