from django import forms

class EssentialsForm(forms.Form):
    StateName = forms.CharField(label='State', max_length=80)
    CityName = forms.CharField(label='City', max_length=80)
    ServiceName = forms.CharField(label='Service', max_length=200)