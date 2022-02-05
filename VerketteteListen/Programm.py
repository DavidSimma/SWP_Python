import random

class VerketteteListe:
    def __init__(self):
        self.laenge = 0
        self.kopf = None
        self.ende = None


    def insertAtEnd(self, neueDaten):
        if self.ende:
            vorletzteDaten = self.ende
            vorletzteDaten.naechster = neueDaten
            vorletzteDaten.naechster.vorher = vorletzteDaten
            self.ende = vorletzteDaten.naechster
        else:
            self.ende = neueDaten
            self.kopf = neueDaten

    def insertAtStart(self, neueDaten):
        if self.kopf:
            zweiter = self.kopf
            zweiter.vorher = neueDaten
            zweiter.vorher.naechster = zweiter
            self.kopf = zweiter.vorher
        else:
            self.ende = neueDaten
            self.kopf = neueDaten

    def deleteAfter(self, delete):
        if self.kopf != None:
            temp = self.kopf
            while temp.naechster != None:
                if temp == delete:
                    if temp.naechster.naechster != None:
                        temp.naechster = temp.naechster.naechster
                        temp.naechster.vorher = temp
                    else:
                        temp.naechster = None
                    return
                temp = temp.naechster

    def deleteBefore(self, delete):
        if self.ende != None:
            temp = self.ende
            while temp.vorher != None:
                if temp == delete:
                    if temp.vorher.vorher != None:
                        temp.vorher = temp.vorher.vorher
                        temp.vorher.naechster = temp
                    else:
                        temp.vorher = None
                    return
                temp = temp.vorher

    def insertAfter(self, beforeD, newD):
        if self.kopf != None:
            temp = self.kopf
            while temp.naechster != None:
                if temp == beforeD:
                    temp2 = temp.naechster
                    temp.naechster = newD
                    temp.naechster.naechster = temp2
                    break
                temp = temp.naechster

    def insertBefore(self, afterD, newD):
        if self.kopf != None:
            temp = self.kopf
            while temp.naechster != None:
                if temp == beforeD:
                    temp2 = temp.naechster
                    temp.naechster = newD
                    temp.naechster.naechster = temp2
                    break
                temp = temp.naechster

    def returnAllAsc(self):
        if self.kopf:
            print(self.kopf.wert)
            temp = self.kopf
            while temp.naechster != None:
                temp = temp.naechster
                print(temp.wert)


    def returnAllDesc(self):
        if self.ende:
            print(self.ende.wert)
            temp = self.ende
            while temp.vorher != None:
                temp = temp.vorher
                print(temp.wert)



    def returnLength(self):
        self.laenge = 0
        if self.kopf != None:
            self.laenge += 1
            temp = self.kopf
            while temp.naechster != None:
                self.laenge += 1
                temp = temp.naechster
        return self.laenge

    def find(self, obj):
        temp = self.kopf
        num = 0
        while temp.naechster != None:
            num += 1

            if temp == obj:
                return "Objekt befindet sich an der Stelle: " + str(num)
            temp = temp.naechster
            if temp.naechster == None:
                return "Objekt befindet sich an der Stelle: " + str(num+1)
        return "Dieses Objekt existiert nicht"


class Daten:
    def __init__(self, wert = 0):
        self.vorher = None
        self.wert = wert
        self.naechster = None

if __name__ == "__main__":

    d1 = Daten(random.randint(0, 30))
    d2 = Daten(random.randint(0, 30))
    d3 = Daten(random.randint(0, 30))
    d4 = Daten(random.randint(0, 30))

    v1 = VerketteteListe()
    print(v1.returnAllAsc())
    v1.insertAtEnd(d1)
    v1.insertAtEnd(d2)
    v1.insertAtEnd(d3)

    print("Ausgabe aller Daten 1:")
    print(v1.returnAllDesc())
    print()

    print("Objekt finden: ")
    print(v1.find(d3))
    print()

    v1.insertAtStart(d4)
    print("Ausgabe aller Daten 1.1")
    print(v1.returnAllAsc())
    print()

    v1.deleteAfter(d2)
    print("Ausgabe aller Daten 1.2:")
    print(v1.returnAllAsc())
    print()

    v1.insertAfter(d1, Daten(random.randint(0,10)))
    print("Ausgabe aller Daten 1.3:")
    print(v1.returnAllAsc())
    print()

    print("Ausgabe der Anzahl aller Daten:")
    print(v1.returnLength())