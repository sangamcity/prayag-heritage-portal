"""prayag URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url 
from django.contrib import admin
from TourismPlaces.views import (
		home, blogList, featuresTypoBasic, featuresTypoBlockquotes,
        featuresLabels, featuresProgessBars, results, layout, weather_results, 
        weather_layout, temp_display, frame
        )
 

urlpatterns = [
    url(r'^sendWeatherRequest/(?P<query>[^/]+)', weather_results, name='weather_results'),
    url(r'^weather_layout/', weather_layout, name='weather_layout'),
    url(r'^sendRequest/(?P<query>[^/]+)', results, name='results'),
    url(r'^frame/', frame, name='frame'),
    url(r'^layout/', layout, name='layout'),
    url(r'^home/', home, name='home'),
    url(r'^temp_display/', temp_display, name='temp_display'),	
    url(r'^bloglist', blogList, name='bloglist'),
    # url(r'^index_page', indexPage, name='index_page'),
    url(r'^features_typo_blockquotes', featuresTypoBlockquotes, name='features_typo_blockquotes'),
    url(r'^features_typo_basic', featuresTypoBasic, name='features_typo_basic'),
    url(r'^features_labels', featuresLabels, name='features_labels'),
    url(r'^features_progess_bars', featuresProgessBars, name='features_progress_bars'),
    url(r'^admin/', admin.site.urls),
]
 