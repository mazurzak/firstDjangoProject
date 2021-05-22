
from django.http import HttpResponse
from django.urls import path

from . import views


def hello(request, name="World"):
    return HttpResponse(f"Hello {name}!")


urlpatterns = [
    path('', hello),
    path('<name>', hello),
]
