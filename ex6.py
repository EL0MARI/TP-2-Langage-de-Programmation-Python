etudiant ={
    "nom" : "mohamed",
    "age" : 19,
    "notes":[15,19,17,20],
    "actif": True
}

print("Les cle du dictionnaire : ",etudiant.keys())
moyenne = sum(etudiant["notes"]) / len(etudiant["notes"])
print("la moyenne des notes est : ",moyenne)

etudiant["moyennes"] = moyenne

print("dictionnaire complet : ",etudiant)
