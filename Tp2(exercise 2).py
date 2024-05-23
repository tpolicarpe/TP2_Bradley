import csv
def changerpkm(pokemon):
    dict_stats = []
    with open("pokemon.csv", encoding="utf-8") as FichierCSV:
        lecteur_csv = csv.reader(FichierCSV)

        for ligne in lecteur_csv:
            if ligne[0] == pokemon:
                for element in ligne:
                    if element != pokemon:
                        dict_stats.append(int(element))
                break

    print(pokemon,":", dict_stats)

# Test de la fonction
changerpkm("Pikachu")
changerpkm("Charizard")
changerpkm("Magikarp")








