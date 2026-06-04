import requests
url = "https://official-joke-api.appspot.com/random_joke"
response = requests.get(url)
if response.status_code == 200: 
    data = response.json()
    print("random joke")
    print()
    print(data['setup'])
    print(data['punchline'])
else:
    print("request invalid")
