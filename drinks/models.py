from django.db import models

class drink(models.Model):
    name = models.CharField(max_length=100)
    description =models.CharField(max_length=500)

    def __str__(self) -> str:
        return self.name