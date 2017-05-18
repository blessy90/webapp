from django.http import HttpResponse

"""To return Hello World to the webapp"""
def index(request):
    return HttpResponse("Hello World.")
