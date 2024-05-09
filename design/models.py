from django.db import models
class design(models.Model):
    images = models.FileField(upload_to="design/", max_length=250, null=True, default=None)


# Create your models here.
