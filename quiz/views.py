from django.shortcuts import render
from django.http import JsonResponse
import smtplib, ssl
import random
import requests

def mq(request):
    data = request.GET
    full_name = data['fn']
    question = data['q']
    answer = data['a']
    explanation = data['exp']
    port = 465
    smtp_server = "smtp.gmail.com"
    sender_email = "covidinformatrics@gmail.com"
    receiver_email = "covidinformatrics@gmail.com"
    password = "#COVID#Abhishek98"
    space = " "
    message = """\
    Subject: QuizQuestions"""+space+"""
    \nName="""+full_name+"""
    \nQuestion="""+question+"""
    \nAnswer="""+answer+"""
    \nExplanation="""+explanation+"""
    """
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)
    return JsonResponse("Done", safe=False)

def quiz(request):
    return render(request, 'quiz/quiz.html', {'title':'Quiz Time | COVID-19 Informatrics'})



####BOT SECTION####

greet = ['hi', 'hello', 'anyone', 'there', 'hi!', "hello!", "how are you?",'hi?', "hello?","anyone?"]

greet_response = ['Hey there! I am NOVELBot!', "How may I help you?", "Hello!"]

hru = ["how are you?", "how are you doing?", "are you ok?", "are you fine?", "are you well?","how are you", "how are you doing", "are you ok", "are you fine", "are you well"]

hru_response = ['I am doing great! Hope you are safe, healthy and indoors!', "Since COVID-19 is not a computer virus, I am safe!", "I am fine! Hope you are too!"]

ask_help = ["help", "can do", "what can you do", "options", "tell me", "tell"]

asking = [
"have corona",
"have the corona",
"have novel corona",
"have coronavirus",
"have COVID-19",
"have the coronavirus",
]

options = [
'Fetch world-wide data',
"Fetch India's current status",
'Fetch country-wise data(status country countryname)',
'Fetch state-wise data(status state statename)',
'Fetch symptoms related to COVID-19',
'Fetch resources by state(resources statename)'
'Debunk myths related to COVID-19 with facts',
'State best practices to aid against COVID-19',
]

symptoms = [
"Fever",
"Tiredness",
"Dry Cough",
"Aches & Pains",
"Nasal Congestion",
"Runny Nose",
"Sore Throat",
"Diarrhoea"
]

myths = [
    {'s':'Spraying chlorine or alcohol on the skin kills viruses in the body', 'a':'Applying alcohol or chlorine to the body can cause harm, especially if it enters the eyes or mouth. Although people can use these chemicals to disinfect surfaces, they should not use them on the skin.'},
    {'s':'Only older adults and young people are at risk', 'a':'SARS-CoV-2, like other coronaviruses, can infect people of any age. However, older adults and individuals with preexisting health conditions, such as diabetes or asthma, are more likely to become severely ill.'},
    {'s':'Children cannot get COVID-19', 'a':'All age groups can contract SARS-CoV-2.'},
    {'s':'COVID-19 is just like the flu', 'a':'SARS-CoV-2 causes an illness that does have flu-like symptoms, such as aches, a fever, and a cough. Similarly, both COVID-19 and the flu can be mild, severe, or, in rare cases, fatal. Both can also lead to pneumonia.'},
    {'s':'Everyone with COVID-19 dies', 'a':'This statement is untrue. As we mentioned above, COVID-19 is only fatal for a small percentage of people.'},
    {'s':'Cats and dogs spread coronavirus', 'a':'Currently, there is little evidence to suggest that SARS-CoV-2 can infect cats and dogs. However, in Hong Kong, a Pomeranian whose owner had COVID-19 also contracted the virus. The dog did not display any symptoms.'},
    {'s':'Face masks always protect against coronavirus', 'a':'Healthcare workers use professional face masks, which fit tightly around the face, to protect themselves from infection.Disposable and cloth masks can protect against droplets, but neither can protect against aerosolized particles.The Centers for Disease Control and Prevention (CDC) recommend that all people wear cloth face masks in public places where it is difficult to maintain a 6-foot (2-meter) distance from others. This will help slow the spread of the virus from asymptomatic people and those who do not know that they have contracted it.When wearing a mask, it is essential to continue with other precautions, such as not touching the face and practicing physical distancing.'},
    {'s':'Hand dryers kill coronavirus', 'a':'Hand dryers do not kill coronavirus. The best way to protect oneself and others from the virus is to wash the hands with soap and water or an alcohol-based hand rub.'},
    {'s':'SARS-CoV-2 is just a mutated form of the common cold', 'a':'Coronaviruses are a large family of viruses, all of which have spiky proteins on their surface. Some of these viruses use humans as their primary host and cause the common cold. Other coronaviruses, such as SARS-CoV-2, primarily infect animals.'},
    {'s':'You have to be with someone for 10 minutes to catch the virus', 'a':'The longer someone is with a person who has it, the more likely they are to catch the virus themselves, but it is still possible to catch it in under 10 minutes.'},
    {'s':'Rinsing the nose with saline protects against coronavirus', 'a':'There is no evidence to suggest that a saline nose rinse protects against respiratory infections. Some research suggests that this technique might reduce the symptoms of acute upper respiratory tract infections, but scientists have not found that it can reduce the risk of infection.'},
    {'s':'You can protect yourself by gargling bleach', 'a':'People should never put bleach in their mouths. There are no circumstances in which gargling bleach might benefit a person’s health. Bleach is corrosive and can cause serious damage.'},
    {'s':'Antibiotics can kill coronavirus.', 'a':'Antibiotics only kill bacteria. They do not kill viruses.'},
    {'s':'Thermal scanners can diagnose coronavirus', 'a':'Thermal scanners can detect whether or not someone has a fever. However, other conditions, such as seasonal flu, can also produce a fever.In addition, symptoms of COVID-19 can appear 2–14 days after infection, which means that someone who has the virus could have a normal temperature for a few days before a fever begins.'},
    {'s':'Garlic protects against coronaviruses', 'a':'Some research suggests that garlic might slow the growth of some species of bacteria. However, COVID-19 is caused by a virus, and there is no evidence to suggest that garlic can protect people against COVID-19.'},
    {'s':'Parcels from China can spread coronavirus', 'a':'From previous research into similar coronaviruses, including those that cause SARS and MERS and are similar to SARS-CoV-2, scientists believe that the virus cannot survive on letters or packages for an extended period of time.'},
    {'s':'Home remedies can cure and protect against COVID-19', 'a':'No home remedies can protect against COVID-19. This goes for vitamin C, essential oils, silver colloid, sesame oil, garlic, fish tank cleaner, burning sage, and sipping water every 15 minutes.'},
    {'s':'You can catch coronavirus from eating Chinese food in the US', 'a':'No, you cannot'},
    {'s':'You can catch coronavirus from urine and feces', 'a':'It is unlikely that this is true, but the jury is currently out. According to Prof. John Edmunds, from the London School of Hygiene & Tropical Medicine in the U.K.:<br>“It isn’t a very pleasant thought, but every time you swallow, you swallow mucus from your upper respiratory tract. In fact, this is an important defensive mechanism. This sweeps viruses and bacteria down into our gut where they are denatured in the acid conditions of our stomachs.”<br>“With modern, very highly sensitive detection mechanisms, we can detect these viruses in feces. Usually, viruses we can detect in this way are not infectious to others, as they have been destroyed by our guts.”<br>However, it is worth noting that some research concludes that viruses similar to SARS-CoV-2 might persist in feces. A recent research letter in JAMA also concludes that SARS-CoV-2 is present in feces'},
    {'s':'The virus will die off when temperatures rise in the spring', 'a':'Some viruses, such as cold and flu viruses, do spread more easily in the colder months, but that does not mean that they stop entirely when conditions become milder.<br>As it stands, scientists do not know how temperature changes will influence the behavior of SARS-CoV-2.'},
    {'s':'Coronavirus is the deadliest virus known to humans', 'a':'Although SARS-CoV-2 does appear to be more serious than influenza, it is not the deadliest virus that people have faced. Others, such as Ebola, have higher mortality rates.'},
    {'s':'Flu and pneumonia vaccines can protect against COVID-19', 'a':'As SARS-CoV-2 is different to other viruses, no existing vaccines protect against infection.'},
    {'s':'The outbreak began because people ate bat soup', 'a':'Although scientists are confident that the virus started in animals, there is no evidence to suggest that it came from soup of any kind.'},
    {'s':'5G helps SARS-CoV-2 spread', 'a':'As the world becomes more connected, some regions are rolling out 5G mobile technology. A raft of conspiracy theories appear wherever this technology sets foot.<br>One of the most recent theories to emerge is that 5G is responsible for the swift spread of SARS-CoV-2 across the globe.<br>Some people claim that 5G helps viruses communicate, often citing a paper from 2011. In this study, the authors conclude that bacteria can communicate via electromagnetic signals. However, experts dispute this theory, and SARS-CoV-2 is a virus, not a bacterium.<br>Wuhan was one of the first cities to trial 5G in China, which helps explain the origin of some of these theories. However, Beijing, Shanghai, and Guangzhou also rolled out 5G at a similar time.<br>It is also worth noting that COVID-19 has significantly impacted countries with very little 5G coverage, such as Iran.'},
    {'s':'Drinking alcohol reduces the risk of infection', 'a':'In response to a series of myths surrounding alcohol and COVID-19, the WHO released a statement. In it, they explain that although alcohol can disinfect the skin, it does not work the same way inside the body.<br>They explain that “consuming any alcohol poses health risks, but consuming high-strength ethyl alcohol (ethanol), particularly if it has been adulterated with methanol, can result in severe health consequences, including death.”<br>In a fact sheet on the subject, they write that, “Alcohol use, especially heavy use, weakens the immune system and thus reduces the ability to cope with infectious diseases.”<br>Because alcohol is associated with a number of diseases, it may make people more vulnerable to COVID-19.'},
    {'s':'Injecting or consuming bleach or disinfectant kills the virus', 'a':'Consuming or injecting disinfectant or bleach will not remove viruses from the body.'}
]

best_response = [
    {'s':'Regularly and thoroughly clean your hands with an alcohol-based hand rub or wash them with soap and water.', 'a':' Washing your hands with soap and water or using alcohol-based hand rub kills viruses that may be on your hands.'},
    {'s':'Maintain at least 1 metre (3 feet) distance between yourself and others.', 'a':'When someone coughs, sneezes, or speaks they spray small liquid droplets from their nose or mouth which may contain virus. If you are too close, you can breathe in the droplets, including the COVID-19 virus if the person has the disease.'},
    {'s':'Avoid going to crowded places.', 'a':'Where people come together in crowds, you are more likely to come into close contact with someone that has COIVD-19 and it is more difficult to maintain physical distance of 1 metre (3 feet).'},
    {'s':'Avoid touching eyes, nose and mouth.', 'a':'Hands touch many surfaces and can pick up viruses. Once contaminated, hands can transfer the virus to your eyes, nose or mouth. From there, the virus can enter your body and infect you.'},
    {'s':'Make sure you, and the people around you, follow good respiratory hygiene. This means covering your mouth and nose with your bent elbow or tissue when you cough or sneeze. Then dispose of the used tissue immediately and wash your hands.', 'a':'Droplets spread virus. By following good respiratory hygiene, you protect the people around you from viruses such as cold, flu and COVID-19.'},
    {'s':'Stay home and self-isolate even with minor symptoms such as cough, headache, mild fever, until you recover. Have someone bring you supplies. If you need to leave your house, wear a mask to avoid infecting others.', 'a':'Avoiding contact with others will protect them from possible COVID-19 and other viruses.'},
    {'s':'If you have a fever, cough and difficulty breathing, seek medical attention, but call by telephone in advance if possible and follow the directions of your local health authority.', 'a':'National and local authorities will have the most up to date information on the situation in your area. Calling in advance will allow your health care provider to quickly direct you to the right health facility. This will also protect you and help prevent spread of viruses and other infections.'},
    {'s':'Keep up to date on the latest information from trusted sources, such as WHO or your local and national health authorities.', 'a':'Local and national authorities are best placed to advise on what people in your area should be doing to protect themselves.'}
]
qmyth = ['myths', 'myth', 'fact', 'facts', 'knowledge']
best_practices = ["what are the best practices?", "best?", "practices?","best", "practices", "best practices?", "best practices", "suggestions", "suggestion", "suggest", 'prevention', 'preventions', 'preventional measures', 'safe', 'protection', 'protection against coronavirus', 'protection against', 'stop the spread']
appreciation=["good", "amazing","wow", "wonderful","great", "brilliant", "fabulous", "fantastic", 'futuristic', 'feedback']
thanks = [
    f"Was that a compliment? Thank you so much! <i class='fas fa-smile-beam text-warning'></i><br>Please consider leaving a feedback <a href='/feedbacks' target='_blank' title='Feedback!'>here!</a>",
    f"Like my efforts?<br>Please consider leaving a feedback <a href='/feedbacks' target='_blank' title='Feedback!'>here!</a>",
    f"So kind! <i class='fas fa-heart text-danger'></i><br>Please consider leaving a feedback <a href='/feedbacks' target='_blank' title='Feedback!'>here!</a>",
    f"I am glad I could be of service! <i class='fas fa-smile text-warning'></i><br>Please consider leaving a feedback <a href='/feedbacks' target='_blank' title='Feedback!'>here!</a>"
]
def week():
	from datetime import datetime as date
	week = date.today().strftime("%A")
	return week

#GETTING INDIA STATS
def getinddata():
	url = "https://covid-19-india-data-by-zt.p.rapidapi.com/GetIndiaTotalCounts"
	headers = {
        "x-rapidapi-host": "covid-19-india-data-by-zt.p.rapidapi.com",
		"x-rapidapi-key": "4c265e0db5msh2d261aab83a8dfbp1d9134jsnfb7360ed7019"
	}
	response = requests.request("GET", url, headers=headers)
	data = response.json()
	senddata = {"active": 0, "recovered":0, "deaths":0, "confirmed":0}
	senddata['confirmed'] = data['data'][0]['confirmed']
	senddata['active'] = data['data'][0]['active']
	senddata['recovered'] = data['data'][0]['recovered']
	senddata['deaths'] = data['data'][0]['deaths']
	return senddata

#GETTING STATEWISE STATS
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

#FETCH GLOBAL DATA
def worlddata():
    url = "https://coronavirus-map.p.rapidapi.com/v1/summary/latest"
    headers = {
        'x-rapidapi-host': "coronavirus-map.p.rapidapi.com",
        'x-rapidapi-key': "b827ab8680mshbd7949fbb60d632p1ff3cfjsn6f4462105676"
    }
    response = requests.request("GET", url, headers=headers)
    data = response.json()
    return data

#FETCH COUNTRYWISE DATA
def getcountrywise(country):
	url = "https://coronavirus-map.p.rapidapi.com/v1/summary/region"
	querystring = {"region":country}
	headers = {
	    'x-rapidapi-host': "coronavirus-map.p.rapidapi.com",
	    'x-rapidapi-key': "b827ab8680mshbd7949fbb60d632p1ff3cfjsn6f4462105676"
	    }
	response = requests.request("GET", url, headers=headers, params=querystring)
	data = response.json()
	return data

#FETCH RESOURCES
def getresources(statename):
    url = "https://api.covid19india.org/resources/resources.json"
    state = statename.capitalize().replace(" ","") 
    response = requests.request("GET", url)
    data = response.json()
    count = 1
    senddata = {'category': "", 'city': "", 'contact': "", 'organisation': "", 'phone': ""}
    for each in data['resources']:
        if state == each['state'].replace(' ',''):
            senddata['category'] = each['category']
            senddata['city'] = each['city']
            senddata['contact'] = each['contact']
            senddata['description'] = each['descriptionandorserviceprovided']
            senddata['organisation'] = each['nameoftheorganisation']
            senddata['phone'] = each['phonenumber']
        else:
            pass
    
    return senddata

def askbot(request):
    inp = request.GET['asked'].lower()
    reply = ''
    if inp in greet:
        reply = greet_response[random.randint(0, len(greet_response)-1)]
    elif inp in hru:
        reply = hru_response[random.randint(0, len(hru_response)-1)]
    elif "day" in inp:
        reply = "Its a "+week()+" today!"
    elif "symptoms" in inp or "signs" in inp:
        reply = "Symptoms of the COVID-19 include:"
        reply += " <br>"
        for each in symptoms:
            reply +="<strong>"+each+"</strong>,<br>"
    elif inp in ask_help:
        reply = "I can help you with:"
        for each in options:
            reply += "<strong>"+each+"</strong>,<br>"
    elif inp in asking:
        reply = "If you feel sick or cold, visit a doctor soon!<br>Here are some symptoms:"
        for each in symptoms:
            reply += f"<strong>{each}</strong>"
    elif inp in qmyth:
        reply = "Here's a myth debunk for you!<br><br>"
        myth =  myths[random.randint(0,len(myths)-1)]
        reply += f"<p style='font-weight: 700'>{myth['s']}</p><br>"
        reply += f"<article>{myth['a']}</article><br>"
    elif inp in best_practices:
        reply = "Here's a best practice to follow!<br><br>"
        best =  best_response[random.randint(0,len(best_response)-1)]
        reply += f"<p style='font-weight: 700'>{best['s']}</p><br>"
        reply += f"<article>{best['a']}</article><br>"
    elif inp in appreciation:
        reply = thanks[random.randint(0,len(thanks)-1)]
    elif "status" in inp and "india" in inp:
        showdata = getinddata()
        reply = "Showing statistics in <strong>India</strong>:<br><hr><br>"
        reply += f"Confirmed cases: <strong>{showdata['confirmed']}</strong><br>"
        reply += f"Active cases: <strong>{showdata['active']}</strong><br>"
        reply += f"Recovered: <strong>{showdata['recovered']}</strong><br>"
        reply += f"Deceased: <strong>{showdata['deaths']}</strong><br>"
    elif "resources" in inp or "resource" in inp or "essentials" in inp or "essentials" in inp:
        sn = inp.split()
        if len(sn) == 2:
            showdata = getresources(sn[1])
            reply = f"Showing a few resources in <strong>{sn[1].capitalize()}</strong><br><br>"
            reply += f"There's <span style='color:#f71a56;'>{showdata['category']}</span> in <span style='color:#f71a56;'>{showdata['city']}</span> run by <span style='color:#f71a56;'>{showdata['organisation']}</span>!<br>"
            reply += f"Contact them at <a style='color:#f71a56' href='tel:{showdata['phone']}'>{showdata['phone']}</a> or reach out <a href='{showdata['contact']}' title='Organisation website'>here!</a>"
            reply += "<p style='font-weight: 400'>For more resources, visit this <a href='/essentials' title='Our Essentials Page'>page</a>!</p>"

    elif "status" in inp and "state" in inp:
        sn = inp.split()
        if len(sn) == 3:
            showdata = getstatestat(sn[2].replace('&','and'))
            reply = f"Statistics in <strong>{showdata['statename']}</strong>:<br><hr><br>"
            reply += f"Confirmed cases: <strong>{showdata['confirmed']}</strong><br>"
            reply += f"Active cases: <strong>{showdata['active']}</strong><br>"
            reply += f"Recovered: <strong>{showdata['recovered']}</strong><br>"
            reply += f"Deceased: <strong>{showdata['deaths']}</strong><br>"
        elif len(sn) > 3:
            ns = ""
            for each in sn[2::]:
                ns += each.replace('&','and')
                showdata = getstatestat(ns)
                reply = f"Statistics in <strong>{showdata['statename']}</strong>:<br><hr><br>"
                reply += f"Confirmed cases: <strong>{showdata['confirmed']}</strong><br>"
                reply += f"Active cases: <strong>{showdata['active']}</strong><br>"
                reply += f"Recovered: <strong>{showdata['recovered']}</strong><br>"
                reply += f"Deceased: <strong>{showdata['deaths']}</strong><br>"
        else:
            reply = "If you need statistics for an Indian state, try typing<br><i>status state statename</i>"
    elif "country" in inp and "status" in inp:
        sn = inp.split()
        if len(sn) == 3:
            showdata = getcountrywise(sn[2])
            reply = f"Statistics in <strong>{sn[2].capitalize}</strong> statistics:<br><hr><br>"
            reply += f"Total Cases: <strong>{showdata['data']['summary']['total_cases']}</strong><br>"
            reply += f"Active Cases: <strong>{showdata['data']['summary']['active_cases']}</strong><br>"
            reply += f"Deceased: <strong>{showdata['data']['summary']['deaths']}</strong><br>"
            reply += f"Recovered: <strong>{showdata['data']['summary']['recovered']}</strong><br>"
        else:
            reply = "If you need statistics for a country, try typing<br><i>status country country</i>"
    elif "world" in inp and "status" in inp:
        showdata = worlddata()
        reply = "Showing <strong>Global</strong> statistics:<br><hr><br>"
        reply += f"Total Cases: <strong>{showdata['data']['summary']['total_cases']}</strong><br>"
        reply += f"Active Cases: <strong>{showdata['data']['summary']['active_cases']}</strong><br>"
        reply += f"Deceased: <strong>{showdata['data']['summary']['deaths']}</strong><br>"
        reply += f"Recovered: <strong>{showdata['data']['summary']['recovered']}</strong><br>"
    else:
        reply = "Sorry, I didn't get that. Try rephrasing your question?"
        
    
    return JsonResponse({"r":reply}, safe= False)