from django import forms
from django.forms import ModelForm
from dropoff_locator.models import Item, Site

BOROUGHS = [
    ("", "---"),
    ("Manhattan", "Manhattan"),
    ("Brooklyn", "Brooklyn"),
    ("Queens", "Queens"),
    ("Bronx", "Bronx"),
    ("Staten Island", "Staten Island"),
]

class NewSiteForm(ModelForm):
    name = forms.CharField(
        label='Site Name', 
        widget=forms.TextInput(attrs={'placeholder': "Joe's Worm Farm"})
    )
    address = forms.CharField(
        label='Street Address',
        widget=forms.TextInput(attrs={'placeholder': '123 Main St'})
    )
    borough = forms.ChoiceField(choices=BOROUGHS)
    notes = forms.TextInput()
    accepted_items = forms.ModelMultipleChoiceField(
        label = 'Accepted Items',
        queryset=Item.objects.all(),
        widget=forms.CheckboxSelectMultiple()
    )

    class Meta:
        model = Site
        fields = [
            "name",
            "address",
            "borough",
            "notes",
            "accepted_items",
        ]
