from django.shortcuts import render
import requests

def index(request):
    appid = '82b797b6ebc62503218e16f1b42c016'
	url = 'https://samples.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + appid
	city = 'London'
	res = requests.get(url.format(city))

	city_info={

	'city':city,
	'temp':res["main"]["temp"],
	'icon':res["weather"]["icon"]
	}
    print(res.text)
	return render(request, 'weather/index.html')