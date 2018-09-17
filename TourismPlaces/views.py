from django.shortcuts import get_object_or_404, redirect, render
from django.http import JsonResponse
from TourismPlaces.models import TourismPlace, Image, Video, Review
from prayag.decorators import ajax_required
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseBadRequest
import json
import requests  
import datetime 


temp_f = ""
search_url = "https://maps.googleapis.com/maps/api/place/textsearch/json"
details_url = "https://maps.googleapis.com/maps/api/place/details/json"

# Create your views here. 
  
def home(request):
	page_quote = 'Immerse yourself in some of the inspiring destinations in Allahabad'
	page_quote = page_quote.upper()
	page_user = request.user    
	tourism_places = TourismPlace.objects.all().filter(place_type__contains='front')[:4]  
	print(len(tourism_places))
	#images = Image.objects.all()
	return render(request, 'prayag/home.html', {  
			'tourism_places': tourism_places, 
			'page_user': page_user,
			'page_quote' : page_quote,
			})
    
def place_detail(request, place_slug):
	all_reviews = Review.objects.all().filter(tourism_place__slug=place_slug)
	videos = Video.objects.all().filter(tourism_place__slug=place_slug)
	related_images = Image.objects.all().filter(tourism_place__slug=place_slug)[:4]
	place = get_object_or_404(TourismPlace, slug=place_slug)
	# if place: print(place.image.image.url)
	if videos: video = videos[0]
	else: video = []
	return render(request, 'place_detail.html', {
			'place':place, 
			'related_images':related_images, 
			'video':video,
			'all_reviews': all_reviews,
			})  

def views_360(request):
	return render(request, 'views_360.html', {})   #login_view


def img_show(request, place_slug): 
	place = get_object_or_404(TourismPlace, slug=place_slug)
	related_images = Image.objects.all().filter(tourism_place__slug=place_slug)
	return render(request, 'img_show.html', { 'place': place, 'related_images': related_images })

def video_show(request, place_slug):
	related_videos = Video.objects.all().filter(tourism_place__slug=place_slug)
	place = get_object_or_404(TourismPlace, slug=place_slug)
	# related_images = Image.objects.all().filter(tourism_place__name=place_name)[4:]	
	return render(request, 'video_show.html', { 'place': place, 'related_videos': related_videos })

def img_show_all(request): 
	related_images = Image.objects.all().filter()
	return render(request, 'img_show_all.html', {'related_images': related_images })

def video_show_all(request):
	related_videos = Video.objects.all().filter()
	# related_images = Image.objects.all().filter(tourism_place__name=place_name)[4:]	
	return render(request, 'video_show_all.html', { 'related_videos': related_videos })



@ajax_required
def search(request):
    print('came inside search')  
    places = TourismPlace.objects.all()
    dump = []
    template = '<a href="/place_detail/'+ '{2}' +'/" style="text-decoration:none;">'+'<img src="'+ '{0}' +'" style="max-height:25px; max-width:25px;">  <span style="color:black;">{1}</span>\
      '+'</a>'
    # template = '<a href="/place_detail/'+ '{2}' +'/" style="text-decoration:none;">'+'<img src="'+ '{0}' +'" style="max-height:40px; max-width:40px;min-height:40px; min-width:40px; float:left;"><span style="color:purple; font-size:14px; float:right;">{1}</span>\
    # ' +'</a>'

    for place in places:
        try:
            dump.append(template.format(place.image.image.url, 'Welcome in '+place.name,
                                    place.slug))           
        except AttributeError:
            pass
        # if user.username != request.user.username:
        #     dump.append(template.format(user.profile.get_screen_name(),
        #                                 user.username))
        # else:
    data = json.dumps(dump)
    return HttpResponse(data, content_type='application/json')


def contact(request):
	page_quote = 'Some Quotation'
	return render(request, 'contact.html', {
		'page_quote' : page_quote,
		})

def acknowledge(request):
	page_quote = 'Some Quotation'
	return render(request, 'acknowledge.html', {
		'page_quote' : page_quote,
		})

def about(request):
	page_quote = page_quote
	return render(request, 'about.html', {
			'page_quote' : page_quote,
		})

def layout(request):
	return render(request, "layout.html", {}) # empty dictionary

def results(request, query):
	print (query)
	key = 'AIzaSyAJWFjIVM-voIy9yQw_3mGe50lJJsJyjP8'
	search_payload = {"key":key, "query":query}
	# search_temp = requests.post("https://github.com/timeline.json")
	print (search_payload)
	search_req = requests.get(search_url, params=search_payload)
	print ("sushant")
	search_json = search_req.json()
	print ("sushant")
	print(search_json)
	place_id = search_json["results"][0]["place_id"]

	details_payload = {"key":key, "placeid":place_id}
	details_resp = requests.get(details_url, params=details_payload)
	details_json = details_resp.json()

	url = details_json["result"]["url"]
	return JsonResponse({'result' : url})

def weather_layout(request):
	return render(request, "google_weather.html", {}) # empty dictionary
	

# sessional_ views

#__contains == case sensitive
#__icontains == dont match case

def explore_place(request, place_type):
	place_type = place_type
	related_places = TourismPlace.objects.all().filter(place_type__contains=place_type)
	related_place_videos = Video.objects.all().filter(tourism_place__place_type__contains=place_type)
	video_count = len(related_place_videos)
	return render(request, 'explore/explore_place.html', { 
			'related_places':related_places, 
			'place_type':place_type,
			'video_count' : video_count,
			 })

def weather_results(request, query):
    # print (query)
    key = 'dcdff188d0ebcd4c1ecee4fa0a6be769'
    r = requests.get('http://api.openweathermap.org/data/2.5/weather?q='+query+',in&appid='+key+'')
    json_object = r.json()
    # print(json_object)
    temp_weather = json_object['weather'][0]['main']
    temp_k = float(json_object['main']['temp'])
    # global temp_f
    temp_f = (temp_k - 273.15) * 1.8 
    temp_f *= 5.0
    temp_f /= 9.0
    # print(temp_weather)
    # print(temp_f)
    others = str(json_object['main']['pressure'])
    others = others + " " + str(json_object['main']['humidity'])
    others = others + " " + str(json_object['wind']['speed'])
    return JsonResponse({'weather' : temp_weather, 'temp' : temp_f, 'others' : others,}) 

def optimal_dist(request):
    return render(request, "min-dist.html", {}) # empty dictionary

def maps_distance(request):
    return render(request, "maps_distance.html", {}) # empty dictionary

def history(request):
    return render(request, 'allahabad/history_alld.html', {})

def coming_soon(request):
	today = datetime.date.today()
	now = datetime.datetime.now()
	magh_date = datetime.date(2018, 1, 21)
	remaining = magh_date - today
	print(remaining.days)
	return render(request, 'coming_soon/coming_soon.html', {'remaining':remaining})

def stay_visit(request):
    return render(request, 'coming_soon/coming_soon.html', {})

def temp_events(request):
	place = TourismPlace.objects.all().filter(place_type__contains="magh_mela_main")[0]
	print(place.name)
	related_images = Image.objects.all().filter(tourism_place__place_type__contains="magh_mela")
	return render(request, 'temp_events/magh_fair.html', {
		'related_images' : related_images,
		'place' : place
		});

