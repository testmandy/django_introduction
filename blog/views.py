from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
import json
from django.shortcuts import render


# def request():
#     jsonStr = {"amy":1, "b":1, "c":1,"d":1, "e":1, "f":1}
#     return render(request, 'test.html', {"ret": json.dumps(jsonStr)})

def hello_world(request):
    return HttpResponse("Hello World")