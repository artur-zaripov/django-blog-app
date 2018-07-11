from django.db import models
from django.contrib.auth.models import User


class Article(models.Model):
    user = models.ForeignKey(User, related_name='articles', on_delete=models.CASCADE)
    text = models.CharField(max_length=2000)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.text
