from simplelist.models import Collection, Entry
from django.contrib import admin
from django.utils import timezone

class CollectionAdmin:
    fields = ('collection_name',)

    def save_model(self, request, obj, form, change):
        obj.created_by = request.user
        obj.create_date = timezone.now()
        obj.save()
    pass

class EntryAdmin:
    fields = ('collection', 'heading_text', 'body_text', 'doc_sort_order',)

    def save_model(self, request, obj, form, change):
        obj.created_by = request.user
        obj.create_date = timezone.now()
        obj.save()
    pass

admin.site.register(Collection, CollectionAdmin)
admin.site.register(Entry, EntryAdmin)
