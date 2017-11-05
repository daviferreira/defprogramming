# coding: utf-8
import uuid

from django.db.models import signals
from django.template.defaultfilters import slugify

from .models import Author, Quote, Tag


def author_pre_save(signal, instance, sender, **kwargs):
    if not instance.uuid:
        instance.uuid = uuid.uuid4().hex[:12]
    instance.slug = slugify(instance.name[:99])


def quote_pre_save(signal, instance, sender, **kwargs):
    if not instance.uuid:
        instance.uuid = uuid.uuid4().hex[:12]
    instance.slug = slugify(instance.body[:99])


def tag_pre_save(signal, instance, sender, **kwargs):
    if not instance.uuid:
        instance.uuid = uuid.uuid4().hex[:12]
    instance.slug = slugify(instance.name[:99])


signals.pre_save.connect(author_pre_save, sender=Author)
signals.pre_save.connect(quote_pre_save, sender=Quote)
signals.pre_save.connect(tag_pre_save, sender=Tag)