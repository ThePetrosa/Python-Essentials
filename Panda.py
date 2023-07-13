import pandas as pd
titulos = pd.read_csv('PANDA/titles.csv' )
print(titulos.head(100))
print("\n"*2)
elenco = pd.read_csv('PANDA/cast.csv', encoding='utf-8')
print(elenco.head(10))
print (len(titulos))

print(titulos[titulos.title == "Romeo and Juliet"].sort_values('year').head(5))

print(titulos[titulos.title.str.contains("Exorcist")].sort_values('year'))

print(len( titulos[titulos.year == 1980] ))

print(len( titulos[titulos.year == 2020] ))

print(len( titulos[ (titulos.year >= 1950) & (titulos.year <= 1959) ] ))
print(len( titulos[ titulos.year // 10 == 195] ))

print(titulos[ titulos.title == "Batman"])
print(titulos[ titulos.title == "Start Wars"])
print(titulos[titulos.title.str.contains("Star War")].sort_values('year'))
print(titulos[ titulos.year == 1973].head(1))
print(len( titulos[ (titulos.year >= 1980) & (titulos.year <= 2000)]))

print(len( elenco[elenco.title == "The Godfather"] ))

c = elenco[elenco.title == "The Godfather"]
c = c[c.n.isnull()]
print(len( c ))
