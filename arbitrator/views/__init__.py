from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from arbitrator.models import ArbitratorUser


@receiver(post_save, sender=User)
def dispatch(sender, instance: User, created, **kwargs):
    if created:
        try:
            existing_user = ArbitratorUser.objects.get(user=instance)

        except ArbitratorUser.DoesNotExist:
            new_user = ArbitratorUser(user=instance)
            new_user.save()