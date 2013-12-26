# -*- coding: utf-8 -*-

from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.views import generic


from simplelist.models import List, Entry, EntryTable

class IndexView(generic.ListView):
    template_name = 'simplelist/index.html'
#    model = List
    context_object_name = 'list_of_lists'

    def get_queryset(self):
        """Return the lists."""
        return List.objects.order_by('-create_date')[:]


# Note: There's also a get_list_or_404() function, which works just as
# get_object_or_404() – except using filter() instead of get(). It 
# raises Http404 if the list is empty.
def detail(request, list_id):
    list = get_object_or_404(List, pk=list_id)
    entry_list = list.entry_set.all()
    table = EntryTable(entry_list)
    return render(request, "simplelist/detail.html", {"list_name": list.list_name, "table": table})
    #template_name = 'simplelist/detail.html'

