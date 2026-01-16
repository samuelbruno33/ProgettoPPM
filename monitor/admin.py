from django.contrib import admin
from .models import Server

# This class customizes how the list looks in the Admin panel
class ServerAdmin(admin.ModelAdmin):
    list_display = ('name', 'ip_address', 'owner', 'is_online', 'last_checked')
    #list_filter = ('is_online', 'owner')
    #search_fields = ('name', 'ip_address')

admin.site.register(Server, ServerAdmin)