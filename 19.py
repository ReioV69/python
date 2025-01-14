import json

kl12 = 0
kl11 = 0
kl10 = 0

with open("haridustulemused.json", 'r', encoding='utf-8') as file:
    opilased = json.load(file)

for opilane in opilased:
    if opilane["klass"] == "12":
        kl12 += 1
        print(opilane['nimi'])
        for tegevus in opilane['tegevused']:
            print(tegevus)
        print("-----------------")
    if opilane["klass"] == "11":
        kl11 += 1
    if opilane["klass"] == "10":
        kl10 += 1   


print(f"12. klassis on {kl12} õpilast")
print(f"11. klassis on {kl11} õpilast")
print(f"10. klassis on {kl10} õpilast")