from django.shortcuts import render
from django.views.generic import TemplateView
from .services import get_locations

class GetLocations(TemplateView):
    template_name = 'locations.html'
    def get_context_data(self, *args, **kwargs):
        context = {
            'locations' : get_locations(),
        }
        return context
