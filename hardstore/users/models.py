from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
	usuario = models.OneToOneField(User , null = True , on_delete = models.CASCADE)
	f_creacion = models.DateTimeField(auto_now_add = True ,null = True)
	birth_date = models.DateField(null=True, blank=True)
	

	#def __str__(self):
	#	return self.usuario.User.first_name +' '+ self.usuario.last_name
		
#Now this is where the magic happens: we will now define signals so 
#our Profile model will be automatically created/updated when we create/update User instances.

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
	if created:
		Profile.objects.create( user=instance )

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
	instance.profile.save()