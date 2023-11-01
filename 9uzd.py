"""
Uzdevumā izmantot funkciju map(), kura  komandu izpilda 
katram saraksta(virknes) loceklim.

"""

saraksts1=[2, 6, 7, 4]
sarakts2=[]
def pieskaitit(skaitlis):
    return skaitlis + 2

saraksts2=list(map(pieskaitit,saraksts1))
print(saraksts2)