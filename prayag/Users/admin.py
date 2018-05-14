from django.contrib import admin

# Register your models here.


from .models import Profile

# class ProfileModelAdmin(admin.ModelAdmin):
# 	list_display = ["job_title","location","user"]
# 	list_display_link = ["user"]
# 	list_editables = ["url"]
# 	# list_filter = ["location","job_title"]
# 	# search_fields = ["location","user"]
# 	class Meta:
# 		model = Profile
 
admin.site.register(Profile)
