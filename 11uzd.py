"""
Uzrakstiet Python programmu, lai trīskāršotu visus dotā veselo skaitļu saraksta skaitļus.
Izmantojiet Python map() funkciju.
"""

saraksts = [1, 2, 3, 4, 5]

def triskarsot(skaitlis):
    return skaitlis * 3

rezultats = map(triskarsot, saraksts)
 
rezultata_saraksts = list(rezultats)
 
print(rezultata_saraksts)