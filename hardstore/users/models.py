from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

from django.db.models.signals import post_save
from django.dispatch import receiver

class UserProfile(models.Model):
	user = models.OneToOneField(User , null = True , on_delete = models.CASCADE, related_name='profile')
	f_creacion = models.DateTimeField(auto_now_add = True ,null = True)
	birth_date = models.DateField(null=True, blank=True)
	
	def __str__(self):
		return self.user.username

#Utilizando signals
#De esta manera, cuando creamos una instancia de User, se crea tambien una instancia de Profile asociada a esta 
	@receiver(post_save, sender=User)
	def update_profile_signal(sender, instance, created, **kwargs):
		if (created):
			UserProfile.objects.create(user=instance)

#instance.Userprofile.save()

	#def __str__(self):
	#	return self.usuario.User.first_name +' '+ self.usuario.last_name
		
#Now this is where the magic happens: we will now define signals so 
#our Profile model will be automatically created/updated when we create/update User instances.

#@receiver(post_save, sender=User)
#def create_user_profile(sender, instance, created, **kwargs):
	if created:
		Profile.objects.create( user=instance )

#@receiver(post_save, sender=User)
#def save_user_profile(sender, instance, **kwargs):
	instance.profile.save()