import environ
import requests

from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

env = environ.Env(DEBUG=(bool, False))
environ.Env.read_env(env_file="docker/.env")
URL_PRINT = env("URL_PRINT")

def index(request):
    jsonPrintParameters = print_parameters(request)
    return jsonPrintParameters

def print_parameters(request):
    res = requests.get(URL_PRINT + '?f=pjson')
    json = JsonResponse(res.json())
    return json