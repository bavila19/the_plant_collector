from django.shortcuts import render
# View class handles requests
from django.views import View
from django.views.generic.base import TemplateView
# A class to handle sending a type of response
from django.http import HttpResponse

# Create your views here.

# Here we will be creating a class called Home and extending it from the View class
class Home(TemplateView):
    template_name = "home.html"

class About (TemplateView):
    template_name= "about.html"

class Plant:
    def __init__ (self, name, image, description):
        self.name = name 
        self.image = image
        self.description = description

plants = [
    Plant("Monstera", "https://cdn.shopify.com/s/files/1/0597/1460/1169/products/detailSSP_2387_1400x.jpg?v=1645668123", "Monstera deliciosa, the Swiss cheese plant or split-leaf philodendron is a species of flowering plant native to tropical forests of southern Mexico, south to Panama. It has been introduced to many tropical areas, and has become a mildly invasive species in Hawaii, Seychelles, Ascension Island and the Society Islands"),
    Plant("Marble Queen Pothos", "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS_pfKnrrRTJIu8gAPan8_kX7qy7CkpScF7jz6XtbIH7oRe2sCDAlvS2icOPsuHIrlygMs&usqp=CAU", "Part of the aroid family, Araceae, it is a climbing vine, capable of growing to over 3m in height. It produces glossy bright green, oval-shaped leaves that are heavily spotted and streaked with cream-white colouring." )
]

class PlantList(TemplateView):
    template_name = "plant_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["plants"] = plants # this is where we add the key into our context object for the view to use
        return context
