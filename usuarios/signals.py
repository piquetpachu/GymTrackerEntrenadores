from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from clientes.models import Cliente


@receiver(post_save, sender=User)
def crear_perfil_cliente(sender, instance, created, **kwargs):
    if created and not hasattr(instance, 'perfil_cliente'):
        Cliente.objects.create(usuario=instance, nombre=instance.username)
