from .models import UserProfile, AdminProfile
from django.contrib.auth.models import User
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver


# Utilizando signals
# De esta manera, cuando creamos una instancia de User, se crea tambien una instancia de Profile asociada a esta

# SIGNALS https://docs.djangoproject.com/en/3.0/topics/signals/#module-django.dispatch

@receiver(post_save, sender=User)
def create_Userprofile(sender, instance, created, **kwargs):

    if ((created) and (instance.is_staff)):
        AdminProfile.objects.create(user=instance)
        print('AdminProfile created')
    else:
        if (created):
            UserProfile.objects.create(user=instance)
            print('UserProfile created')


# forma de conectar el User con el profile
# post_save.connect(create_profile, sender=User)

# @receiver(post_save, sender=User)
# def update_Userprofile(sender, instance, created, **kwargs):

 #   if created == False:
 #     UserProfile.save()
#      print('Userprofile updated')


# post_save.connect(update_profile, sender=User)
