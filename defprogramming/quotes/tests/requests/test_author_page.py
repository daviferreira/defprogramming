# coding: utf-8
from lxml import html

from django.test import TestCase
from django.test.client import Client

from quotes.tests.utils import create_test_author


class AuthorPageTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        self.dom = ''
        self.author = create_test_author()

    def tearDown(self):
        self.dom = ''
        self.author = ''

    def __load_dom(self):
        response = self.client.get('/quotes-by/author/')
        self.dom = html.fromstring(response.content)

    def testAuthorPageResponse(self):
        response = self.client.get('/quotes-by/author/')
        self.failUnlessEqual(response.status_code, 200)

    def testAuthorPageShouldHaveTheRightTitle(self):
        self.__load_dom()
        assert self.dom.cssselect('h1.jumbotron')[0].text_content(), self.author.name

    def testAuthorPageShouldListAuthorsQuotes(self):
        self.__load_dom()
        assert len(self.dom.cssselect('.quote-card')), 10