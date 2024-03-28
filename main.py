import requests
api_url = 'http://numbersapi.com/43'
response = requests.get(api_url)
print(response.text)