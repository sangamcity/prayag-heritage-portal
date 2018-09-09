from django.contrib import admin

# Register your models here.

from .models import TourismPlace, Image, Video, Review

class TourismPlaceModelAdmin(admin.ModelAdmin):
	list_display = ["name","location"]
# 	list_display_link = ["user"]
#	list_editables = ["url"]
 	# list_filter = ["location","job_title"] 
	search_fields = ["name","description"]
	class Meta:
		model = TourismPlace

 

# from .models import Image

class ImageModelAdmin(admin.ModelAdmin):
	list_display = ["name"]
# 	list_display_link = ["user"]
# 	list_editables = ["url"]
# 	# list_filter = ["location","job_title"]
	search_fields = ["name","description"]
	class Meta:
		model = Image

  

class VideoModelAdmin(admin.ModelAdmin):
	list_display = ["name"]
# 	list_display_link = ["user"]
# 	list_editables = ["url"]
# 	# list_filter = ["location","job_title"]
	search_fields = ["name","description"]
	class Meta:
		model = Video

class ReviewModelAdmin(admin.ModelAdmin):
	list_display = ["post"]
# 	list_display_link = ["user"]
# 	list_editables = ["url"]
# 	# list_filter = ["location","job_title"]
	search_fields = ["post"]
	class Meta:
		model = Review



admin.site.register(TourismPlace, TourismPlaceModelAdmin)
admin.site.register(Image, ImageModelAdmin)
admin.site.register(Video, VideoModelAdmin)
admin.site.register(Review, ReviewModelAdmin)