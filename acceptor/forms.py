from django.forms import ModelForm, TextInput, Textarea, CheckboxSelectMultiple
from dropoff_locator.models import Item, Site


class NewSiteForm(ModelForm):
    class Meta:
        model = Site
        fields = ["name", "address", "borough", "notes", "accepted_items",]
        widgets = {
            "name": TextInput(
                attrs={
                    "class": "form-control",
                    "style": "max-width: 300px;",
                    "placeholder": "Name",
                }
            ),
            "address": TextInput(
                attrs={
                    "class": "form-control",
                    "style": "max-width: 300px;",
                    "placeholder": "123 Main St",
                }
            ),
            "notes": Textarea(
                attrs={
                    "class": "form-control",
                    "style": "max-width: 300px;",
                    "placeholder": "ex. Dropoff available only on weekends",
                }
            ),
            "accepted_items": CheckboxSelectMultiple(
                attrs={
                    "class": "form-control",
                    "style": "max-width: 300px;",
                    "choices": Item.objects.all(),
                }
            ),
        }
