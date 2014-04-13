from django import forms
from django.core.mail import send_mail
from django.conf import settings


class QuoteForm(forms.Form):
    name = forms.CharField(label='Your name', max_length=50)
    email = forms.EmailField(label='Your e-mail')
    quote = forms.Field(label='Quote', widget=forms.Textarea)
    authors = forms.CharField(label='Authors, separated by commas')
    tags = forms.CharField(label='Tags, separated by commas')
    source = forms.CharField(label='Source (website, book etc.)')

    def save(self, data):
            message = "%s\n\nFrom: %s <%s>\nAuthors: %s\n" \
                      "Tags: %s\nSource: %s\n" % (data.get('quote'),
                                                  data.get('name'),
                                                  data.get('email'),
                                                  data.get('authors'),
                                                  data.get('tags'),
                                                  data.get('source'))

            send_mail('[defprogramming] New quote', message, data.get('email'),
                      [settings.SERVER_EMAIL], fail_silently=False)
