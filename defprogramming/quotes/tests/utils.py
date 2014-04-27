# coding: utf-8
from datetime import datetime

from quotes.models import Author, Tag, Quote


def create_test_quote():
    body = 'Test quote'
    now = datetime.now()
    quote = Quote.objects.create(body=body, publish_date=now)
    quote.authors.create(name='Author 1')
    quote.authors.create(name='Author 2')
    quote.tags.create(name='Tag 1')
    quote.tags.create(name='Tag 2')
    return quote


def create_test_author():
    name = 'Author'
    author = Author.objects.create(name=name)
    now = datetime.now()
    for i in xrange(10):
        body = 'Test quote %d' % i
        quote = Quote.objects.create(body=body, publish_date=now)
        quote.authors.add(author)
    return author


def create_test_tag():
    name = 'Tag'
    tag = Tag.objects.create(name=name)
    now = datetime.now()
    for i in xrange(10):
        body = 'Test quote %d' % i
        quote = Quote.objects.create(body=body, publish_date=now)
        quote.tags.add(tag)
    return tag


def create_multiple_test_quotes(ammount=100):
    quotes = []
    for i in xrange(ammount):
        body = 'Test quote %d' % i
        now = datetime.now()
        quote = Quote.objects.create(body=body, publish_date=now)
        quote.authors.create(name='Author 1')
        quote.authors.create(name='Author 2')
        quote.tags.create(name='Tag 1')
        quote.tags.create(name='Tag 2')
        quotes.append(quote)
    return quotes


def create_multiple_test_authors(ammount=100):
    authors = []
    for i in xrange(ammount):
        name = "Author %d" % i
        author = Author.objects.create(name=name)
        authors.append(author)
    now = datetime.now()
    for i in xrange(10):
        body = 'Test quote %d' % i
        quote = Quote.objects.create(body=body, publish_date=now)
        quote.authors.add(authors[0])
    return authors


def create_multiple_test_tags(ammount=100):
    tags = []
    for i in xrange(ammount):
        name = "Tag %d" % i
        tag = Tag.objects.create(name=name)
        tags.append(tag)
    now = datetime.now()
    for i in xrange(10):
        body = 'Test quote %d' % i
        quote = Quote.objects.create(body=body, publish_date=now)
        quote.tags.add(tags[0])
    return tags
