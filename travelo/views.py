from django.shortcuts import render
from django.http import HttpResponse
from . models import Destination

# Create your views here.
def index(request):
    dest1= Destination()
    dest1.name = 'Karachi'
    dest1.desc = 'City of lights'
    dest1.price = '1000'
    dest1.img = 'destination_1.jpg'
    dest1.special_offer = False

    dest2= Destination()
    dest2.name = 'Lahore'
    dest2.desc = 'City for food'
    dest2.price = '800'
    dest2.img = 'destination_2.jpg'
    dest2.special_offer = True

    dest3= Destination()
    dest3.name = 'Islamabad'
    dest3.desc = 'City of beauty'
    dest3.price = '950'
    dest3.img = 'destination_3.jpg'
    dest3.special_offer = True

    dests = [dest1,dest2,dest3]
    return render(request, 'index.html', {'dests':dests})

    