from django.db import models
from django.contrib.auth.models import User


class Pdf(models.Model):
    PDFfile = models.FileField(upload_to='PDF/')

    