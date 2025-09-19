# SISTEMA DI GESTIONE STUDENTI E VOTI
from random import randrange

studenti = [
    ["Mario Rossi", [6, 7, 8, 6], [7, 8, 7, 9], [5, 6, 7, 6]],
    ["Laura Bianchi", [9, 8, 9, 10], [8, 7, 8, 8], [9, 9, 8, 10]],
    ["Giuseppe Verdi", [5, 6, 5, 7], [6, 6, 7, 6], [7, 8, 7, 8]],
    ["Anna Neri", [8, 7, 9, 8], [9, 9, 8, 9], [7, 8, 8, 7]],
    ["Marco Gialli", [4, 5, 6, 5], [6, 5, 6, 7], [5, 5, 6, 6]]
]

classe_2 = [
    ["Luca Verdi", [2, 3, 4, 5], [6, 6, 7, 9], [5, 4, 5, 8]],
    ["Giordano Aranci", [4, 6, 6, 7], [3, 5, 7, 6], [7, 8, 4, 6]]
]

materie = ["Matematica", "Italiano", "Inglese"]


# ==============================================================================
# 1 Aggiungi un nuovo studente
# Crea una funzione che aggiunge un nuovo studente alla lista
# ==============================================================================

# ritorna dati alunno
def dati_studente():
    nome, cognome = prendi_nomi()
    alunno = nome + cognome
    mat, ita, ing = genera_voti()
    
    return alunno, mat, ita, ing

# ritorna lista studenti aggiornata
def aggiungi_studente(nome, mat, ita, ing):
    studente = [nome, mat, ita, ing]
    studenti.append(studente)

    return studenti

# ritorna nome e cognome con iniziali maiuscole
def prendi_nomi():
    alunno = input("Inserisci nome e cognome dello studente separati da una virgola: ").strip()
    nome, cognome = alunno.split(",")

    return nome.title(), cognome.title()

# ritorna le liste con 4 voti di ogni materia nell'ordine mat - ita - ing
def genera_voti():
    while True:
        numero_voti = input("Quanti voti vuoi che abbia ogni materia? ")
        try:
            n = int(numero_voti)
            mat = [randrange(2, 10) for x in range(n)]
            ita = [randrange(2, 10) for x in range(n)]
            ing = [randrange(2, 10) for x in range(n)]

            return mat, ita, ing
        
        except ValueError:
            print("La quantità dei voti scelta dev'essere necessariamente un intero, riprovare.")


# ==============================================================================
# 2 Calcola la media dei voti
# Crea una funzione che calcola la media di tutti i voti di uno studente
# ==============================================================================

# restituisce lista [nome cognome, media voti]
def calcola_media(alunno):
    for i in studenti:
        if alunno == i[0]:
            somma_voti = sum(i[1]) + sum(i[2]) + sum(i[3])
            media = somma_voti / (len(i[1]) + len(i[2]) + len(i[3]))
    
            return [alunno, round(media, 2)]


# ==============================================================================
# 3 Trova gli studenti con insufficienze
# Usa cicli for e if per trovare studenti con almeno un voto sotto il 6
# ==============================================================================

# restituisce lista [nome cognome, conta insuff mate, conta insuff ita, conta insuff ing]
def trova_insufficienze():
    lista_alunni_insufficienti = []
    for i in studenti:
        conta_mate = 0
        for k in i[1]:
            if k < 6: 
                conta_mate += 1

        conta_ita = 0
        for m in i[2]:
            if m < 6:
                conta_ita += 1

        conta_ing = 0
        for j in i[3]:
            if j < 6:
                conta_ing += 1

        if conta_mate != 0 or conta_ita != 0 or conta_ing != 0:
            alunno_insufficiente = [i[0], conta_mate, conta_ita, conta_ing]
            lista_alunni_insufficienti.append(alunno_insufficiente)
        
    return lista_alunni_insufficienti

# ==============================================================================
# 4 Migliora i voti
# Aumenta di 1 punto tutti i voti insufficienti (< 6), max 10
# Usa enumerate() e modifica le liste in-place
# ==============================================================================

# restituisce la lista studenti aggiornata
def migliora_voti():
    for studente in studenti:
        conta = 0
        for i, materia in enumerate(studente[1:]):
            for j, voto in enumerate(materia):
                if materia[j] < 6 and conta < 10:
                    materia[j] += 1
                    conta += 1

    return studenti


# ==============================================================================
# 5 Classifica studenti
# Crea una classifica ordinata per media voti
# ==============================================================================

# esegue la media di ogni studente e ordina gli elementi nella lista in ordine decrescente
# ritorna una lista del tipo [media, nome cognome]
def classifica():
    lista_ordinata = []
    for i in studenti:
        somma_voti = sum(i[1]) + sum(i[2]) + sum(i[3])
        media = somma_voti / (len(i[1]) + len(i[2]) + len(i[3]))

        alunno = [round(media, 2), i[0]]
        lista_ordinata.append(alunno)

    lista_ordinata.sort(reverse=True)
    lista_ordinata_nuova = []
    for i in lista_ordinata:
        lista_ordinata_nuova.append([i[1], i[0]])
    
    return lista_ordinata_nuova




# ==============================================================================
# 6 Rimuovi studente
# Rimuovi uno studente dalla lista usando remove() o pop()
# ==============================================================================

# ritorna la lista aggiornata oppure None
def rimuovi_studente(alunno):
    for i in studenti:
        if i[0] == alunno:
            indice = studenti.index(i)
            studenti.pop(indice)
            
            return studenti
        
        else:
            return None


# ==============================================================================
# 7 Statistiche complete
# Calcola varie statistiche usando count(), index(), max(), min()
# ==============================================================================

# eccellenze = media >= 8 ritorna dizionario con le statistiche, parametro = funzione classifica()
def statistiche_complete(valori):
    totale_studenti = len(studenti)
    somma = 0
    lista_eccellenze = []
    lista_insufficienze = []
    for i in valori:
        somma += i[1]
        if i[1] >= 8:
            lista_eccellenze.append(i)
        elif i[1] < 6:
            lista_insufficienze.append(i)

    media_classe = round(somma / totale_studenti, 2)
    
    statistiche = {
        "Media classe" : media_classe,
        "Media Maggiore" : [valori[0][0], valori[0][1]],
        "Media Minore" : [valori[-1][0], valori[-1][1]],
        "Eccellenze" : lista_eccellenze,
        "Insufficienze" : lista_insufficienze
    }

    # print("------------------------")
    # for k, v in statistiche.items():
    #     print(k, "-->", v)

    return statistiche


# ==============================================================================
# 8 Inserisci voto in posizione specifica
# Usa insert() per aggiungere un voto in una posizione specifica
# ==============================================================================

# restituisce lista aggiornata del singolo studente
def inserisci_voto(alunno, materia, indice, voto):
    # [nome cognome, [mate], [ita], [ing]]
    for i in studenti:
        if i[0] == alunno:
            materia = i[1:][int(materia)]
            materia.insert(indice, voto)
            alunno_aggiornato = i

    if not alunno_aggiornato:
        return "Studente non trovato"

    else:
        return alunno_aggiornato


# ==============================================================================
# 9 Unisci classi
# Usa extend() per unire due liste di studenti
# ==============================================================================

# restituisce il numero degli studenti pre-modifica, il numero della seconda classe
# la nuova classe e il numero aggiornato degli studenti

def unisci_classi():
    all_studenti_prima = len(studenti)
    alunni_classe_2 = len(classe_2)

    studenti.extend(classe_2)

    all_studenti_dopo = len(studenti)
    
    return all_studenti_prima, alunni_classe_2, studenti, all_studenti_dopo

# ==============================================================================
# 10 Resetta voti materia
# Usa clear() per azzerare i voti di una specifica materia
# ==============================================================================

# restituisce la lista studenti aggiornata
def resetta_voti(materia):
    for i in studenti:
        i[materia].clear()

    return studenti



def main():
    for i in studenti:
        print(i)
    print("\n--- GESTIONALE SCOLASTICO ---")
    while True:
        print("Scegli un'opzione da eseguire...\n")
        print("[1] - Aggiungere studente")
        print("[2] - Calcolare la media generale di uno studente")
        print("[3] - Verifica insufficienze studenti")
        print("[4] - Aumenta di 1 voto le insufficienze fino ad un massimo di 10 per ciascun studente")
        print("[5] - Classifica studenti per media generali dei voti")
        print("[6] - Rimuovere studente")
        print("[7] - Mostra statistiche")
        print("[8] - Inserisci un voto in una materia specifica")
        print("[9] - Unisci le due classi")
        print("[10] - Resetta tutti i voti di una singola materia per tutti gli studenti")
        print("[11] - Esci")

        user = input("\nInserisci un numero corrispondente all'azione che vuoi eseguire: ")

        try:
            user = int(user)

            if user == 1:
                print("Aggiunta dati alunno...")
                alunno, mat, ita, ing = dati_studente()

                print(f"Aggiunta dello studente {alunno} in corso...")
                lista_studenti_aggiornata = aggiungi_studente(alunno, mat, ita, ing)

                for i in lista_studenti_aggiornata:
                    print(i)
                    
                print("✅ Aggiunto correttamente alla lista.")
                print("\n---------------------------------------\n")


            elif user == 2:
                print("Media studente...")
                nome = input("Inserisci SOLO il nome dello studente: ").strip()
                cognome = input("Inserisci SOLO il cognome dello studente: ").strip()

                alunno_media = nome.title() + " " + cognome.title()
                print(f"Calcolo della media generale dello studente {alunno_media}...")

                alunno_con_media = calcola_media(alunno_media)
                print(f"Lo studente {alunno_con_media[0]} ha una media generale di {alunno_con_media[1]}.")
                print("\n---------------------------------------\n")


            elif user == 3:
                print("Verifica insufficienze studenti...")
                lista_alunni = trova_insufficienze()

                if lista_alunni:
                    for i in lista_alunni:
                        print(f"Lo studente {i[0]} presenta:")
                        print(f"{i[1]} insufficienze in matematica")
                        print(f"{i[2]} insufficienze in italiano")
                        print(f"{i[3]} insufficienze in inglese")

                else:
                    print("Nessuno studente presenta delle insufficienze.")

            elif user == 4:
                print("Aumentando di 1 voto tutti, massimo 10 ciascuno...")
                migliora_voti()
                print("La nuova lista studenti aggiornata:")
                for i in studenti:
                    print(i)

            elif user == 5:
                print("Calcolando la classifica...")
                lista_ordinata = classifica()

                for index, value in enumerate(lista_ordinata, start=1):
                    print(f"{index}. {value[1]} --> {value[0]}")

            elif user == 6:
                nome = input("Inserisci SOLO il nome dello studente: ").strip()
                cognome = input("Inserisci SOLO il cognome dello studente: ").strip()

                alunno_rimuovi = nome.title() + " " + cognome.title()
                print("Rimuovendo uno studente...")
                print("✅", alunno_rimuovi)
                rimosso = rimuovi_studente(alunno_rimuovi)
                if rimosso != None:
                    print(f"Lo studente {alunno_rimuovi} è stato rimosso correttamente dalla lista")
                    print(f"La lista aggiornata...")
                    for i in studenti:
                        print(i)
                
                else:
                    print("Lo studente non è stato trovato, pertanto la lista rimane invariata")
                    for i in studenti:
                        print(i)

            elif user == 7:
                print("Mostra statistiche in corso...")
                dizionario_statistiche = statistiche_complete(classifica())
                for k, v in dizionario_statistiche.items():
                    print(k, ":", v)

            elif user == 8:
                print("Aggiunta voto alunno...")
                nome = input("Inserisci SOLO il nome dello studente: ").strip()
                cognome = input("Inserisci SOLO il cognome dello studente: ").strip()
                materia = input(
                    "Scegli la materia a cui aggiungere il voto\n[1] Matematica [2] Italiano [3] Inglese\n--> "
                )

                alunno_voto = nome.title() + " " + cognome.title()
                # alunno_scelto = []
                for i in studenti:
                    if i[0] == alunno_voto:
                        alunno_scelto = i[int(materia)]
                        print(alunno_scelto)

                print(f"Materia: {materie[int(materia) - 1]}\nVoti: {alunno_scelto}")

                indice = input(
                    f"Inserisci l'indice corrisponde a dove vuoi inserire il voto\nposizioni (da 1 a {len(alunno_scelto) + 1}) --> "
                    )
                
                voto_da_inserire = input("Inserisci il voto da inserire (da 2 a 10 disponibili) --> ")

                # print(f"\n\nNome --> {alunno_voto}\nIndice materia --> {int(materia) - 1}\nPosizione --> {int(indice) - 1}\nVoto --> {voto_da_inserire}\n\n") # debug


                alunno_aggiornato = inserisci_voto(alunno_voto, int(materia) - 1, int(indice) - 1, int(voto_da_inserire))
                print(alunno_aggiornato)

            elif user == 9:
                print("Sto unendo le due classi...")
                totale_classe_1_prima, totale_classe_2, studenti_aggiornati, totale_classe_1_dopo = unisci_classi()

                print(f"Conteggio alunni prima classe --> {totale_classe_1_prima}")
                print(f"Conteggio alunni seconda classe --> {totale_classe_2}")
                print(f"Conteggio alunni prima classe (dopo unione con seconda) --> {totale_classe_1_dopo}")

                print("Stampa della nuova classe in corso...")
                for i in studenti_aggiornati:
                    print(i)

            elif user == 10:
                print("Rimozione voti materia specifica...")
                pulisci_materia = input("Scegli la materia che vuoi resettare da tutti i voti per tutti gli alunni --> [1] Matematica [2] Italiano [3] Inglese\n--> ")
                    
                pulisci_materia = int(pulisci_materia)
                print("Lista attuale")
                for i in studenti:
                    print(i)

                print("Sto resettando i voti...")
                lista_resettata = resetta_voti(pulisci_materia)
                print("Lista aggiornata")
                for i in lista_resettata:
                    print(i)
            
            elif user == 11:
                print("Uscita dal programma in corso...")
                break

            else:
                print("⚠️  Il valore inserito non è presente nell'elenco, riprovare.")

        except ValueError:
            print("⚠️  Input non valido, puoi inserire solo un numero intero.")


main()

