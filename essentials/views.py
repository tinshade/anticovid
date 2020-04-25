from django.shortcuts import render
from django.http import JsonResponse
from .forms import EssentialsForm
import requests
def search_data(StateName,CityName,ServiceName):
    print(StateName,CityName,ServiceName)
    url = "https://api.covid19india.org/resources/resources.json"
    resp = requests.get(url=url)
    data = resp.json()
    print(data)

def essentials(request):
    if request.method == 'POST':
        form = EssentialsForm(request.POST)
        if form.is_valid():
            StateName = form.cleaned_data['StateName']
            CityName = form.cleaned_data['CityName']
            ServiceName = form.cleaned_data['ServiceName']
            r = search_data(StateName,CityName,ServiceName)
            return JsonResponse({ 'infos': r })
    else:
        form = EssentialsForm()
        return render(request, 'essentials/test.html', {'form': form})