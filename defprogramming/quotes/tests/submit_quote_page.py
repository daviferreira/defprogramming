# coding: utf-8
from lxml import html

from django.test import TestCase
from django.test.client import Client

from utils import create_test_tag


class testSubmitQuotePage(TestCase):

    def setUp(self):
        self.client = Client()
        self.dom = ''
        self.tag = create_test_tag()

    def tearDown(self):
        self.dom = ''
        self.tag = ''

    def __load_dom(self):
        response = self.client.get('/submit/')
        self.dom = html.fromstring(response.content)

    def testSubmitQuotePageResponse(self):
        response = self.client.get('/submit/')
        assert response.status_code, 200

    def testSubmitQuotePageShouldHaveTheRightTitle(self):
        self.__load_dom()
        assert self.dom.cssselect('h1')[0].text, 'Submit Quote'

    def testSubmitQuotePageShouldHaveLinkToGoBackToTheHomePage(self):
        self.__load_dom()
        home_link = self.dom.cssselect('p.back a')
        assert len(home_link), 1
        assert home_link[0].text, '&larr; go back to the home page'
        assert home_link[0].attrib['href'], '/'

    def testSubmitQuotePageShouldHaveAFormToSubmitQuotes(self):
        self.__load_dom()
        form = self.dom.cssselect('div.box form')
        assert len(form), 1
        assert form[0].attrib['action'], '/submit/'
        assert len(self.dom.cssselect('div.box form input[type="text"][name="name"]')), 1
        assert len(self.dom.cssselect('div.box form input[type="text"][name="email"]')), 1
        assert len(self.dom.cssselect('div.box form input[type="text"][name="source"]')), 1
        assert len(self.dom.cssselect('div.box form input[type="text"][name="authors"]')), 1
        assert len(self.dom.cssselect('div.box form input[type="text"][name="tags"]')), 1
        assert len(self.dom.cssselect('div.box form textarea[name="quote"]')), 1
        assert len(self.dom.cssselect('div.box form input[type="submit"]')), 1

    def testUserShouldBeAbleToSubmitQuoteWithPOST(self):
        self.__load_dom()
        response = self.client.post('/submit/')
        assert response.status_code, 200

    def testFormSubmittedWithInvalidDataShouldDisplayErrors(self):
        response = self.client.post('/submit/')
        self.dom = html.fromstring(response.content)
        assert len(self.dom.cssselect('ul.errorlist')), 6

    def testFormSubmittedWithInvalidEmailShouldDisplayError(self):
        response = self.client.post('/submit/', {
            'name': 'Foo Bar',
            'email': 'invalid e-mail',
            'quote': 'This is a test quote',
            'authors': 'Author 1',
            'tags': 'Tag 1',
            'source': 'www.defprogramming.com',
        })
        self.dom = html.fromstring(response.content)
        errorlist = self.dom.cssselect('ul.errorlist li')
        assert len(errorlist), 1
        assert errorlist[0].text, 'Enter a valid e-mail address.'

    def testFormSubmittedWithValidDataShouldDisplaySuccessMessage(self):
        response = self.client.post('/submit/', {
            'name': 'Foo Bar',
            'email': 'foo@bar.com',
            'quote': 'This is a test quote',
            'authors': 'Author 1',
            'tags': 'Tag 1',
            'source': 'www.defprogramming.com',
        })
        self.dom = html.fromstring(response.content)
        assert self.dom.cssselect('p.success')[0].text, 'Your quote was successfully submitted, thank you! :-)'

    def testFormSubmittedWithValidDataShouldSendQuoteByEmail(self):
        self.client.post('/submit/', {
            'name': 'Foo Bar',
            'email': 'foo@bar.com',
            'quote': 'This is a test quote',
            'authors': 'Author 1',
            'tags': 'Tag 1',
            'source': 'www.defprogramming.com',
        })
        pass
