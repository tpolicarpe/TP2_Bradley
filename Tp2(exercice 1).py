import csv
import json

#Fichier lecture(json)
with open("data.json","r") as dj:
    data = json.load(dj)
    print(f"Voici le contenue dans le fichier data.json\n {data}")

#Fichier csv
ajout_debut = ["reel","imaginaire"]

#ecrire dans le fichier csv
with open("fichier.csv","w",newline= "") as fs:
    json_to_csv = csv.writer(fs)
    json_to_csv.writerows(data)

#ajout de nouvelle donné
    new_fichier = [ajout_debut] + data

with open ("fichier.csv","r",newline="") as fs:
    for ligne in new_fichier:
        print(*ligne,sep=",")









