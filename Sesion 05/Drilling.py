palabra = "paralelepipedo"

brk = []

for letter in palabra:
    brk.append(letter)

consonantes = []

for letter in brk:
    if letter not in ['a', 'e', 'i', 'o', 'u']:
        consonantes.append(letter)

final = ""

for letter in range(len(consonantes)):
    final = final+consonantes[letter]

print(final)