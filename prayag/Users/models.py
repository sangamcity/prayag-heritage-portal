from __future__ import unicode_literals

# import hashlib 
import os.path 
     
from django.conf import settings
from django.contrib.auth.models import User
from django.db import models 
from django.db.models.signals import post_save 
from django.utils.encoding import python_2_unicode_compatible

from django.core.cache import cache   
import datetime

 

@python_2_unicode_compatible      
class Profile(models.Model):     
    user = models.OneToOneField(User)  
    gender = models.CharField(max_length=10, null=True, blank=True)
    image = models.ImageField(upload_to='profile_pictures',
                                # format='JPEG',
                                # options={ 'quality': 100},
                                null=True,
                                blank=True,
            height_field="height_field",
            width_field="width_field")
    height_field = models.IntegerField(default=450)
    width_field = models.IntegerField(default=350)

    class Meta: 
        db_table = 'auth_profile'

    def __str__(self):
        return self.user.username

    def get_picture(self):
        #print('settings.MEDIA_URL,self.image',settings.MEDIA_URL,self.image)
        no_picture = settings.MEDIA_URL + 'profile_pictures/' + 'no_picture.png'
        gender = self.gender
        if self.image:
            return settings.MEDIA_URL+str(self.image)
        elif gender:
            if gender.lower() == 'male':
                return settings.MEDIA_URL + 'profile_pictures/' + 'male.png'
            elif gender.lower() == 'female': 
                return settings.MEDIA_URL + 'profile_pictures/' + 'female.png'
            elif gender == 'Gender':
                return no_picture
        else:
            return no_picture

    def get_screen_name(self): 
        try:
            if self.user.get_full_name():
                return self.user.get_full_name()
            else:
                return self.user.username
        except:
            return self.user.username
            

def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


def save_user_profile(sender, instance, **kwargs):  
    instance.profile.save()

post_save.connect(create_user_profile, sender=User)
post_save.connect(save_user_profile, sender=User)



   



