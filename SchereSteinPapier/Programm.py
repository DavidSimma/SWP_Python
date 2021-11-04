import random
print("Schere, Stein oder Papier")
sachen = {1:"Schere", 2:"Stein", 3:"Papier"}
ein = input("Ihre Wahl: ")
ein2 = 0

if ein == "Schere":
    ein2 = 1
if ein == "Stein":
    ein2 = 2
if ein == "Papier":
    ein2 = 3

gegner = random.choice(list(sachen.keys()))
if ein2 > gegner:
    print("Gewonnen")
elif ein2 == 1 & ein2 == 3:
    print("Verloren")
elif ein2 == gegner:
    print("unentschieden")
else:
    print("Verloren")