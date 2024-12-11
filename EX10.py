def fusionner_dicts(dict1, dict2):
    fusion = dict1.copy()
    for cle, valeur in dict2.items():
        if cle in fusion:
            fusion[cle] += valeur
        else:
            fusion[cle] = valeur
    return fusion

dict1 = {'a': 10, 'b': 15, 'c': 30}
dict2 = {'a': 5, 'd': 10, 'b': 20}
print("Dictionnaire fusion :", fusionner_dicts(dict1, dict2))
