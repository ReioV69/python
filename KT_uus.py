import requests

sõna = input("Sisesta sõna: ")
url = "https://dummy-json.mock.beeceptor.com/roles"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    leitud = False
    
for item in data:
    if sõna.lower() in item["description"].lower():
        print(f"Kirjeldus: {item['description']}")
        print(f"Nimi: {item['name']}")
        leitud = True
if not leitud:
    print("Sellist ei leitud")
