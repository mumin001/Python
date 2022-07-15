# -*- coding: utf-8 -*-
"""
Created on Sat Jul  9 23:27:32 2022

@author: User
"""

# mehmonlar = ['Ali', 'Vali', 'Xusan', 'Xusan', 'olim']
# for mehmon in mehmonlar:
#     print("Salom", mehmon)
#       print("Hayr", mehmon)

# mehmonlar = ['Ali', 'Vali', 'Xusan', 'Xusan', 'olim']
# for mehmon in mehmonlar:
#     print(f"Hurmatli {mehmon}, sixni 20 Dekabir kuni nahorga oshga xurmat bilan taklift etamiz")
#     print("Hurmat bilan palonchyevlar oilasi\n")

# sonlar = list(range(1,11))
# for son in sonlar:
#     print(f"{son} ning kivadrati {son**2} ga teng")

# sonlar = list(range(11))
# sonlar_kvadrati =[]
# for son in sonlar:
#     sonlar_kvadrati.append(son**2)
    
#print(sonlar)
# print(sonlar_kvadrati)

dostlar =[]
print("5 ta eng yaqin do'stlaringiz kim?")
for n in range(5):
    dostlar.append(input(f"{n+1}-do'stlaringiz ismini kiriting: "))
print(dostlar)    