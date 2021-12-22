import random
import mysql.connector
import requests as requests

if __name__ == "__main__":
    mydb = mysql.connector.connect(host="localhost", user="user", password="user")
    mc = mydb.cursor()
    print("Schere, Stein, Papier, Lizard und Spock")

    def eingabe(values):
        eingabe = input("Schere, Stein, Papier, Lizard oder Spock: ").lower()
        if eingabe in values:
            return eingabe
        else:
            print("Falsche Eingabe!")
    def compare(spieler, bot, value, result):
        print("Bot:" + bot)
        print("Spieler:" + spieler)
        erg = value[spieler] - value[bot]
        print(spieler)
        print(bot)
        print(erg)
        print(result[erg % 5])
        return result[erg % 5]

    def weiter():
        while True:
            inp = input("Weiterspielen? [y/n]: ")
            if inp == 'y':
                return True
            elif inp == 'n':
                print("Das Spiel ist vorbei!")
                return False


    def getSqlCreateStatement():
        path = "C:/Users/simma/Desktop/Schulrepositories/SWP_Python/SchereSteinPapier/mysqlQuerry.txt"
        return open(path, "r")

    def speichern(spieler, erg):
        #ergebnis = mc.execute("SHOW DATABASES;")
        #if "schereSteinPapier" not in mc:
        #    print(mc)
        #    for x in getSqlCreateStatement():
        #        print(x)
        #        mc.execute(x)
        #else:
        mc.execute("use schereSteinPapier;")
        mc.execute("insert into results ("+spieler+","+erg+") values(1,1)")
        mydb.commit()

    def apiAufruf(username, anzScheren, anzStein, anzPapier, anzLizard, anzSpock, apiIP="http://127.0.0.1:5000"):
        url = apiIP + "/v1/updateRecord"
        url += "?username=" + str(username) + "&voteScissors=" + str(anzScheren) + "&voteRock=" + str(anzStein) + "&votePaper=" +\
               str(anzPapier) + "&voteSpock=" + str(anzSpock) + "&voteLizard=" + str(anzLizard)
        responseCode = 0
        try:
            response = requests.post(url, None)
            responseCode = response.status_code
        except:
            return 0
        return responseCode

    def summeVonSpalte(spaltenname):
        cursor = mydb.cursor()
        cursor.execute("select sum("+spaltenname+") from results;")
        return cursor.fetchall()[0][0]

    status = True
    while status:
        if status == True:
            werte = ["schere", "stein", "papier", "lizard", "spock"]
            vergleichswerte = {"schere": 4, "stein": 0, "papier": 2, "lizard": 3, "spock": 1}
            result = ["Unentschieden", "Gewonnen", "Gewonnen", "Verloren", "Verloren"]
            spielerwahl = eingabe(werte)
            bot = random.choice(werte)
            erg = compare(spielerwahl, bot, vergleichswerte, result)
            speichern(spielerwahl, erg)
            status = weiter()

    summeVonSpalte("schere")
    apiAufruf("SimmaDavid", summeVonSpalte("schere"), summeVonSpalte("stein"), summeVonSpalte("papier"), summeVonSpalte("lizard"),
              summeVonSpalte("spock"))

    mydb.close()