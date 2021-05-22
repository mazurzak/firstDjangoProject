from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
#
def sub(request, number1, number2):
     return HttpResponse(f'Wynik odejmowania to: {number1 - number2}')

def mul(request, number1, number2):
    return HttpResponse(f'Wynik mnożenia to: {number1 * number2}')
