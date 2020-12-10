import requests
import json
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
   
    response = requests.get('https://api.themoviedb.org/3/movie/top_rated?api_key=52364270e03d88b2f26ad29cff466e81&language=en-US&page=1')
   
    json_str= json.dumps(response.json(),indent=2)
    data=json.loads(json_str)

    movie_data={}
    for i in range(len(data['results'])):
        movie_data[data['results'][i]['id']] = {"poster_path":data['results'][i]['poster_path'],
                                            "title":data['results'][i]['title'],
                                            "overview":data['results'][i]['overview'],
                                            "popularity":data['results'][i]['popularity'],
                                            }
    context={
       'movie_data':movie_data,
    }

    return HttpResponse("Hello")
    # return render(request, 'movies/index.html',context)
