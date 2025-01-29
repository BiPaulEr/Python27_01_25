import requests

response = requests.get("https://httpbin.org/get")

if response.status_code == 200:
    print("REquete reussi")
    print(response.json())
else:
    print("Requete echoue")