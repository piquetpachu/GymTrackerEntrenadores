from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from clientes.models import Cliente

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def crear_cliente_automatico(sender, instance, created, **kwargs):
    """
    Cuando se crea un usuario con rol 'cliente',
    se crea automáticamente un registro Cliente vinculado.
    """
    if created and instance.rol == "cliente":
        Cliente.objects.create(
            usuario=instance,
            nombre=instance.first_name or instance.username
        )
