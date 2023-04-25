from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from dropoff_locator.models import Site


# Extending User Model Using a One-To-One Link
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    avatar = models.ImageField(default="default.jpg", upload_to="profile_images")
    bio = models.TextField()
    url = models.CharField(max_length=225, null=True)
    sites = models.ManyToManyField(Site, through="SiteHost", related_name="hosts")

    def __str__(self):
        return self.user.username

    # resizing images
    def save(self, *args, **kwargs):
        super().save()

        img = Image.open(self.avatar.path)

        if img.height > 100 or img.width > 100:
            new_img = (100, 100)
            img.thumbnail(new_img)
            img.save(self.avatar.path)

    def is_acceptor(self):
        return self.sites.all().exists()


class SiteHost(models.Model):
    site = models.ForeignKey(Site, on_delete=models.CASCADE, unique=False)
    host = models.ForeignKey(Profile, on_delete=models.CASCADE, unique=False)

    def __str__(self):
        # return "{}_{}".format(self.site.__str__(), self.host.__str__())
        return self.site.__str__()
