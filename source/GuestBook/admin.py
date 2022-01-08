from django.contrib import admin

# Register your models here.
from GuestBook.models import Guest


class GuestAdmin(admin.ModelAdmin):
    list_display = ['id', 'status', 'author_name', 'created_at']
    list_filter = ['status']
    search_fields = ['status']
    fields = ['author_name', 'author_mail', 'text_notes']
    readonly_fields = ['created_at']


admin.site.register(Guest, GuestAdmin)