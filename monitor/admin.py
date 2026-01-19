from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Server, Service, Config

# Allow editing services directly from the server page, very useful
class ServiceInline(admin.TabularInline):
    model = Service
    extra = 1 # extra row at the end


class ServerAdmin(admin.ModelAdmin):
    list_display = ('name', 'ip_address', 'owner')
    inlines = [ServiceInline]


class ConfigAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        # If 1 config exists, don't allow adding more
        if Config.objects.exists():
            return False
        return True


admin.site.register(Server, ServerAdmin)
admin.site.register(Config, ConfigAdmin)

# Groups are not used
admin.site.unregister(Group)