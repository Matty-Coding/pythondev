# funzione per prendere dall'utente la grandezza della lista
def inserisci_grandezza_lista():
    while True:
        grandezza_lista = input("\nInserisci un valore per definire la grandezza della lista: ").strip()

        try:
            grandezza_lista = int(grandezza_lista)
            return grandezza_lista
        
        except ValueError:
            print(f"Il valore inserito dev'essere un intero, non sono ammessi ne float ne str, riprovare.")


# funzione che inserisci i valori nella lista
def inserisci_valori(n):
    lista_valori = []

    while True:
        utente = input(f"Inserisci elemento {len(lista_valori) + 1} nella lista: ").strip()

        try:
            utente = float(utente)
            lista_valori.append(utente)

            # print(len(lista_valori), n)

            if len(lista_valori) == n:
                break

        except ValueError:
            print("Devi inserire un valore numerico di tipo int o float, str non ammessi, riprovare.")

    return lista_valori


# funzione che prende in input la precedente, moltiplica i valori
# dividi il prodotto per 2 --> prodotto lista / 2
# valore <= 100 --> eccezione 
            
def moltiplica_valori_dividi_per_due(lista):
    try:
        # calcola prodotto
        prodotto = 1
        for i in lista:
            prodotto *= i

        # calcola la metà del prodotto
        half_prodotto = round(prodotto / 2, 3)

        if half_prodotto <= 100:
            raise ZeroDivisionError ("La metà del prodotto degli elementi presenti in lista è minore o uguale a 100!")
    
    except ZeroDivisionError:
        print("La divisione non è andata a buon fine.")

    return half_prodotto
    

def main():
    grandezza_lista = gl = inserisci_grandezza_lista()
    print(f"La lista sarà di {gl} elementi.")

    lista = inserisci_valori(n=gl)
    print(f"La lista è stata riempita correttamente.\n--> {lista}")

    half_prodotto = moltiplica_valori_dividi_per_due(lista)
    print(f"La metà del prodotto degli elementi presenti nella lista corrisponde a --> {half_prodotto}")

main()