import requests
nimi = input("Sisesta nimi: ")
url = f"https://dummyjson.com/users"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()

for users in data['users']:
    if users['firstName'].lower() == nimi.lower():
        print(f"Nimi: {users['firstName']} {users['lastName']}")
        print(f"Sugu: {users['gender']}")
        print(f"Vanus: {users['age']}")
        print(f"Kaal: {users['weight']} kg")
        print(f"Pikkus: {users['height']} cm")
        print(f"Email: {users['email']}")
        print(f"Telefon: {users['phone']}")
        print(f"IP address: {users['ip']}")
        break
else:
    print("Sellist kasutajat ei leitud")
