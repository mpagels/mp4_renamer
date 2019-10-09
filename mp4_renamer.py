import os
import shutil

def start():
    # Config
    # Liste die die Fragen enthält
    frage = [
        "[1] - Vorne was hinzufügen             - XXXXDateiName.mp4" ,
        "[2] - Hinten was angängen              - DateiNameXXXX.mp4",
        "[3] - Vorne und hinten was anhängen    - XXXFDateiNameXXX.mp4" 
        ]
    
    frage2 = "Eingabe 1 / 2 / 3 : "

    # Ausgabe, Nutzer wird die Fragen ausgegeben
    print("Wo soll der Dateiname erweitert werden? : ")
    print()
    for zeile in frage:
        print(zeile)
    
    print()

    # Nutzereingabe der Aufgabe des Programms anhand der Frage
    user_eingabe = int(input(frage2))

    # Gibt die Eingabe zurück
    return user_eingabe

def eingabe(zahl):
    # Config der Funktion eingabe()
    frage_vorne = "Was soll vorne angehängt werden? : "
    frage_hinten = "Was soll hinten angehängt werden? : "

    # Wenn der User 1 eingegeben hat dann:
    if zahl == 1:
        # User wird gefragt, was er vorne hinzugefügt haben möchte
        vorne = input(frage_vorne)
        # Programm geht das Verzeichnis durch, wo die Datei gestartet wurde
        for datei in os.listdir():
            # Kontrollinstanz, wenn der User eine Datei später hinzugefügt hat, und das Programm
            # eben nicht schon die umbenannten Dateien nochmal umbennent                      
            if not datei.startswith(vorne):
                # Check, dass er auch nur mp4 Dateien umbennt
                if datei.endswith(".mp4"):
                    # Umbennenung der Dateien
                    shutil.move(datei, vorne + datei)

    elif zahl == 2:
        hinten = input(frage_hinten)
        for datei in os.listdir():                      
            if not datei[:-4].endswith(hinten):
                if datei.endswith(".mp4"):
                    shutil.move(datei, datei[:-4] + hinten + datei[-4:])
    elif zahl == 3:
        vorne = input(frage_vorne)
        hinten = input(frage_hinten)
        for datei in os.listdir():                      
                if datei.endswith(".mp4"):
                    shutil.move(datei, vorne + datei[:-4] + hinten + datei[-4:])

user_eingabe = start()
eingabe(user_eingabe)