# coding: utf-8
from datetime import datetime

from django.db import models
from django.core.urlresolvers import reverse

from sorl.thumbnail import ImageField, get_thumbnail
from sorl.thumbnail.helpers import ThumbnailError


class Author(models.Model):
    name = models.CharField(max_length=200)
    short_bio = models.TextField(max_length=500, null=True, blank=True)
    slug = models.SlugField(max_length=100, blank=True)
    uuid = models.CharField(max_length=100, blank=True, null=True)
    avatar = ImageField(upload_to='authors',
                        blank=True,
                        null=True)

    ordering = ['name']

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('author', kwargs={'slug': self.slug})

    def get_avatar(self, size='60x60'):
        try:
            return get_thumbnail(self.avatar,
                                 size,
                                 crop='center',
                                 quality=70).url
        except ThumbnailError:
            return None


class Tag(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, blank=True)
    uuid = models.CharField(max_length=100, blank=True, null=True)

    ordering = ['name']

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('tag', kwargs={'slug': self.slug})


class Quote(models.Model):
        body = models.TextField()
        authors = models.ManyToManyField(Author)
        tags = models.ManyToManyField(Tag, blank=True, null=True)
        slug = models.SlugField(max_length=100, blank=True)
        publish_date = models.DateTimeField(default=datetime.now)
        source = models.TextField(null=True, blank=True)
        featured = models.BooleanField(default=False)
        uuid = models.CharField(max_length=100, blank=True, null=True)

        ordering = ['-publish_date']

        def __unicode__(self):
            return self.body

        def get_absolute_url(self):
            return reverse('quote', kwargs={'uuid': self.uuid})