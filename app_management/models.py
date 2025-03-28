from django.db import models

# Create your models here.

class App(models.Model):
    app_name = models.CharField(max_length=200)
    version = models.CharField(max_length=50)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.app_name} (v{self.version})"