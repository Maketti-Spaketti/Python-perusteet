player_progress.txt formaatti:
```
	current_location;next_location;passphrase
	0;1;qvfpvcyvar
	1_{SalattuSalasana}.gkg tiedoston ensimmäinen rivi, sisältää 1;2;SalattuSalasana
	2_{SalattuSalasana}.gkg tiedoston ensimmäinen rivi, sisältää 2;3;SalattuSalasana
	...
	lopussa tyhjä rivi
```
Omassa ympäristössä täytyy aluksi luodate tiedosto joka sisältää `player_progress.txt`:in kaksi ensimmäistä riviä + 1 tyhjä rivi.  
Loput rivit lisätään `player_progress.txt`:iin seuraavien ajojen aikana (1 per ajo).
Jos haluat tarkistaa onko tiedosto jo olemassa voit käyttää (ei tarpeen jos luot tiedoston tekstieditorilla)    
```.py
import os
if not os.path.exists("player_progress.txt"):
	#Luo tiedosto
```
Testiympäristössä tiedosto on jo valmiiksi luotu, joten sitä ei tarvitse luoda koodissa.  

Aina kun ohjelmaa aletaan suorittaa pitää lukea `player_progress.txt`:n viimeinen ei tyhjä rivi,  
joka on muotoa `x;y;XXXXXXXXX` esim `0;1;qvfpvcyvar`, tämä jaetaan kolmeen muuttujaan; NykyinenSijainti, SeuraavaSijainti, ja SalattuSalasana.  
SalattuSalasana muuttujasta tehdään myös SalaamatonSalasana muuttuja dekryptaamalla se.  

SalaamatonSalasana:sta pitää vielä tehdä muokattu versio vartijoille:  
Lisäämällä siihen; iso alkukirjain (`.capitalize()`), lainausmerkit, ja huutomerkki.  

Seuraavaksi luetaan {SeuraavaSijainti}_{SalattuSalasana}.gkg tiedosto:  
Sen ensimmäinen rivi lisätään `player_progress.txt` tiedostoon loppuun avaamalle se "a"(append) tilassa.  
Tämä luettu rivi on muotoa `1;2;XXXXXXX`, jotka ovat seuraavalla ajokerralla käytettäviä arvoja.  

Lopun tekstin salaus puretaan ja tallennetaan `{SeuraavaSijainti}-{SalaamatonSalasana}.txt` tiedostoon.  
* SeuraavaSijainti ei ole muuttunut tässä välissä, vaan on ensimmäisellä ajokerralla 1
* SalaamatonSalasana on myöskin sama mitä huudeltiin aikaisemmin vartijoille, mutta ilman niitä ylimääräisiä muotoiluja
* Erota sijainti ja salasana tämän tiedoston nimessä väliviivalla

A6_T7 zipistä löytyy harjoitus .gkg tiedostot joilla voit tarkistaa ohjelman toiminnon.  
Zipistä löytyy myös A6_T7_testeri.py, jolla voi tarkistaa että .txt tiedostot ovat olemassa ja niiden sisältö on oikea  
