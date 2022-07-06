from mailbox import NoSuchMailboxError
from django.db import models

# Create your models here.
class comidas(models.Model):
    nombre = models.CharField(max_length=30)
    precio = models.FloatField()

    class meta:
        verbose_name = 'comida'
        verbose_name_plural= 'comidas'

    def __str__(self):
        return self.nombre