from django.shortcuts import render
import requests

def index(request):
    appid = '82b797b6ebc62503218e16f1b42c016'
	url = 'https://samples.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + appid
	city = 'London'
	res = requests.get(url.format(city))


    print(res.text)
	return render(request, 'food/index.html')