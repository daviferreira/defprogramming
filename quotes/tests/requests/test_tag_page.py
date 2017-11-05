# coding: utf-8
from lxml import html

from django.test import TestCase
from django.test.client import Client

from quotes.tests.utils import create_test_tag


class TagPageTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        self.dom = ''
        self.tag = create_test_tag()

    def tearDown(self):
        self.dom = ''
        self.tag = ''

    def __load_dom(self):
        response = self.client.get('/quotes-tagged-with/tag/')
        self.dom = html.fromstring(response.content)

    def testTagPageResponse(self):
        response = self.client.get('/quotes-tagged-with/tag/')
        self.failUnlessEqual(response.status_code, 200)

    def testTagPageShouldHaveTheRightTitle(self):
        self.__load_dom()
        assert self.dom.cssselect('h1')[0].text_content(), 'Quotes by Tag'

    def testTagPageShouldListTagsQuotes(self):
        self.__load_dom()
        assert len(self.dom.cssselect('div.quote-card')), 10