
import requests
url = "https://api.github.com/users/octocat"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print("\n user information")
    print(f"name : {data['name']}")
    print(f"location : {data['location']}")
    print(f"public repos : {data['public_repos']}")


else:
    print("request file")
