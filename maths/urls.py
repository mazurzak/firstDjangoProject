from django.urls import path
from . import views

urlpatterns = [
    path('add/<int:number1>/<int:number2>', views.add),
    path('div/<int:number1>/<int:number2>', views.div),
]
