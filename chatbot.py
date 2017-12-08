import requests
import json
from wit import Wit 
from geopy.geocoders import Nominatim

machine_connecte = "vide"

def answer(request):
    client = Wit("LBJAOO6J4BBVAGX75QDEF3GUBJMDKZDP")
    
    global machine_connecte
    
    #message = requests.GET.__getitem__("message")
    message = request
    analyse = client.message(message)

    #print(analyse)

    #print(machine_connecte)

    headers = {
        'Authorization': 'JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJvcmlnX2lhdCI6MTUxMjY3Nzk1NywiZXhwIjoxNTEzMjgyNzU3LCJlbWFpbCI6InVzZXJzQG51aXRkZWxpbmZvLmNvbSIsInVzZXJuYW1lIjoidXNlcnNAbnVpdGRlbGluZm8uY29tIiwidXNlcl9pZCI6NjUwNn0.chrs_BCFapaQ7U4bjwDB9K4C8CcPhSrucoOHpTOVYQc'
    }
    if 'intent' not in analyse['entities']:
        answer = "Désolé je n'ai pas compris votre question"
    else:
        intent = analyse['entities']['intent'][0]['value']
        if intent == 'Connection':
            if 'nom_machine' not in analyse['entities']:
                answer = "Je ne trouve pas la machine à laquelle vous voulez vous connecter."
            else:
                params = {'object_type': 'machine', 'q': analyse['entities']['nom_machine'][0]['value']}
                res = requests.get('http://api.mephisto.optimdata.io/search?', params=params, headers=headers)
                if len(json.loads(res.text)) > 1:
                    answer = "Ok, peux-tu préciser, il y a " + len(json.loads(res.text)) + " machines qui correspondent à ce résultat:"
                    for machines in json.loads(res.text):
                        answer += " " + machines
                else:
                    machine_connecte = json.loads(res.text)[0]['object_id']
                    answer = "Vous êtes bien connecté à " + json.loads(res.text)[0]['name']
        elif intent == 'Liste':
            params = {'object_type': 'machine'}
            res = requests.get('http://api.mephisto.optimdata.io/search?', params=params, headers=headers)
            answer = "La liste des machines disponibles est la suivante :"
            for elements in json.loads(res.text):
                answer += " " + elements["name"] + ","
        elif intent == 'Documentation':
            if 'nom_machine' not in analyse['entities']:
                res = requests.get('http://api.mephisto.optimdata.io/api/machines/'+str(machine_connecte), headers=headers)
            else:
                res = requests.get('http://api.mephisto.optimdata.io/api/machines/'+  analyse['entities']['nom_machine'][0]['value'], headers=headers)
            answer = "Voici la/les documentation(s) de la machine :"
        elif intent == 'Geolocalisation':
            if 'nom_machine' not in analyse['entities']:
                res = requests.get('http://api.mephisto.optimdata.io/api/machines/' + str(machine_connecte), headers=headers)
            else:
                res = requests.get('http://api.mephisto.optimdata.io/api/machines/'+  analyse['entities']['nom_machine'][0]['value'], headers=headers)
            #print(res.text)
            longitude = json.loads(res.text)['longitude']
            latitude = json.loads(res.text)['latitude']
            geolocator = Nominatim()
            location = geolocator.reverse((latitude, longitude))
            answer = "La machine se trouve à l'adresse suivante : " + location.address
        elif intent == 'Liste_valeurs':
            if 'valeur' not in analyse['entities']:
                res = requests.get('http://api.mephisto.optimdata.io/api/machines/'+str(machine_connecte) + '/properties', headers=headers)
                answer = "Les propriétés de cette machine sont : "
                for elements in json.loads(res.text):
                    answer+= elements["name"]
            else:
                res = requests.get('http://api.mephisto.optimdata.io/api/machines/'+str(machine_connecte) + '/properties', headers=headers)
                property = analyse['entities']['valeur'][0]['value']
                if property == 'erreur' or property == '**error**':
                    pk = '0'
                    error = 'none'
                    for elements in json.loads(res.text):
                        if 'error' in elements['name']:
                            err = requests.get('http://api.mephisto.optimdata.io/api/machines/'+str(machine_connecte) + '/properties/' + elements['pk'], headers=headers)
                            if json.loads(err.text)['ts'] > pk:
                                pk = json.loads(err.text)['ts']
                                error = elements['name']
                        answer = 'La dernière erreur connue est survenue en date de' + ts + ' et c\'est l\'erreur' + error
                elif property == 'erreur critique':
                    pk = '0'
                    error = 'none'
                    for elements in json.loads(res.text):
                        if 'critical error' in elements['name']:
                            err = requests.get('http://api.mephisto.optimdata.io/api/machines/'+str(machine_connecte) + '/properties/' + elements['pk'], headers=headers)
                            if json.loads(err.text)['ts'] > pk:
                                pk = json.loads(err.text)['ts']
                                error = elements['name']
                        answer = 'La dernière erreur critique connue est survenue en date de' + ts + ' et c\'est l\'erreur' + error 
                for elements in json.loads(res.text):
                    pk = '0'
                    name = 'none'
                    for elements in json.loads(res.text):
                        if 'error' in elements['name']:
                            err = requests.get('http://api.mephisto.optimdata.io/api/machines/'+str(machine_connecte) + '/properties/' + elements['pk'], headers=headers)
                            if json.loads(err.text)['ts'] > pk:
                                pk = json.loads(err.text)['ts']
                                name = elements['name']
                        answer = 'La dernière valeur connue en date de' + ts + ' et de' + name 
    return answer

while True:
    text = input("User >  ")
    print("Chatbot > " + answer(text))