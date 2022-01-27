import random
if __name__ == "__main__":
    class VerketteteListe:
        def __init__(self):
            self.laenge = 0
            self.kopf = None

        def insert(self, neueDaten):
            if self.kopf:
                letzteDaten = self.kopf
                while letzteDaten != None:
                    if letzteDaten.naechster == None:
                        break
                    letzteDaten = letzteDaten.naechster

                letzteDaten.naechster = neueDaten
            else:
                self.kopf = neueDaten

        def delete(self, delete):
            if self.kopf != None:
                temp = self.kopf
                while temp.naechster != None:
                    if temp.naechster == delete:
                        if temp.naechster.naechster != None:
                            temp.naechster = temp.naechster.naechster
                        else:
                            temp.naechster = None
                    temp = temp.naechster

        def insertAtPoint(self, beforeD, newD):
            if self.kopf != None:
                temp = self.kopf
                while temp.naechster != None:
                    if temp == beforeD:
                        temp2 = temp.naechster
                        temp.naechster = newD
                        temp.naechster.naechster = temp2
                        break
                    temp = temp.naechster

        def returnAll(self):
            if self.kopf:
                print(self.kopf.wert)
                temp = self.kopf
                while temp.naechster != None:
                    temp = temp.naechster
                    print(temp.wert)

        def returnLength(self):
            self.laenge = 0
            if self.kopf != None:
                self.laenge += 1
                temp = self.kopf
                while temp.naechster != None:
                    self.laenge += 1
                    temp = temp.naechster
                print(self.laenge)


    class Daten:
        def __init__(self, wert = 0):
            self.wert = wert
            self.naechster = None


    d1 = Daten(random.randint(0, 10))
    d2 = Daten(random.randint(0, 10))
    d3 = Daten(random.randint(0, 10))

    v1 = VerketteteListe()
    v1.insert(d1)
    v1.insert(d2)
    v1.insert(d3)

    print("Ausgabe aller Daten:")
    print(v1.returnAll())
    print()

    v1.delete(d2)
    print("Ausgabe aller Daten neu:")
    print(v1.returnAll())
    print()

    v1.insertAtPoint(d1, Daten(random.randint(0,10)))
    print("Ausgabe aller Daten neuneu:")
    print(v1.returnAll())
    print()

    print("Ausgabe der Anzahl aller Daten:")
    v1.returnLength()