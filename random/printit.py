from timeit import timeit
import os

testi = "testi"


# 1 Hitain, huomattavasti hitaampi pitkillä teksteillä
def printti():
    for i in range(0, len(testi)):
        if i == len(testi) - 1:
            print(testi[i], end="\n")
        else:
            print(testi[i], end=" ")


# 2 Nopein, tekstin pituudelle ei suurta merkitystä
def lista():
    tuloste = []
    for i in testi:
        tuloste.append(i)
    print(" ".join(tuloste))


# 3 Aavistuksen hitaampi kuin 4/5/2, tekstin pituudella pieni merkitys
def ketjuttaminen():
    tuloste = ""
    for i in testi:
        tuloste += i + " "
    tuloste = tuloste[:-1]
    print(tuloste)


# 4 Toiseksi nopein, tekstin pituudelle ei suurta merkitystä, kuluttaa aavistuksen vähemmän muistia kuin #5
def generaattori():
    print(" ".join(x for x in testi))
    # y = 5
    # print(" ".join(str(x) for x in range(0, len(testi)) if x != y))
    # print(" ".join(str(x) for x in range(0, len(testi)) if x != y and x < y))


# 5 Toiseksi nopein, tekstin pituudelle ei suurta merkitystä, avistuksen nopeampi kuin #4
def list_comprehension():
    print(" ".join([x for x in testi]))


testit = [printti, lista, ketjuttaminen, generaattori, list_comprehension]
tulokset = []
num_iterations = 10000

for func in testit:
    time_taken = timeit(func, number=num_iterations)
    kesto = time_taken / num_iterations
    tulos = f"{kesto* 1_000_000:1.0f} µs"
    tulokset.append(tulos)
    os.system("cls" if os.name == "nt" else "clear")
print(
    "\n".join(
        f"{testit[x].__name__}: {tulokset[x]}" for x in range(0, len(tulokset))
    )
)
