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
from django.conf.urls import url,include   
from django.contrib import admin  
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static    
from django.conf import settings
from django.views.static import serve

from TourismPlaces.views import (
		home, results, layout, weather_results,   
        weather_layout, contact, about, acknowledge,
        place_detail, img_show, video_show,  search,
        img_show_all, video_show_all, temp_events,
        explore_place, optimal_dist, maps_distance, history,
        views_360, coming_soon, stay_visit,
        )

from Users.views import (
        signup,profile, change_password, feedback, post_review,
    )

# from django.contrib.auth.views import ( 
#     password_reset,
#     password_reset_done, 
#     password_reset_confirm,    
#     password_reset_complete,     
#     )   

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^cooladmins/home/', admin.site.urls),

    url(r'^weather_layout/', weather_layout, name='weather_layout'),
    url(r'^sendRequest/(?P<query>[^/]+)/', results, name='results'),
    url(r'^layout/', layout, name='layout'),  
    url(r'^sendWeatherRequest/(?P<query>[^/]+)', weather_results, name='weather_results'),

    #All_img and all_video show
    url(r'^place_detail/(?P<place_slug>[^/]+)/$', place_detail, name='place_detail'), 
    url(r'^img_show/(?P<place_slug>[^/]+)/', img_show, name='img_show'),
    url(r'^video_show/(?P<place_slug>[^/]+)/', video_show, name='video_show'),
    url(r'^img_show_all/', img_show_all, name='img_show_all'),
    url(r'^video_show_all/', video_show_all, name='video_show_all'),

    #interactions
    url(r'^contact/', contact, name='contact'),
    url(r'^acknowledge/', acknowledge, name='acknowledge'),
    url(r'^about/', about, name='about'),
    url(r'^feedback/$', feedback, name='feedback'),
    url(r'^review/$', post_review, name='post_review'),
    
    #registration
    url(r'^signup/', signup, name='signup'),
    url(r'^login', auth_views.LoginView.as_view(), {'template_name': 'login.html'}, name='login'),   
    url(r'^logout', auth_views.LogoutView.as_view(), {'next_page': '/'}, name='logout'),

    # url(r'^passwordreset/$', password_reset, name='password_reset'),
    # url(r'^passwordreset/done/$', password_reset_done, name='password_reset_done'),
    # url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
    #             password_reset_confirm, name='password_reset_confirm'),
    # url(r'^reset/done/$', password_reset_complete, name='password_reset_complete'),
    # url(r'^settings/password/$', change_password, name='change_password'),

    url(r'^profile/$', profile, name='profile'),
    url(r'^search/$', search, name='search'),
   
    #Sessional links
    url(r'^explore/(?P<place_type>[^/]+)/$', explore_place, name='explore'),        
    url(r'^magh_fair/$', temp_events, name='temp_event'),        
    
    #map_related    
    url(r'^optimal_distance/$', optimal_dist, name='optimal_distance'),  
    url(r'^maps_distance/$', maps_distance, name='maps_distance'),       

    url(r'^history/$', history, name='history'),

    url(r'^views_360/$', views_360, name='views_360'),

    #coming_soon
    url(r'^coming_soon/$', coming_soon, name='coming_soon'),   

    #Stay&Visit
    url(r'^stay_visit/$', stay_visit, name='stay_visit'),   
   
    url(r'^i18n/', include(('django.conf.urls.i18n','i18n'))),
    # url(r'^translate/', include('rosetta.urls'))
    url(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
   