import random
if __name__ == "__main__":
    print("Schere, Stein oder Papier!")

    def eingabe(values):
        eingabe = input("Schere, Stein oder Papier: ")
        if eingabe in values:
            return eingabe
        else:
            print("Falsche Eingabe!")

    def weiter():
        while True:
            inp = input("Weiterspielen? [y/n]")
            if inp == 'y':
                return True
            elif inp == 'n':
                print("Das Spiel ist vorbei!")
                return False

    def compare(spieler, bot, value, result):
        print("Bot:" + bot)
        print("Spieler:" + spieler)
        erg = value[spieler] - value[bot]
        return result[erg % 3]

    status = True
    while status:
        if status == 1:
            werte = ["Schere", "Stein", "Papier"]
            comparevalues = {"Schere": 2, "Stein": 0, "Papier": 1}
            result = ["Unentschieden", "Gewonnen", "Verloren"]
            spielerwahl = eingabe(werte)
            bot = random.choice(werte)
            print(compare(spielerwahl, bot, comparevalues, result))
            status = weiter()