mixte = [1, "Python", 3.14, True]
for i in range(0,len(mixte)):
    print(type(mixte[i]))
mixte.append("Mohamed")
print(mixte)
mixte.remove(1)
print(mixte)
s=0
for i in range(0,len(mixte)):
    if(type(mixte[i]) == int or type(mixte[i]) == float):
        s = s+mixte[i]
print(s)
