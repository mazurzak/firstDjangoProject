from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
#


def sub(request, number1, number2):
     return HttpResponse(f'Wynik odejmowania to: {number1 - number2}')


def mul(request, number1, number2):
    return HttpResponse(f'Wynik mnożenia to: {number1 * number2}')


def add(request, number1, number2):
    return HttpResponse(f"Wynik dodawania to: {number1 + number2}")


def div(request, number1, number2):

    if number2 == 0:
        return HttpResponse("Błąd, nie dziel przez zero!")
    else:
        return HttpResponse(f"Wynik dzielenia to: {number1/ number2}")
