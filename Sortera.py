

kvinna = ["en forskare","en drottning","ett sto","en präst"]
man = ["en konstapel","en luffare","farfar Frans","en mördare"]
plats = ["på en båt","på pluto","i en läskig grotta med fladdermös"]
honbar = ["en batman kostym","rosa änglavingar","en svart sopsäck"]
hanbar = ["en banan kostym","en taco kostym","ett älghuvud","en prickig badhandduk"]
honsa = ["vem är du","hur många ärter har du i örat","men varför"]
hansa = ["hej svejs!","käka inte kråkor!","har du sett sylten"]
följd = ["fred på jorden","kaos","att en jättefot krossadedem","orkan"]
världsa = ["vilket nys!","ja det är trendigt med ostbågar","jag smälter"]


import random
while True:
    print(random.choice(kvinna), "mötte", random.choice(man), random.choice(plats))
    print("hon hade på sig", random.choice(honbar))
    print("han hade på sig", random.choice(hanbar))
    print("hon sa,", random.choice(honsa))
    print("han sa,", random.choice(hansa))
    print("följande blev:", random.choice(följd))
    print("värld sa:,", random.choice(världsa))

    print()
    input("tryck på retur och kör igen.")
    print()