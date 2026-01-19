from django.db import models

class Config(models.Model):
    refresh_seconds = models.IntegerField(default=30, verbose_name="Intervallo di aggiornamento in secondi")

    def __str__(self):
        return f"Configurazione intervallo di aggiornamento di {self.refresh_seconds} s"

    class Meta:
        verbose_name = "Configuration"


class Server(models.Model):
    name = models.CharField(max_length=100)
    ip_address = models.GenericIPAddressField()
    owner = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} ({self.ip_address})"


# Services associated to a server and checked by port
class Service(models.Model):
    server = models.ForeignKey(Server, on_delete=models.CASCADE, related_name='services')
    name = models.CharField(max_length=20, verbose_name="Nome Servizio")
    port = models.IntegerField(verbose_name="Porta")

    def __str__(self):
        return f"{self.name} ({self.port})"