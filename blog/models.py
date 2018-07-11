from django.db import models


# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Article(models.Model):
    user = models.ForeignKey(User, related_name='articles', on_delete=models.CASCADE)
    text = models.CharField(max_length=2000)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.text
