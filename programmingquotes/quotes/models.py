from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=200)
    short_bio = models.CharField(max_length=200, null=True, blank=True)
    
    def __unicode__(self):
      return self.name

class Quote(models.Model):
    body = models.TextField()
    authors = models.ManyToManyField(Author)
    
    def __unicode__(self):
      return self.body
