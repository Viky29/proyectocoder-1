from datetime import datetime
from django.http import HttpResponse  

import random

def saludo(request):
    return HttpResponse("Hola Django somos-coder")

def numero_random(request):
    return HttpResponse(random.random())

def saludo_con_nombre(request):
    return HttpResponse("buenas noches:.....Rubi")

