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

errors = []

for file in files:
    fp = ROOT_FOLDER / file
    try:
        assert fp.exists(), f"{file} tiedosto puuttuu"
    except AssertionError:
        errors.append(f"{file} tiedosto puuttuu")
for i, file in enumerate(files):
    fp = ROOT_FOLDER / file
    if fp.exists():
        try:
            teksti = fp.read_text(encoding="utf-8")
            assert teksti == contents[i]
        except AssertionError:
            errors.append(f"{file} väärä sisältö:\nOdotettu:\n{repr(contents[i])}\nLuettu:\n{repr(teksti)}")
print(f"Testit suoritettu: {len(errors)} Virhettä")
for e in errors:
    print("------\n"+e)
