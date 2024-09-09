from django.shortcuts import render
import requests
import json
from django.views.generic import RedirectView

url = 'https://newsapi.org/v2/everything'  
API_KEY = "ccd154be70cf44aebb76629eda9b81be"

def index(request):
    
    params = {
    'domains': 'bbc.co.uk, cnn.com',  # Restrict the search to specific domains
    'q': 'climate change',
    'apiKey': API_KEY
}
    
    params = {
    'qInTitle': 'AI',  # Search only in article titles for 'AI'
    'apiKey': API_KEY
}
    
    params = {
    'sources': 'bbc-news, cnn',  # Search in specific news sources
    'q': 'health',
    'apiKey': API_KEY
}
    #Getting the selected options
    q = request.GET.get('q')
    Endpoint = request.GET.get('Endpoint')
    sel = request.GET.get('sel')
    sel1 = request.GET.get('sel1')

    #checking whether all query parameters are present or not

    #calling the endpoints and saving the responses
    if Endpoint=='everything':
        url = f'https://newsapi.org/v2/everything?q={q}&language={sel}&sortby={sel1}&apiKey={API_KEY}'
        
    else:
        url = f'https://newsapi.org/v2/top-headlines?q={q}&country={sel}&category={sel1}&apiKey={API_KEY}'
    
    response = requests.get(url)
    data = response.json()
    status = data['status']

    if status=='ok':
        articles = data['articles']
        total_results = data['totalResults']
        context = {
            'status' : status,
            'articles' : articles,
            'total_results' : total_results
        }
    else:
        message = data['message']
        context = {
            'status' : status,
            'message' : message
        }

    #rendering the results
    return render(request, 'news_app/index.html', context)
    
