"""
Doti divi saraksti.
Izmantojot funkciju map(), izdrukāt abu sarakstu vienādo( sakrīt elementi un to index) elementu summu.
"""

# Funkcija, kas apvieno elementus no diviem sarakstiem, ja tie sakrīt pēc indeksa
def combine_equal_elements(a, b):
    if a == b:
        return a

def summa (saskaitit):
    return vienādi_elementi + vienādi_elementi
# Sākotnējie saraksti
saraksts1 = [1, 2, 3, 4, 5]
saraksts2 = [3, 2, 1, 4, 7]
 
# Izmantojot map(), izveidojam jaunu sarakstu ar vienādajiem elementiem
vienādi_elementi = list(map(combine_equal_elements, saraksts1, saraksts2))
 

# Izdrukājam rezultātu
for elements in vienādi_elementi:
    if elements is not None:
        print(elements)