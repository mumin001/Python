# -*- coding: utf-8 -*-
"""
Created on Fri Jul 15 02:36:18 2022

@author: User
"""

import re
from uzwords import words

word1 = "темир"
word2 = "томир"
word3 = "тулпор"

andoza = "^т...р$"

print(re.match(andoza, word1))
print(re.match(andoza, word2))
print(re.match(andoza, word3))


andoza = "^а...й$"
matches = []
for word in words:
    if re.match(andoza, word):
        matches.append(word)

print(matches)

## Emailni ajratib olish
matn = """Maqolalar  2020-yilning 20-martiga qadar rtmkonferensiya2021@mail.ru elektron pochtasida qabul qilinadi.
Quyidagi yo'nalishdagi maqolalar qabul qilinadi:
 Aniq va tabiiy fanlarni zamonaviy pedagogik texnologiyalar asosida uqitish  metodikasi.
 Umumtalim  fanlarini uqitishda  STEAM yondashuvning urni va ahamiyati. """

andoza = "[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+"
email = re.findall(andoza, matn)
print(email)

# Kuchli parolni tekshirish
andoza = "^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$ %^&*-]).{8,}$"
msg = "Yangi parol kiriting"
msg += "(kamida 8 belgidan iborat, kamida 1 ta lotin bosh harf, 1 ta kichik harf, "
msg += "1 ta son va 1 ta maxsus belgi bulishi kerak): "

while True:
    password = input(msg)
    if re.match(andoza, password):
        print("Maxfiy suz qabul qilindi")
        break
    else:
        print("Maxfiy suz talabga javob bermadi")