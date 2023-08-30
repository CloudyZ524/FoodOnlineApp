from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from .models import User, UserProfile


# connect the saver to the receiver
@receiver(post_save, sender=User)
def post_save_create_profile_receiver(sender, instance, created, **kwargs):   # post save signal function
    print(created)
    if created:
        UserProfile.objects.create(user=instance)
    else:  # update cases
        try:
            profile = UserProfile.objects.get(user=instance)
            profile.save()
        except:
            # create the userProfile if not exits
            UserProfile.objects.create(user=instance)


@receiver(pre_save, sender=User)
def pre_save_profile_receiver(sender, instance,  **kwargs):
    print(instance.username, 'This user is saved')
