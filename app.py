import http.client
import os
import requests
import json
import csv
import pandas as pd
from base64 import b64encode

conn = http.client.HTTPSConnection("opendata.aemet.es")
print("Coloque su API KEY de opendata.aemet.es\n")
api = input()
print(f"API, {api} \n")
print("Coloque el código de la estación, ejemplo de la estación Hinojosa del Duque en Córdoba: 4267x\n")
estacion = input()
print("Tenga en cuenta que la siguiente API solo puede abarcar un rango de fechas de 5 anios \n")
print("a Continuación coloque la fecha de inicio con el siguiente formato: 2015-08-23 \n")
fechaIni=input()
print("a Continuación coloque la fecha de cierre con el siguiente formato: 2016-08-23 \n")
fechaFin=input()

headers = {
    'cache-control': "no-cache"
    }

conn.request("GET", "/opendata/api/valores/climatologicos/diarios/datos/fechaini/"+fechaIni+"T00:00:00UTC/fechafin/"+fechaFin+"T23:59:59UTC/estacion/"+estacion+"/?api_key="+api, headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))
#respuestaUrl=data.decode.datos

def serialize(self):
        return {
            "datos": self.datos,
            # do not serialize the password, its a security breach
        }

print("Ahora copie a continuación la URL sin comillas que aparece en la etiqueta datos, y péguela a continuación \n")
url2=input()
response2=requests.get(url2)
#x = requests.get(url2)
print(response2)
#print(response2.content)

# def save_users(users):
#     """
#         abre/crea el archivo users_lists.json y guarda
#         la lista de diccionarios que representan a los
#         usuarios.
#     """
#     with open(os.path.join(os.getcwd(), "users_lists.json"), "w") as users_file:
#         users_as_dictionaries = []
#         for user in users:
#             users_as_dictionaries.append(user.serialize())
#         json.dump(users_as_dictionaries, users_file)

## Write API Results to CSV
# Write to .CSV
f = open('newfile.json', "w")
f.write(response2.text)
f.close()



# with open('newfile.txt', 'r') as in_file:
#     stripped = (line.strip() for line in in_file)
#     lines = (line.split(",") for line in stripped if line)
#     with open('log.csv', 'w') as out_file:
#         writer = csv.writer(out_file)
#         writer.writerow(('title', 'intro'))
#         writer.writerows(lines)

df = pd.read_json (r'newfile.json')
df.to_csv (r'Final.csv', index = None)

print("""
archivo .cvs y .txt creados

App creada por:
Antonio Martínez
antonio_martinez88@hotmail.com
""")