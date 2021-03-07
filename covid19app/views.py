from django.shortcuts import render
import requests
import json
#rapidapi apicall
url = "https://covid-193.p.rapidapi.com/statistics"

headers = {
    'x-rapidapi-key': "27ce14180amsh575aa57f1ac1fe7p16ad33jsn6029aa888866",
    'x-rapidapi-host': "covid-193.p.rapidapi.com"
    }
#until here

#get response and turn it into json
response = requests.request("GET", url, headers=headers).json()


# Create your views here.
def helloworldview(request):
    if request.method=="POST":
        mylist = []  # empty list to store the country data
        noofresult = int(response['results'])  # number of result
        for x in range(0, noofresult):
            # print(response['response'][x]['country'])
            mylist.append(response['response'][x]['country'])


        selectedcountry = request.POST['selectedcountry']
        noofresult = int(response['results'])  # number of result
        for x in range(0, noofresult):
            if selectedcountry == response['response'][x]['country']: #if the country in response = selected country return that country cases
                new = response['response'][x]['cases']['new']
                active = response['response'][x]['cases']['active']
                critical = response['response'][x]['cases']['critical']
                recovered = response['response'][x]['cases']['recovered']
                total = response['response'][x]['cases']['total']
                deaths = int(total) - int(active) - int(recovered)
        context = {'selectedcountry':selectedcountry, 'mylist': mylist, 'new': new, 'active': active, 'critical': critical, 'recovered': recovered, 'total': total, 'deaths': deaths, 'total': total}
        return render(request, 'helloworld.html', context)


    context = {'mylist' : mylist}
    return render(request, 'helloworld.html', context) #move the context to html