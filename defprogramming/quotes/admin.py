# coding: utf-8
from quotes.models import Author, Tag, Quote
from django import forms
from django.contrib import admin


class QuoteAdminForm(forms.ModelForm):
    class Meta:
        model = Quote

    def __init__(self, *args, **kwds):
        super(QuoteAdminForm, self).__init__(*args, **kwds)
        self.fields['authors'].queryset = Author.objects.order_by('name')
        self.fields['tags'].queryset = Tag.objects.order_by('name')


class QuoteAdmin(admin.ModelAdmin):
    list_display = ('id', 'body')
    list_filter = ('authors', 'tags')
    search_fields = ('id', 'body')
    date_hierarchy = 'publish_date'
    ordering = ('-publish_date',)
    form = QuoteAdminForm


class AuthorAdmin(admin.ModelAdmin):
    ordering = ('name',)


admin.site.register(Author, AuthorAdmin)
admin.site.register(Quote, QuoteAdmin)
admin.site.register(Tag)
