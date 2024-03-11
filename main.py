import requests
import json

url = 'https://api.languagetool.org/v2/check'
data = {
  'text': 'henlo',
  'language':'auto'
}
response = requests.post(url, data=data)

results = json.loads(response.text)
print(results)
