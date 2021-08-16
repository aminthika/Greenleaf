from django.db import models

class Rewild(models.Model):
    email = models.EmailField()
    location = models.CharField(max_length=256)
    trees = models.IntegerField()


class RewildPhoto(models.Model):
    rewild = models.ForeignKey(Rewild, on_delete=models.PROTECT)
    image = models.ImageField()
        
