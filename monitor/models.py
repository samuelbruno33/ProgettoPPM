from django.db import models

class Server(models.Model):
    # Server identification
    name = models.CharField(max_length=100, help_text="Name of the server")
    ip_address = models.GenericIPAddressField(help_text="IP Address")
    owner = models.CharField(max_length=100, help_text="Owner for this server")
    
    ports_to_check = models.CharField(max_length=200, blank=True, null=True, help_text="Ports")

    # Status fields
    is_online = models.BooleanField(default=False)
    last_checked = models.DateTimeField(auto_now=True)

    def __str__(self):
        # Displays the name in the Admin panel
        return f"{self.name} ({self.ip_address})"