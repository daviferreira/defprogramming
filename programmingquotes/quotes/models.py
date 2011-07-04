from django.db import models
from django.core.urlresolvers import reverse

class Author(models.Model):
    name = models.CharField(max_length=200)
    short_bio = models.CharField(max_length=200, null=True, blank=True)
    slug = models.SlugField(max_length=100, blank=True)
    
    def __unicode__(self):
      return self.name
      
    def get_absolute_url(self):
      return reverse('quotes.views.author_detail', kwargs={'slug': self.slug})

class Quote(models.Model):
    body = models.TextField()
    authors = models.ManyToManyField(Author)
    slug = models.SlugField(max_length=100, blank=True)
    
    def __unicode__(self):
      return self.body
      
    def get_absolute_url(self):
      return reverse('quotes.views.detail', kwargs={'slug': self.slug})
      
# signals
from django.db.models import signals
from django.template.defaultfilters import slugify

def author_pre_save(signal, instance, sender, **kwargs):
  instance.slug = slugify(instance.name[0:99])
  
def quote_pre_save(signal, instance, sender, **kwargs):
  instance.slug = slugify(instance.body[0:99])
  
signals.pre_save.connect(author_pre_save, sender=Author)
signals.pre_save.connect(quote_pre_save, sender=Quote)
