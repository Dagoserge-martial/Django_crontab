from django.db import models

# Create your models here.
class Crontab(models.Model):
    titre = models.CharField(max_length=50)

    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.titre
