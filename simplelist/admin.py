from simplelist.models import List, Entry
from django.contrib import admin
from django.utils import timezone

class ListAdmin:
    fields = ('list_name',)

    def save_model(self, request, obj, form, change):
        obj.created_by = request.user
        obj.create_date = timezone.now()
        obj.save()
    pass

class EntryAdmin:
    fields = ('list', 'heading_text', 'body_text', 'doc_sort_order',)

    def save_model(self, request, obj, form, change):
        obj.created_by = request.user
        obj.create_date = timezone.now()
        obj.save()
    pass

admin.site.register(List, ListAdmin)
admin.site.register(Entry, EntryAdmin)
