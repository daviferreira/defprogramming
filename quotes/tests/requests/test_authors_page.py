# coding: utf-8
from lxml import html

from django.test import TestCase
from django.test.client import Client

from quotes.tests.utils import create_multiple_test_authors


class AuthorsPageTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        self.dom = ''
        self.authors = []

    def tearDown(self):
        self.dom = ''
        self.authors = []

    def __load_dom(self):
        response = self.client.get('/authors/')
        self.dom = html.fromstring(response.content)

    def testAuthorsPageResponse(self):
        response = self.client.get('/authors/')
        self.failUnlessEqual(response.status_code, 200)

    def testAuthorsPageShouldShowAuthors(self):
        self.authors = create_multiple_test_authors()
        self.__load_dom()
        authors_list = self.dom.cssselect('#authors-list li')
        assert len(authors_list), 100

    def testAuthorNameShouldHaveQuotesCount(self):
        self.authors = create_multiple_test_authors()
        self.__load_dom()
        assert self.dom.cssselect('#authors-list li a')[0].text_content(), \
               'Author 0 (10)'