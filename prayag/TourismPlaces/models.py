from django.db import models
from django.conf import settings
# Create your models here.

class TourismPlace(models.Model):
    image = models.ForeignKey('TourismPlaces.Image', related_name="image_for", null=True, blank=True)
    name 	= models.CharField(max_length=200, null=True, blank=True)
    location = models.CharField(max_length=200, null=True, blank=True)
    category = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(max_length=1000, null=True, blank=True)
    def __str__(self):
        return self.name
 
 #   def get_image(self): 
  #      image_url = setting.MEDIA_URL+ 'places_pictures' + str(self.image)
  #      return image_url


# """
# main_image 	 = models.ImageField(upload_to='/home/sushant2/projects/djangoprojects/prayag/prayag/prayag/media_root/places_pictures', 


# # format='JPEG',
# # options={ 'quality': 100},
# null=True,
# blank=True,
# height_field="height_field",
# width_field="width_field") 
# height_field = models.IntegerField(default=450)
# width_field = models.IntegerField(default=350)	
# """
class Image(models.Model):
   # tourism_place = models.ForeignKey(TourismPlace, related_name="TourismPlace_for", null=True, blank=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    image   = models.ImageField(upload_to='places_pictures',
                                # format='JPEG',
                                # options={ 'quality': 100},
                                null=True,
                                blank=True,
            height_field="height_field",
            width_field="width_field") 
    height_field = models.IntegerField(default=450)
    width_field = models.IntegerField(default=350)
    def __str__(self):
        return self.name
    #def get_image(self):
     #   image_url = setting.MEDIA_URL+ 'places_pictures' + str(self.image)
    #        return image_url


