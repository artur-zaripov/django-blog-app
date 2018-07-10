from django.http import HttpResponse

def index(request):
    return HttpResponse('Welcome! <a href="/api/v1/">Click here to go to API</a>')
