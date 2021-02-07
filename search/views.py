from django.http import HttpResponse
from django.shortcuts import render
from .helpers import perform_search, manage_theme
from urllib.parse import urlencode
from django.conf import settings


# Create your views here.
def about(request):
    return render(request,"search/start.html")

def index(request):
    """ The page where users can search """

    url_params = {}
    query = request.GET.get("q", "")
    start_index = request.GET.get("start")
    search_data = perform_search(query, start_index=start_index)

    return render(request, "search/index.html", {
        "query": query,
        **search_data,
        **manage_theme(request, query, start_index),
    })


def credits(request):
    """ Credits to all the open source projects used in DevXplore """

    # Data of each open source project included
    projects = {
        'Django': {
            'description': 'Django is a high-level Python Web framework that encourages rapid development and clean, pragmatic design',
            'project_link': 'https://github.com/django/django',
            'license_type': 'BSD',
        },
        'Materialize': {
            'description': 'Materialize, a CSS Framework based on Material Design',
            'project_link': 'https://github.com/Dogfalo/materialize',
        },

        'google-api-python-client': {
            'description': "The official Python client library for Google's discovery based APIs.",
            'project_link': 'https://github.com/googleapis/google-api-python-client',
            'license_type': 'Apache',
        },

        'django-heroku': {
            'description': 'Django library for Heroku applications that ensures a seamless deployment and development experience.',
            'project_link': 'https://github.com/heroku/django-heroku',
            'license_type': 'BSD',
            
        },
        'django-htmlmin': {
            'description': 'django-html is an HTML minifier for Python, with full support for HTML 5',
            'project_link': 'https://github.com/cobrateam/django-htmlmin',
            'license_type': 'BSD',
        },

         'tldextract': {
            'description': 'Accurately separate the TLD from the registered domain and subdomains of a URL, using the Public Suffix List.',
            'project_link': 'https://github.com/john-kurkowski/tldextract',
            'license_type': 'BSD',
        },

         'python-decouple': {
            'description': 'Decouple helps you to organize your settings so that you can change parameters without having to redeploy your app.',
            'project_link': 'https://github.com/henriquebastos/python-decouple/',
            'license_type': 'MIT',
        },

        'gunicorn': {
            'description': "gunicorn 'Green Unicorn' is a WSGI HTTP Server for UNIX, fast clients and sleepy applications",
            'project_link': 'https://github.com/benoitc/gunicorn',
            'license_type': 'MIT',
        },
    }

    return render(request, "search/credits.html",{'projects': projects,**manage_theme(request, "",""),})
