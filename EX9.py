def analyse_texte(texte):
    nbr_mot = len(texte.split())
    nbr_characters = len(texte)
    return{"nombre_mots": nbr_mot,  "nombre_characters": nbr_characters}

texte = "Cut the last breath from them"
test = analyse_texte(texte)
print("Analyse du texte :", test)