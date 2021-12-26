from django.http.response import HttpResponse


def homepage(request):
    return HttpResponse("Hello CSE-465 (Week 7)")