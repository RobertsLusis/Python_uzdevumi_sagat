"""
Izmantojot map() funkciju izveidot no diviem sarakstiem saliktnei.


"""

saraksts1 = [1, 2, 3]
saraksts2 = ['a', 'b', 'c']
 
# Izveidojam funkciju, kas apvieno divus elementus pāriem
def apvienot(pari):
    return f"{pari[0]}{pari[1]}"
 
# Izmantojam map() un zip() funkcijas, lai izveidotu saliktni
saliktnes = list(map(apvienot, zip(saraksts1, saraksts2)))
 
print(saliktnes)
 