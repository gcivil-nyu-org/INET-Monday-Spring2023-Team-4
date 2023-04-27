from django.contrib import admin
from .models import Site, Item, SiteAccepted

admin.site.register(Site)
admin.site.register(Item)
admin.site.register(SiteAccepted)
