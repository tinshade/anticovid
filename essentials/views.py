from django.shortcuts import render
def essentials(request):
    return render(request, 'essentials/resources.html', {'title': "Resources | COVID-19 Informatrics"})