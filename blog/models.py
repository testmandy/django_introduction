from django.db import models

# Create your models here.


class Article(models.Model):
    article_id = models.AutoField(primary_key=True)
    title = models.TextField()
    content = models.TextField()
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Bug(models.Model):
    bug_id = models.AutoField(primary_key=True)
    title = models.TextField()
    content = models.TextField()
    state = models.BooleanField()
    owner = models.TextField()
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


