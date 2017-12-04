from django.contrib import admin

# Register your models here.

from .models import TourismPlace, Image

class TourismPlaceModelAdmin(admin.ModelAdmin):
 	list_display = ["name","location"]
# 	list_display_link = ["user"]
#	list_editables = ["url"]
 	# list_filter = ["location","job_title"] 
# 	# search_fields = ["location","user"]
 	class Meta:
 		model = TourismPlace

admin.site.register(TourismPlace, TourismPlaceModelAdmin)
 

from .models import Image

class ImageModelAdmin(admin.ModelAdmin):
 	list_display = ["image"]
# 	list_display_link = ["user"]
# 	list_editables = ["url"]
# 	# list_filter = ["location","job_title"]
# 	# search_fields = ["location","user"]
 	class Meta:
 		model = Image

admin.site.register(Image, ImageModelAdmin)
  