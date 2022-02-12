from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
def reservations_view(request):
    return JsonResponse({"msg": "This is the reservations home"})


def reservations_add_view(request):
    return JsonResponse({"msg": "This is the reservations ADD page"})
