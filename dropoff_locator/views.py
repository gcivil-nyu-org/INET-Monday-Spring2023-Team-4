from django.shortcuts import render
from django.views.generic import TemplateView

# from .services import get_locations
from .models import Site

# class GetLocations(TemplateView):
#     template_name = 'locations.html'
#     def get_context_data(self, *args, **kwargs):
#         context = {
#             'locations' : get_locations(),
#         }
#         return context


def locations(request):
    locations = Site.objects.all()
    context = {"locations": locations}
    return render(request, "locations.html", context)
