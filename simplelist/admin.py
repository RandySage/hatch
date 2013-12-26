from simplelist.models import List, Entry
from django.contrib import admin
from django.utils import timezone

class ListAdmin(admin.ModelAdmin):
    exclude = ('created_by','create_date',)

    def save_model(self, request, obj, form, change):
        obj.created_by = request.user
        obj.create_date = timezone.now()
        obj.save()


class EntryAdmin(admin.ModelAdmin):
    exclude = ('created_by','create_date',)
    #fields = ('list', 'heading_text', 'body_text', 'doc_sort_order',)

    def save_model(self, request, obj, form, change):
        obj.created_by = request.user
        obj.create_date = timezone.now()
        obj.save()


admin.site.register(List, ListAdmin)
admin.site.register(Entry, EntryAdmin)
