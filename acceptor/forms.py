from django.forms import ModelForm, TextInput, Textarea
from dropoff_locator.models import Site


class NewSiteForm(ModelForm):
    class Meta:
        model = Site
        fields = ["name", "address", "borough", "notes"]
        widgets = {
            'name': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Name'
                }),
            'address': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': '123 Main St'
                }),
            'notes': Textarea(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Notes'
                }),
        }