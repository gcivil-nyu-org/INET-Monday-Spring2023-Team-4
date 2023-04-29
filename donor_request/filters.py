import django_filters
from .models import Request
from django_filters import ChoiceFilter


class RequestFilter(django_filters.FilterSet):
    class Meta:
        model = Request
        fields = {
            "host": ["exact"],
            "status": ['exact'],
        }
