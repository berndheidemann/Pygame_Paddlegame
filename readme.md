# Lernsituation: **Ein Pong-Spiel erweitern**

---

## **Aufgabenstellung**

### 0. **Codeverständnis**
- Klonen Sie das Projekt und installieren ggf. Pygame (`python3 -m pip install -U pygame --user`). Starten Sie die `Main.py` und testen, ob das Programm funktioniert.
- Analysieren Sie den gegebenen Code und verstehen Sie, wie das Spiel funktioniert.
- Fügen Sie Kommentare hinzu, um den Code zu erklären.

### 1. **Zweites Paddle hinzufügen**
- Ergänzen Sie das Spiel um ein zweites Paddle für den rechten Spieler.
- **Problemstellung**: Finden Sie einen Weg, mit einer einzigen Klasse `Paddle` auszukommen, indem Sie die Keys für up und down als Parameter mitgeben.

---

### 2. **Gameover-Logik implementieren**
- Wenn der Ball den linken oder rechten Bildschirmrand erreicht:
    - Das Spiel endet.
    - Eine Nachricht zeigt an, welcher Spieler gewonnen hat.
- Optional: Das Spiel pausiert oder startet automatisch neu.

---

### 3. **Punktestand zählen und anzeigen**
- Erstellen Sie eine neue Klasse `Score`, die:
    - Punkte für **Spieler 1** und **Spieler 2** speichert.
    - Den Punktestand in der oberen Mitte des Bildschirms anzeigt.
    - Recherchieren Sie, wie Sie Text in Pygame anzeigen können.
- **Punktevergabe**:
    - Spieler 1 erhält einen Punkt, wenn der Ball den rechten Rand erreicht.
    - Spieler 2 erhält einen Punkt, wenn der Ball den linken Rand erreicht.

---

### 4. **Abprallwinkel anpassen**
Der Ball soll je nach Trefferposition auf dem Paddle in einem anderen Winkel zurückfliegen:

| Trefferposition auf dem Paddle    | Verhalten des Balls              |
|-----------------------------------|----------------------------------|
| **Obere Spitze**                  | Steiler Winkel nach oben         |
| **exakte Mitte des Paddles**      | Einfallswinkel = Ausfallswinkel  |
| **sonstiger Bereich des Paddles** | Winkel entsprechend modifizieren |
| **Untere Spitze**                 | Steiler Winkel nach unten        |

- **Hinweis**: Passen Sie die Werte für `yspeed` und `xspeed` dynamisch an. 

---

### 5. **Ballbeschleunigung**
- Bei jedem Kontakt mit einem Paddle wird der Ball schneller.

---

### 6. **Power Ups**

Alle Power-Ups sollen zufällig erscheinen, wenn der Ball das Paddle berührt (z.B. mit einer Wahrscheinlichkeit von 1:3). Power-Ups sollen an einer zufälligen Position erscheinen.
- Implementieren Sie ein Power-Up, das die Geschwindigkeit des Balls erhöht. 
- Implementieren Sie ein Power-Up, das die Geschwindigkeit des Balls verringert. 
- Implementieren Sie ein Power-Up, das die Paddle-Größe verändert.
---

