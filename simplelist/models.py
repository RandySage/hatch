from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User
import django_tables2

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

    list = models.ForeignKey(List)
    create_date = models.DateTimeField('date created')
    created_by = models.ForeignKey(User)
    heading_text = models.CharField(max_length=200, blank=True)
    body_text = models.CharField(max_length=2000, blank=True)
    doc_sort_order = models.IntegerField(default=0, null=False)
    def short_text(self):
        if len(self.heading_text):
            return "H: "+self.heading_text[0:Entry.MAX_SHORT_TEXT_LENGTH];
        else:
            return "B: "+self.body_text[0:Entry.MAX_SHORT_TEXT_LENGTH];

    def __unicode__(self):  # Python 3: def __str__(self):
        return self.short_text();

# Attempting to follow http://stackoverflow.com/a/11931849/527489

class EntryTable(django_tables2.Table):
    #actions = EntryActions(orderable=False)
    class Meta:
        model = Entry
        exclude = ('id',)
        attrs = {"class": "paleblue"}

