from django.http import HttpResponseBadRequest
from django.shortcuts import render
from django.utils import timezone


def index(request):
    return render(request, "index.html")


def time_partial(request):
    context = {"now": timezone.now()}
    if getattr(request, "htmx", False):
        return render(request, "partials/time.html", context)
    return HttpResponseBadRequest("HTMX requests only")


