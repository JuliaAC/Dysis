import os
from django.db import models
from django.conf import settings
from django.utils import timezone

class Post(models.Model):
    author = models.ForeignKey('auth.User',on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Dysisci(models.Model):
    ZONNIE = 'ZO'
    LID = 'LI'
    LUNA = 'LU'
    TYPE_CHOICES = (
        (ZONNIE, 'Zonnestraaltje'),
        (LID, 'Lid'),
        (LUNA, 'Luna'),
    )
    type = models.CharField(
        max_length=2,
        choices=TYPE_CHOICES,
        default=ZONNIE,
    )
    naam = models.CharField(max_length=60)
    generatie = models.IntegerField()
    studie = models.CharField(max_length=50)
    foto = models.ImageField(upload_to= '')
    info = models.TextField()

    def publish(self):
        Dysisci.foto.delete(False)
        self.save()

    def __str__(self):
        return self.naam


class Picture(models.Model):
    description = models.CharField(max_length=225, blank=True)
    document = models.FileField(upload_to='documents/')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, default=13)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def publish(self):
        self.uploaded_at = timezone.now()
        self.save()

    def __str__(self):
        return self.description