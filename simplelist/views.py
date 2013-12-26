# -*- coding: utf-8 -*-

from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.views import generic


from simplelist.models import List, Entry, EntryForm

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
class DetailView(generic.DetailView):
    model = List
    template_name = 'simplelist/detail.html'

class ResultsView(generic.DetailView):
    model = List
    template_name = 'simplelist/results.html'

def form_view(request, list_id): 
    if request.method == 'POST': # If the form has been submitted...
        form = EntryForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
            # ...
            return HttpResponseRedirect('/thanks/') # Redirect after POST
    else:
        form = EntryForm() # An unbound form

    return render(request, 'simplelist/results.html', {
        'form': form,
    })

def vote(request, list_id): 
    return HttpResponse("You're voting on list %s." % list_id)
