"""
Uzrakstiet Python programmu, lai diviem sarakstiem noteikti atšķirību.
Izmantojiet funkciju map().
"""

# Funkcija, kas atgriež atšķirību starp diviem elementiem
def find_difference(a, b):
    return a - b
 
# Sākotnējie saraksti
saraksts1 = [1, 2, 3, 4, 5]
saraksts2 = [3, 4, 5, 6, 7]
 
# Izmantojot map(), izveidojam jaunu sarakstu ar atšķirībām
atšķirības = list(map(find_difference, saraksts1, saraksts2))
 
# Izdrukājam rezultātu
print(atšķirības)