from django.db import models

# Create your models here.
# MVC model view controller

class Walk(models.Model):
    walk_id = models.PositiveIntegerField(primary_key=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    time = models.DateTimeField(auto_now=False, auto_now_add=True)
    comments = models.TextField()

    def __str__(self):
        return self.walk_id
