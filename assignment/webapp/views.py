import  operator
from django.http import HttpResponse
from django.shortcuts import render
from .models import RequestCounter

"""To return Hello World to the webapp"""
def index(request):
    return HttpResponse("Hello World.")

"""Receives the http request to sort the integers and returns the sorted list"""
def post(request,*args, **kwargs):

    if request.method == "POST":
        requestCounter = RequestCounter.objects.get(id=1)
        requestCounter.counter += 1
        requestCounter.save()
        print("The numbers of times the '/v1/sort' URL is hit is",requestCounter.counter)
        values = request.POST['sortdata']
        values = values.replace(",","")
        if values.isdigit():
            data = sorted(values)
            context = {'sortedlist': data}
        else:
            context = {'sortedlist': "Entered list is not integers"}
        return render(request,"webapp/sort.html",context)
    else:
        return render(request, "webapp/sort.html")
