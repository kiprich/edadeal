import json
import requests

API_KEY = 'de3e15252d8a57de5514988f45a1e6e680d7aaed'
BASE_URL = 'https://suggestions.dadata.ru/suggestions/api/4_1/rs/suggest/%s'

def suggest(query, resource):
    url = BASE_URL % resource
    headers = {
        'Authorization': 'Token %s' % API_KEY,
        'Content-Type': 'application/json',
    }
    data = {
        'query': query
    }
    r = requests.post(url, data=json.dumps(data), headers=headers)
    return r.json()
    
print (suggest(u'москва хабаровская', 'address'))