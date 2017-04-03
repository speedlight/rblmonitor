from django.db import models

class Rbllist(models.Model):
    name = models.CharField(max_length=100)
    url = models.URLField(max_length=100, unique=True)
    description = models.CharField(max_length=300, null=True, blank=True)

    def __str__(self):
        return self.name