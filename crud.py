# file dati.txt gestito con operazioni CRUD
# scrivi nuovo contenuto nel file
# mostra a schermo il contenuto del file
# aggiungi nuove righe al file senza cancellare le precedenti
# svuota completamente il file
# menu contestuale

# crea nuovo file se non esistente, altrimenti aprilo
def crea():
    try:
        with open("dati.txt", "x") as f:
            print("File creato correttamente.")
    except FileExistsError:
        print("File già esistente.")

# scrive primo contenuto nel file   
def scrivi():
    with open("dati.txt", "w") as f:
        testo = input("Inserisci il testo da scrivere nel file --> ")
        f.write(testo)
        print("Primo contenuto aggiunto correttamente.")

# legge e mostra il contenuto del file
def leggi():
    with open("dati.txt", "r") as f:
        contenuto = f.read()
        print("Contenuto del file:")
        print(contenuto)

# aggiunge nuovo contenuto al file senza cancellare il precedente
def aggiorna():
    with open("dati.txt", "a") as f:
        testo = input("Inserisci il testo da aggiungere al file --> ")
        f.write("\n" + testo)
        print("Testo aggiunto correttamente al precedente.")

# svuota completamente il file
def cancella():
    with open("dati.txt", "w") as f:
        f.write("")
        print("File svuotato correttamente.")

def main():
    print("\nProgramma che gestisce file di testo con operazioni CRUD")
    print("\n   -----  MENU  -----\n")
    print("[1] - Apri file (Crea se non esistente)")
    print("[2] - Scrivi nuovo contenuto nel file")
    print("[3] - Leggi contenuto del file")
    print("[4] - Aggiorna del file")
    print("[5] - Svuota file")
    print("[6] - Esci\n")

    while True:
        scelta = input("Inserisci l'indice corrispondente alla tua scelta: ")

        if scelta == "1":
            crea()
        elif scelta == "2":
            scrivi()
        elif scelta == "3":
            leggi()
        elif scelta == "4":
            aggiorna()
        elif scelta == "5":
            cancella()
        elif scelta == "6":
            print("Uscita dal programma in corso...")
            break
        else:
            print("Scelta non valida, riprovare.")

main()