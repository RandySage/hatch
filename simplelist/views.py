# -*- coding: utf-8 -*-

from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.views import generic


from simplelist.models import Collection, Entry, EntryForm

class IndexView(generic.CollectionView):
    template_name = 'simplelist/index.html'
#    model = Collection
    context_object_name = 'collection_list'

    def get_queryset(self):
        """Return the collections."""
        return Collection.objects.order_by('-create_date')[:]


# Note: There's also a get_collection_or_404() function, which works just as
# get_object_or_404() – except using filter() instead of get(). It 
# raises Http404 if the collection is empty.
class DetailView(generic.DetailView):
    model = Collection
    template_name = 'simplelist/detail.html'

class ResultsView(generic.DetailView):
    model = Collection
    template_name = 'simplelist/results.html'

def form_view(request, collection_id): 
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

def vote(request, collection_id): 
    return HttpResponse("You're voting on collection %s." % collection_id)
