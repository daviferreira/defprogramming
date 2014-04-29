# coding: utf-8
from lxml import html

from django.test import TestCase
from django.test.client import Client

from quotes.tests.utils import create_test_quote


class HomePageTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        self.quote = create_test_quote()
        self.dom = ''
        self.quotes = []

    def tearDown(self):
        self.quote = ''
        self.dom = ''
        self.quotes = []

    def __load_dom(self):
        response = self.client.get('/')
        self.dom = html.fromstring(response.content)

    def testHomePageResponse(self):
        response = self.client.get('/')
        self.failUnlessEqual(response.status_code, 200)

    def testHomePageShouldHaveTheRightTitle(self):
        self.__load_dom()
        assert self.dom.cssselect('h1 a')[0].text_content(), 'def programming'

    def testHomePageShouldListQuotes(self):
        self.__load_dom()
        assert len(self.dom.cssselect('div.quote-card')), 1
        assert self.dom.cssselect('div.quote-card q')[0].text_content(), self.quote.body
        assert self.dom.cssselect('div.quote-card .quote-card-author')[0].text_content(), 'Author 1 & Author 2'
        assert self.dom.cssselect('div.quote-card .quote-card-tags')[0].text_content(), 'tagged under Tag 1, Tag 2'
        # assert self.dom.cssselect('div.quote-card q a')[0].attrib['href'], ("/q/%s/" % self.quote.uuid)

    # TODO: not a home page test, more like a site test
    # should also test for footer links
    def testHomePageShouldShowMenu(self):
        self.__load_dom()
        menu_links = self.dom.cssselect('header nav a')
        assert len(menu_links), 6
        assert menu_links[0].text_content(), 'Home'
        assert menu_links[0].attrib['href'], '/'
        assert menu_links[1].text_content(), 'Authors'
        assert menu_links[1].attrib['href'], '/authors'
        assert menu_links[2].text_content(), 'Tags'
        assert menu_links[2].attrib['href'], '/tags'
        assert menu_links[3].text_content(), 'Random'
        assert menu_links[3].attrib['href'], '/random'
        assert menu_links[4].text_content(), 'Submit'
        assert menu_links[4].attrib['href'], '/submit'