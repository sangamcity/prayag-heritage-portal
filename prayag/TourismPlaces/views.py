from django.shortcuts import render
from django.http import JsonResponse
from TourismPlaces.models import TourismPlace

import requests

temp_f = ""
search_url = "https://maps.googleapis.com/maps/api/place/textsearch/json"
details_url = "https://maps.googleapis.com/maps/api/place/details/json"

# Create your views here.

def home(request):
	tourism_places = TourismPlace.objects.all()
	#images = Image.objects.all()
	return render(request, 'index.html', {'tourism_places':tourism_places})
 
def blogList(request):
	return render(request, 'blog-list.html', {})
	
def frame(request):
 	return render(request, 'frame.html', {})

def featuresTypoBlockquotes(request):
	return render(request, 'features-typo-blockquotes.html', {})	

def featuresTypoBasic(request):
	return render(request, 'features-typo-basic.html', {})		

def featuresLabels(request):
	return render(request, 'features-labels.html', {})
		
def featuresProgessBars(request):
	return render(request, 'features-progress-bars.html', {})

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
def temp_display(request):
	global temp_f
	return render(request, "temp_display.html", {'temp' : temp_f})
def weather_results(request, query):
	print (query)
	key = 'dcdff188d0ebcd4c1ecee4fa0a6be769'
	r = requests.get('http://api.openweathermap.org/data/2.5/weather?q='+query+',in&appid='+key+'')
	json_object = r.json()
	print(json_object)
	temp_k = float(json_object['main']['temp'])
	global temp_f
	temp_f = (temp_k - 273.15) * 1.8 + 32
	url = "http://127.0.0.1:8000/temp_display"
	return JsonResponse({'result' : url})

	

