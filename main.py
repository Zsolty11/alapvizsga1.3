'''
Nyitvatartás.
Egy bolt pontban reggel nyolc órakor nyit, és pontban délután tizenhat órakor zár be – azaz 8:00‑kor már nyitva van és 16:00-kor már nincs nyitva.
A program kérjen be egy egész órát jelző számot a felhasználótól, majd írja ki, hogy a megadott időpontban nyitva van-e a bolt! 
Amennyiben igen, akkor azt is írja ki, hogy mennyi idő van még zárásig, azaz hány egész óra áll rendelkezésre odaérni a boltba! 
A program üzeneteinek megfogalmazásában kövesse az alábbi mintát:
-----
Hány óra van most? 8
Nyitvatartás.
Ennyi órád van még odaérni: 8
-----
Hány óra van most? 7
A bolt zárva van.
-----
Hány óra van most? 17
A bolt zárva van.
-----
Hány óra van most? 16
A bolt zárva van.
-----
Hány óra van most? 12
A bolt nyitva van.
Ennyi órád van még odaérni: 4
'''

egeszOra = int(input("Hány óra van most? "))

if egeszOra > 8 and egeszOra < 16 :
  print("A bolt nyitva van.")
  print(f"Ennyi órád van még odaérni:{16-egeszOra}")
else:
  print("A bolt zárva van.")

