<h1>Verkettete Listen</h1>

<h3>Was macht das Programm?</h3>
Dieses Programm befasst sich mit der Funktinosweise und Abwicklung von doppelt verketteten Listen. Man findet eine Reihe an Methoden, welche für die doppelt verkettete Liste angepasst worden sind.

<h3>Wie führt man das Programm aus?</h3>
Das Programm wurde in der Entwicklungsumgebung IntelliJ entwickelt, lässt sich aber auch in jeder anderen Entwicklungsumgebung ausführen, welche ein Python Programm ausführen kann. Die verwendete Pythonversion lautet 3.10.

<h3>Ablauf des Programms</h3>
Nach dem Ausführen des Programms wird der Benutzer aufgefordert, die Anzahl der zu erstellenden Elemente anzugeben. Diese Eingabe muss eine Ganzzahl sein! Anschließend werden z.B. 100 zufällige Elemente erzeugt, welche jeweils von einer Spanne von 0 bis (der eingegebenen Zahl) variieren können. Diese Zahlen werden nun sowohl in eine doppelt-verkettete Liste als auch in eine Arrayliste eingefügt. Nun beginnt das Sortieren der Zahlen. Es wird sowohl die Dauer der Sortierung mittels Insertionsort Verfahren bei der doppelt-verketteten Liste, als auch der Arraylist in Sekunden gemessen. Die gemessenen Zeiten werden dann wiedergegeben.

<h3>Aufwandsklassen</h3>

| Methode | Aufwandklasse doppelt-verkettete Liste | Aufwandsklasse Arraylist |
| --- | --- | --- |
| insertAtEnd() | 1 | n + 1 |
| insertAtStart() | 1 | n + 1 |
| deleteAfter() | n | n |
| deleteBefore() | n | n |
| insertAfter() | n | n + 1 |
| insertBefore() | n | n + 1 |
| returnAllAsc() | n | n |
| returnAllDesc() | n | n |
| returnLength() | n | n |
| findByIndex() | n | n |
| findByObject | n | n |
| sortAsc() | n^8 | n^2 |
| sortDesc() | n^8 | n^2 |
