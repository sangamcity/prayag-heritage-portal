import bleach
from django.utils.html import escape
from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.db.models.signals import post_save, pre_save 

# from videofield.fields import VideoField   

def image_upload_path(instance, filename):
    return 'place_pictures/{0}/{1}'.format(instance.tourism_place.slug, filename)
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>

def video_upload_path(instance, filename):
    return 'place_videos/{0}/{1}'.format(instance.tourism_place.slug, filename)
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>

class Image(models.Model):  
    tourism_place = models.ForeignKey('TourismPlaces.TourismPlace', related_name="image_of" ,null=True, blank=True)
    name          = models.CharField(max_length=200, null=True, blank=True)
    slug          = models.SlugField(unique=True, null=True, blank=True)
    image         = models.ImageField(upload_to=image_upload_path,
                                # format='JPEG',
                                # options={ 'quality': 100},
                                null=True,
                                blank=True,
                                height_field="height_field",
                                width_field="width_field") 
    height_field  = models.IntegerField(default=450)
    width_field   = models.IntegerField(default=350)
    description   = models.TextField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.name  

    #Image_object.image.url (gives absolute url of image of Image_object)

class Video(models.Model):
    tourism_place   = models.ForeignKey('TourismPlaces.TourismPlace', related_name="video_of" ,null=True, blank=True)
    name            = models.CharField(max_length=200, null=True, blank=True)
    slug            = models.SlugField(unique=True,null=True, blank=True)
    video           = models.FileField(upload_to=video_upload_path,
                                # format='JPEG',
                                # options={ 'quality': 100},
                                null=True,
                                blank=True,
                                ) 
    description     = models.TextField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.name  
   

class TourismPlace(models.Model):
    video       = models.ForeignKey(Video, related_name="video_for", null=True, blank=True)
    image       = models.ForeignKey(Image, related_name="image_for", null=True, blank=True)
    name 	    = models.CharField(max_length=200, null=True, blank=True)
    slug        = models.SlugField(unique=True,null=True, blank=True)
    latitude    = models.DecimalField(null = True, blank = True, max_digits=19, decimal_places=10)
    longitude   = models.DecimalField(null = True, blank = True, max_digits=19, decimal_places=10)
    place_type  = models.CharField(max_length=200, null=True, blank=True)
    location    = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(max_length=1500, null=True, blank=True)
    
    def __str__(self):
        return self.name

    def linkfy_post(self):
        return bleach.linkify(escape(self.description)) 

 
class Review(models.Model):
    tourism_place = models.ForeignKey('TourismPlaces.TourismPlace', related_name="review_of" ,null=True, blank=True)
    user          = models.ForeignKey(User, related_name="review_by", null=True, blank=True)
    post          = models.TextField(max_length=255, null=True, blank=True)
    date          = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
    class Meta:
        verbose_name='Reviews_for_Tourism_places'




def create_slug(instance, sender, new_slug=None):
    slug = slugify(instance.name)
    if new_slug is not None:
        slug = new_slug
    if sender == TourismPlace:
        qs = TourismPlace.objects.filter(slug=slug).order_by('-id')
    elif sender == Image:
        qs = Image.objects.filter(slug=slug).order_by('-id')
    elif sender == Video:
        qs = Video.objects.filter(slug=slug).order_by('-id')        
    exists = qs.exists()
    if exists:
        new_slug = '%s-%s'%(slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug


def pre_save_models_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance,sender)


pre_save.connect(pre_save_models_receiver, sender=TourismPlace)
pre_save.connect(pre_save_models_receiver, sender=Image)
pre_save.connect(pre_save_models_receiver, sender=Video)

