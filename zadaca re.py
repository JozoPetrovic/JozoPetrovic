import re

regex = "^lj[0-5]+\s.*s$"

while 1:
    unos = input("Unesite ime:")
    rezultat = re.match(regex,unos)
    if rezultat:
        break
    else:
        print("Pogresan unos!")
print("Uspješno")