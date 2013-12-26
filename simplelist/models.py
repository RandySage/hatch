from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User

import datetime
from django.utils import timezone

class List(models.Model):
    list_name = models.CharField(max_length=200)
    create_date = models.DateTimeField('date created')
    created_by = models.ForeignKey(User)
    # This function is maintained only as a template for later functions
    def __unicode__(self):  # Python 3: def __str__(self):
        return self.list_name

class Entry(models.Model):
    MAX_SHORT_TEXT_LENGTH = 55;

    ## TODO - rename each of the following to its 'verbose' name
    doc_sort_order = models.IntegerField(default=0, null=False, verbose_name='Sort')
    heading_text = models.CharField(max_length=200, blank=True, verbose_name='Concept')
    body_text = models.CharField(max_length=2000, blank=True, verbose_name='Description')
    create_date = models.DateTimeField('date created')
    created_by = models.ForeignKey(User)
    list = models.ForeignKey(List)
    def short_text(self):
        if len(self.heading_text):
            return "H: "+self.heading_text[0:Entry.MAX_SHORT_TEXT_LENGTH];
        else:
            return "B: "+self.body_text[0:Entry.MAX_SHORT_TEXT_LENGTH];

    def __unicode__(self):  # Python 3: def __str__(self):
        return self.short_text();


## TODO: move this to a tables.py

# # Attempting to follow http://django-tables2.readthedocs.org/en/latest/
# import django_tables2 as tables
# from django_tables2.utils import A  # alias for Accessor
# class EntryTable(tables.Table):
#     name = tables.LinkColumn('simplelist.entry_detail', args=[A('pk')])
#     class Meta:
#         model = Entry
#         #exclude = ('id',)
#         attrs = {"class": "paleblue"}

# Attempting to follow http://stackoverflow.com/a/11931849/527489
import django_tables2 as tables
class EntryTable(tables.Table):
    DetailsLink = tables.TemplateColumn(template_name='simplelist/entry_detail_link.html')
    # View = tables.TemplateColumn(verbose_name=_('Details'),
    #                              template_name='simplelist/entry_detail_link.html',
    #                              sortable=False)
    class Meta:
        model = Entry
        exclude = ('id','list',)
        attrs = {"class": "paleblue"}

