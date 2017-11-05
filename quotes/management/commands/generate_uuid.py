# coding: utf-8
import uuid

from django.core.management.base import BaseCommand
from quotes.models import Quote, Author, Tag


class Command(BaseCommand):
    help = 'Generates unique hashes for quotes, tags and authors'

    def handle(self, *args, **options):
        models = [Quote, Author, Tag]
        for model in models:
            self.stdout.write('Generating hashes for %s' % model)
            items = model.objects.all()
            for item in items:
                self.stdout.write('Generating hashes for %s, item %d' %
                                  (model, item.id))
                item.uuid = uuid.uuid4().hex[:12]
                item.save()

        self.stdout.write('Successfully generated hashes for quotes models')