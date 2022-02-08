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
        if self.ende == beforeD:
            temp3 = self.ende
            self.ende = newD
            self.ende.vorher = temp3
            self.ende.vorher.naechster = self.ende
        else:
            if self.kopf != None:
                temp = self.kopf
                while temp.naechster != None:
                    if temp == beforeD:
                        temp2 = temp.naechster
                        temp.naechster = newD
                        temp.naechster.naechster = temp2
                        if temp.naechster.naechster != None:
                            temp.naechster.naechster.vorher = temp.naechster
                        else:
                            self.ende = temp.naechster
                        temp.naechster.vorher = temp
                        break
                    temp = temp.naechster

    def insertBefore(self, afterD, newD):
        if self.kopf == afterD:
            temp3 = self.kopf
            self.kopf = newD
            self.kopf.naechster = temp3
            self.kopf.naechster.vorher = self.kopf
        else:
            if self.ende != None:
                temp = self.ende
                while temp.vorher != None:
                    if temp == afterD:
                        temp2 = temp.vorher
                        temp.vorher = newD
                        temp.vorher.naechster = temp
                        temp.vorher.vorher = temp2
                        if temp.vorher.vorher != None:
                            temp.vorher.vorher.naechster = temp.vorher

                        break
                    temp = temp.vorher

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

    def findByObj(self, obj):
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

    def findByIndex(self, index):
        temp = self.kopf
        num = 0
        while temp.naechster != None:
            num += 1

            if num == index:
                return temp
            temp = temp.naechster
            if temp.naechster == None:
                return self.ende
        return "Dieses Objekt existiert nicht"

    def sortAsc(self):
        for i in range(2, self.returnLength()):
            temp = self.findByIndex(i)
            temp2 = temp.vorher
            while temp.wert < temp2.wert:
                if temp2.vorher != None:
                    temp2 = temp2.vorher
            self.insertAfter(temp2, temp)
            self.deleteAfter(temp2)




    def sortDesc(self):
        pass



class Daten:
    def __init__(self, wert = 0):
        self.vorher = None
        self.wert = wert
        self.naechster = None

if __name__ == "__main__":
    v1 = VerketteteListe()
    for i in range(0, 5):
        v1.insertAtEnd(Daten(random.randint(0,30)))

    print("Ausgabe aller Daten:")
    print(v1.returnAllAsc())
    print()

    print("Sortieren ASC: ")
    v1.sortAsc()
    print(v1.returnAllAsc())
    print()