player_progress.txt formaatti:
```
	current_location;next_location;passphrase
	0;1;qvfpvcyvar
	1_{salattuSalasana}.gkg tiedoston ensimmäinen rivi, sisältää 1;2;salattuSalana
	2_{salattuSalasana}.gkg tiedoston ensimmäinen rivi, sisältää 2;3;salattuSalana
	...
	lopussa tyhä rivi
```
Omassa ympäristössä luodaan alussa tiedosto jossa on vain 2 ensimmäistä riviä (+tyhjä rivi), mutta loput lisätään seuraavien ajojen aikana.  
Jos haluat tarkistaa onko tiedosto jo olemassa voit käyttää  
```.py
import os
if not os.path.exists("player_progress.txt"):
	#Luo tiedosto
```
Testiympäristössä tiedosto on jo valmiiksi luotu, joten voit ohittaa edellisen vaiheen.


Ensimmäisenä luetaan viimeinen (ei tyhjä) rivi player_progress.txt tiedostosta  
Ja jaetaan se nykyinenSijainti, seuraavaSijainti, ja salattuSalasana muuttujiin  
Tehdään myös salaamatonSalasana muuttuja purkamalla salattuSalasanasta salaus  

salaamatonSalasana:sta pitää vielä tehdä muokattu versio vartijoille:  
Iso alkukirjain (`.capitalize()`), lainausmerkit, ja huutomerkki

Seuraavaksi luetaan {seuraavaSijainti}_{salattuSalasana}.gkg tiedosto:  
Sen ensimmäinen rivi lisätään player_progress.txt tiedostoon loppuun avaamalle se "a"(append) tilassa.  
Tämä luettu rivi sisältää `1;2;XXXXXXX` missä X on salattu salasana.

Lopun tekstin salaus puretaan ja tallennetaan `{seuraavaSijainti}-{salaamatonSalasana}.txt` tiedostoon.
* seuraavaSijainti ei ole muuttunut, eli ekassa ajossa on 1
* salaamatonSalasana on myöskin sama mitä huudeltiin aikaisemmin vartijoille, mutta ilman niitä ylimääräisiä muotoiluja
* Erota sijainti ja salasana tämän tiedoston nimessä väliviivalla

A6_T7 zipistä löytyy harjoitus .gkg tiedostot joilla voit tarkistaa ohjelman toiminnon.  
Zipistä löytyy myös A6_T7_testeri.py testiri joka tarkistaa että .txt tiedostot on luoto oikein ja sisältävät oikean tekstin
