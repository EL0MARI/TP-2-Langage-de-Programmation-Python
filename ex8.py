personne = ("Alice", 25, "Paris")
print(personne)
print(personne[0])
print(personne[1])
#personne[0] = "Mohamed"

#"TypeError: 'tuple' object does not support item assignment" car les tuples reste inchangable 
personne1 = ("Mohamed", personne[1], personne[2])
print(personne1)