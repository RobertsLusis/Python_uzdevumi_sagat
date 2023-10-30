"""
Uzrakstiet programmu definējot klasi,lai veselu 
skaitli pārveidotu par romiešu ciparu.

"""

class AAA:
    def __init__(self):
        #vardnica
        self.romiesu={
            1:"I",
            4:"IV",
            5:"V",
            9:"IX",
            10:"X",
            40:"XL",
            50:"L",
            90:"XC",
            100:"C",
            400:"CD",
            500:"D",
            900:"CM",
            1000:"M"
        }
    def uz_romu(self, num):
        result= "" #result ir virkne
        for value, sk in sorted(self.romiesu.items(), key=lambda x:x[0], reverse=True):
            while num>=value:
                result+=sk
                num-=value
            return result

skaitlis=1000 #definēju mainīgo
konvertet=AAA()             #ir izveidot objekts
romiesu=konvertet.uz_romu(skaitlis) 
print(f"{skaitlis} romiešu ciparos ir {romiesu}")