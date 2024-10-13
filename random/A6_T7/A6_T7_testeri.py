from pathlib import Path
import os

ROOT_FOLDER = Path(os.path.dirname(os.path.realpath(__file__)))
files = ["1-discipline.txt", "2-jauheliha.txt", "3-sipuli.txt", "4-peruna.txt"]
contents = [
    """Part 0 - Year of the Four Emperors:

In AD 68, after Nero's death, Rome plunged into chaos.
With no clear heir, the empire saw rapid power struggles.
Galba took the throne first, followed by Otho, Vitellius, and finally Vespasian,
each battling for control in what became the Year of the Four Emperors.
""",
    """Ruskista jauheliha ja hienonnettu sipuli rasvassa pannulla.
Ripottele joukkoon vehnäjauho.
Paista muutama min.
""",
    """Murenna päälle liemikuutio.
Lisää vesi ja pippurit.
Sekoita tasaiseksi ja kiehauta.
""",
    """Lisää ruokakerma. Keitä 5 min.
Viimeistele kastike halutessasi hienonnetulla persiljalla.
Tarjoa keitettyjen perunoiden ja salaatin kanssa.
https://www.youtube.com/watch?v=dQw4w9WgXcQ
""",
]

for i, file in enumerate(files):
    try:
        fp = ROOT_FOLDER / file
        assert fp.exists()
    except AssertionError:
        print(f"{file} tiedosto puuttuu")
for i, file in enumerate(files):
    fp = ROOT_FOLDER / file
    teksti = fp.read_text(encoding="utf-8")
    assert teksti == contents[i], f"{file} väärä sisältö:\n{teksti}\nvs\n{contents[i]}"

print("Kaikki testit läpäisty")
