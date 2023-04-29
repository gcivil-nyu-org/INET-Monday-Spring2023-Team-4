import django_filters.filterset
from dropoff_locator.models import Site


class SiteFilter(django_filters.FilterSet):
    class Meta:
        model = Site
        fields = {
            "borough": ["exact"],
            "type": ["exact"],
            "accepted_items": ["exact"],
        }
