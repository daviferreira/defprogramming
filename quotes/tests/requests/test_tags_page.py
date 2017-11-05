# coding: utf-8
from lxml import html

from django.test import TestCase
from django.test.client import Client

from quotes.tests.utils import create_multiple_test_tags


class TagsPageTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        self.dom = ''

    def tearDown(self):
        self.dom = ''

    def __load_dom(self):
        response = self.client.get('/tags/')
        self.dom = html.fromstring(response.content)

    def testTagsPageResponse(self):
        response = self.client.get('/tags/')
        self.failUnlessEqual(response.status_code, 200)

    def testTagsPageShouldShowTags(self):
        self.tags = create_multiple_test_tags()
        self.__load_dom()
        tags_list = self.dom.cssselect('#tags-list li')
        assert len(tags_list), 100

    def testTagNameShouldHaveQuotesCount(self):
        self.tags = create_multiple_test_tags()
        self.__load_dom()
        assert self.dom.cssselect('#tags-list li a')[0].text_content(), 'Tag 0 (10)'
