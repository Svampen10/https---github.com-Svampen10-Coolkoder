
alfabet= "ABCDEFGHIJKLMNOPQRSTUVWXYZÅÄÖABCDEFGHIJKLMNOPQRSTUVWXYZÅÄÖ"
meddelande = input("skriv ett meddelandet som ska krypteras: ")
meddelande = meddelande.upper()
nyckel = int(input("välj ett tal mellan 1 och 28 "))
krypteradSträng = ""

for aktuelltTecken in meddelande:
    position = alfabet.find(aktuelltTecken)
    nyPosition = position + nyckel
    krypteradSträng = krypteradSträng + alfabet[nyPosition]

print ("det krypterade meddelandet är", krypteradSträng)
