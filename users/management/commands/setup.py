from django.core.management.base import BaseCommand, CommandError
from users.models import Profile
from dropoff_locator.models import Site, Item


class Command(BaseCommand):
    help = "Set up initial database objects"

    def handle(self, *args, **options):
        sites = Site.objects.all()
        hosts = Profile.objects.all()

        for site in sites:
            if site.type == "NYC Smart Bin":
                for i in range(1, 9):
                    site.accepted_items.add(Item.objects.get(pk=i))
                    site.save()

            elif site.type == "NYC Community Site":
                for i in [1, 2, 3, 7, 8]:
                    site.accepted_items.add(Item.objects.get(pk=i))
                    site.save()

        for host in hosts:
            if "http" in host.user.email:
                host.url = host.user.email
                host.save()
