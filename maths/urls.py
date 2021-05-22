from django.urls import path
from . import views

urlpatterns = [
    path('sub/<int:number1>/<int:number2>', views.sub),
    path('mul/<int:number1>/<int:number2>', views.mul),
]
