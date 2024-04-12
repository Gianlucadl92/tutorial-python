import json

dizionario = {
    "nome": "Marco",
    "cognome" : "Rossi",
    "eta" : 30
}

json_dizionario = json.dumps(dizionario)
print(json_dizionario)