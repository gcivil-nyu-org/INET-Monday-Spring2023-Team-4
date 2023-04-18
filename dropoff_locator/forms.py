from django import forms

class SiteFilterForm(forms.Form): 
    borough = forms.CharField()
    