
print("Program starting.")
print("String comparisons")
sana = input("Insert first word: ")
kirjain = input("Insert a character: ")
if kirjain in sana:
    print(f'Word "{sana}" contains character "{kirjain}"')
else:
    print(f'Word "{sana}" doesn\'t contain character "{kirjain}"')
toka_sana = input("Insert second word: ")
if toka_sana == sana:
    print(f'Both inserted words are the same alphabetically, "{sana}"')
elif toka_sana < sana:
    print(f'The second word "{toka_sana}" is before the first word "{sana}" alphabetically.')
else:
    print(f'The first word "{sana}" is before the second word "{toka_sana}" alphabetically.')
print("Program ending.")
