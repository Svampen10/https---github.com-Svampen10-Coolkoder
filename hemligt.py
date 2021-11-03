zyrkoOrdlista = {"vi": "nrrrr", "kommer": "billlk", "som": "zonnnrrr","vänner": "agh", "hej": "kodig", "får": "zank","jag": "az", "låna":"liftit",
"lite": "sniift", "raketbränsle": "upgoman", "tack": "selpin", "snälla": "baaaaaaaarn", "skjuta": "flabil", "inte": "sarrk", "välkommen": "turm",
"våra": "mundu", "kamrater": "marangin", "från": "bap", "rymden": "birp", "vara": "dripppp"}


svenska = input ("skriv ett svenskt ord som ska översätta till zyrko: ")
svenskaOrd = svenska.lower().split()

zyrkoOrd = []
for ord in svenskaOrd:
    if ord in zyrkoOrdlista:
        zyrkoOrd.append(zyrkoOrdlista[ord])
    else:
        zyrkoOrd.append(ord)
print ("blir på zyrko:"," " .join(zyrkoOrd))