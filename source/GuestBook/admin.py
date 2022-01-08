from django.contrib import admin

# Register your models here.
from GuestBook.models import Guest


class GuestAdmin(admin.ModelAdmin):
    list_display = ['id', 'status', 'author_name', 'created_at']
    list_filter = ['status']
    search_fields = ['status']
    fields = ['status', 'author_name', 'created_at', 'editing_time']
    readonly_fields = ['created_at']


admin.site.register(Guest, GuestAdmin)