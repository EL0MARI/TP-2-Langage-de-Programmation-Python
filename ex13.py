nom = input("entrez le nom de l'etudiant :")
prenom = input("entrez le prenom de l'etudiant :")
age = int(input("entrez le age de l'etudiant :"))

print("\n--------entrez les notes ----------")
notes1 = float(input("entrez la 1 ere note (sur 20) : "))
notes2 = float(input("entrez la 2 eme note (sur 20) : "))
notes3 = float(input("entrez la 3 eme note (sur 20) : "))

notes = [notes1,notes2,notes3]

etudiant = {
    "nom" : nom,
    "prenom" : prenom,
    "age" : age,
    "notes" : notes
}
moyenne = sum(etudiant["notes"]) / len(etudiant["notes"])
etudiant["admis"] = (moyenne >= 10)


print("\n===================================RAPPORT DE L'ETUDIANT=====================================\n")
print(f"Nom complet : {etudiant['prenom']} {etudiant['nom']}")
print(f"Âge         : {etudiant['age']} ans")
print(f"Notes       : {etudiant['notes']}")
print(f"Moyenne     : {moyenne:.2f} / 20")
if etudiant["admis"]:
    
    print("Statut      : admis ✓")
else:
    print("Statut      : non admis")