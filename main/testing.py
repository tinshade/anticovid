import requests
def getstatestat(statename):
    sn = statename.replace(' ', '').lower()
    senddata = {"statename":None, "active": 0, "recovered":0, "deaths":0, "confirmed":0}
    url = "https://api.covid19india.org/state_district_wise.json"
    response = requests.request("GET", url)
    data = response.json()
    active,confirmed,recovered,deaths = 0,0,0,0
    for each in data:
        if each.lower().replace(' ','') == sn:
            for key, value in data[each]['districtData'].items():
                active = active+value['active']
                confirmed = confirmed+value['confirmed']
                recovered = recovered+value['recovered']
                deaths = deaths+value['deceased']
            senddata['statename'] = each
            senddata['active'] = active
            senddata['confirmed'] = confirmed
            senddata['recovered'] = recovered
            senddata['deaths'] = deaths

    return senddata


print(getstatestat("tamil nadu"))