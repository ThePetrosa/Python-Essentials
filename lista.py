lista1=[]
lista2=[]
lista3=[]
lista4=[]
lista=["R1", "R2", "R3",
       "S1", "S2", "S3",
       "AP1", "AP2", "AP3",
       "c1", "c2", "c3"]
for elemento in lista:
    if "R" in elemento:
        lista1.append(elemento)
for elemento in lista:
    if "S" in elemento:
        lista2.append(elemento)
for elemento in lista:
    if "c" in elemento:
        lista3.append(elemento)
for elemento in lista:
    if "AP" in elemento:
        lista4.append(elemento)
