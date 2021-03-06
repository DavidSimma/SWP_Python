import random
import time


class ArrayListe:

    def __init__(self):
        self.liste = []

    #--------------------------Einfügen-------------------------------

    def insertAtEnd(self, neueDaten):
        self.liste.append(neueDaten)
    def insertAtStart(self, neueDaten):
        self.liste.insert(0, neueDaten)

    #--------------------------Löschen-------------------------------

    def deleteByIndex(self, index):
        self.liste.pop(index)
    def deleteAfterIndex(self, index):
        if len(self.liste) > index+1:
            self.liste.pop(index+1)
    def deleteBeforeIndex(self, index):
        if index-1 >= 0:
            self.liste.pop(index-1)

    #--------------------------Einfügen an Punkt-------------------------------

    def insertAtPoint(self, index, newD):
        self.liste.insert(index, newD)
    def insertAfter(self, index, newD):
        self.liste.insert(index+1, newD)
    def insertBefore(self, index, newD):
        if index-1 >= 0:
            self.liste.insert(index-1, newD)

    #--------------------------Wiedergabe-------------------------------

    def returnAllAsc(self):
        for i in self.liste:
            print(i)
    def returnAllDesc(self):
        for i in reversed(self.liste):
            print(i)

    #--------------------------Length-------------------------------

    def returnLength(self):
        return len(self.liste)

    #--------------------------Find-------------------------------

    def findByObj(self, obj):
        indexes = []
        for i in range(0, len(self.liste)):
            if self.liste[i] == obj:
                indexes.append(i)
        return indexes
    def findByIndex(self, index):
        return self.liste[index]

    #--------------------------Insertionsort-------------------------------
    def sortAsc(self):
        for i in range(1, len(self.liste)):

            key = self.liste[i]
            j = i-1
            while j >= 0 and key < self.liste[j] :
                self.liste[j + 1] = self.liste[j]
                j -= 1
            self.liste[j + 1] = key

    def sortDesc(self):
        for i in range(1, len(self.liste)):

            key = self.liste[i]
            j = i-1
            while j >= 0 and key > self.liste[j] :
                self.liste[j + 1] = self.liste[j]
                j -= 1
            self.liste[j + 1] = key

class VerketteteListe:
    def __init__(self):
        self.laenge = 0
        self.kopf = None
        self.ende = None

    #--------------------------Einfügen-------------------------------

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

    #--------------------------Löschen-------------------------------

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

    #--------------------------Einfügen an Punkt-------------------------------

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

    #--------------------------Wiedergabe-------------------------------

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

    #--------------------------Length-------------------------------

    def returnLength(self):
        self.laenge = 0
        if self.kopf != None:
            self.laenge += 1
            temp = self.kopf
            while temp.naechster != None:
                self.laenge += 1
                temp = temp.naechster
        return self.laenge

    #--------------------------Find-------------------------------

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

    #--------------------------Insertionsort-------------------------------

    def sortAsc(self):
        if self.kopf == None:
            return
        else:
            temp = self.kopf
            while temp.naechster != None:
                index = temp.naechster
                while index != None:
                    if temp.wert > index.wert:
                        temp2 = temp.wert
                        temp.wert = index.wert
                        index.wert = temp2
                    index = index.naechster
                temp = temp.naechster

    def sortDesc(self):
        if self.kopf == None:
            return
        else:
            temp = self.kopf
            while temp.naechster != None:
                index = temp.naechster
                while index != None:
                    if temp.wert < index.wert:
                        temp2 = temp.wert
                        temp.wert = index.wert
                        index.wert = temp2
                    index = index.naechster
                temp = temp.naechster

class Daten:
    def __init__(self, wert = 0):
        self.vorher = None
        self.wert = wert
        self.naechster = None


if __name__ == "__main__":

    a1 = ArrayListe()
    v1 = VerketteteListe()

    anzahl = int(input("Wie viele Elemente sollen erzeugt werden: "))
    if anzahl > 0:
        print("Elemente erzeugen")
        for i in range(0, anzahl):
            temp = random.randint(0, anzahl)
            v1.insertAtEnd(Daten(temp))
            a1.insertAtEnd(temp)
        print("Elemente erzeugt")

        a1.deleteByIndex(4)

        print("Beginne Sortieren")
        startzeitV = time.time()
        v1.sortAsc()
        endzeitV = time.time()
        print("Das Sortieren der verketteten Liste hat ", endzeitV-startzeitV, " Sekunden gebraucht")

        startzeitA = time.time()
        a1.sortAsc()
        endzeitA = time.time()
        print("Das Sortieren der Array Liste hat ", endzeitA-startzeitA, " Sekunden gebraucht")
