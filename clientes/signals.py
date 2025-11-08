from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from clientes.models import Cliente

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def crear_perfil_cliente(sender, instance, created, **kwargs):
    """Crea automáticamente un perfil Cliente si el usuario tiene rol 'cliente'."""
    if created and getattr(instance, "rol", None) == "cliente":
        Cliente.objects.create(usuario=instance, nombre=instance.username)
