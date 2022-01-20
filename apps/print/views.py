from multiprocessing import context
import environ
import requests
import json

from django.shortcuts import render
from django.http import HttpResponse

env = environ.Env(DEBUG=(bool, False))
environ.Env.read_env(env_file="docker/.env")
URL_PRINT = env("URL_PRINT")

def index(request):
    jsonPrintParameters = print_parameters(request)
    for parameter in jsonPrintParameters["parameters"]:
        if parameter["name"] == "Layout_Template":
            plantillas = parameter["choiceList"]
            print(plantillas)
    
    context = {
        "plantillas": plantillas
    }

    if(request.GET.get('btnImprimir')):
        print(request.GET.get('textDPI'))

    return render(request, "printApp/index.html", context)

def print_parameters(request):
    res = requests.get(URL_PRINT + '?f=pjson')
    return res.json()
