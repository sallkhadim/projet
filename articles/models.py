from django.db import models
from django import forms

# Create your models here.
class Articles(models.Model):
    titre = models.CharField(max_length=255)
    body = models.TextField()
    image = models.FileField(null=True, blank=True)

    def __str__(self):
        return self.titre


class ArticlesForm(forms.Form):
    titre = forms.CharField()
    body = forms.CharField(widget=forms.Textarea)
    image = forms.FileField()



class Blog(models.Model):
    titre = models.CharField(max_length=255)
    body = models.TextField()
    image = models.ImageField(upload_to="photos/")

    def __str__(self):
        return self.titre