
# Decoratore per gestire divisione per 0
def zero_division(f):
    def wrapper(x, y):
        try:
            x = float(x)
            y = float(y)

            return f(x, y)
        
        except ZeroDivisionError:
            return "⚠️  Il dividendo non deve essere nullo."
        
    return wrapper


# Decoratore per gestire basi delle radici
# Se esponente pari allora base > 0
def base_radice(f):
    def wrapper(x, y):
        x = float(x)
        y = int(y)

        if x < 0 and y % 2 == 0:
            return "⚠️  La base dev'essere positiva se l'indice della radice è pari."
        elif y <= 0:
            return "⚠️  L'indice dev'essere positivo."
        else:
            return f(x, y)
        
    return wrapper


# Decoratore per gestire validità input utente
# Valore SOLO di tipo intero positivo
def intero(f):
    def wrapper(x):
        try:
            x = int(x)
            if x < 0:
                return "⚠️  Devi inserire un valore intero positivo."
            
            return f(x)
        
        # Gestisce errore di conversione (stringa alfanumerica)
        except ValueError:
            return "⚠️  Devi inserire un valore intero positivo."
    
    return wrapper


# Classe senza costruttore, non necessario  
# In questo caso la Classe raccoglie solamente le funzioni
# Mantengo codice ordinato e pulito 
# Non necessario l'accesso ai dati della classe 
# viene quindi usato il decoratore @staticmethod
class Calcola:
    # Somma algebrica dei due valori inseriti
    @staticmethod    
    def somma(x:int|float, y:int|float) -> int|float:
        return x + y
    
    # Differenza in modulo dei due valori inseriti
    @staticmethod
    def differenza(x:int|float, y:int|float) -> int|float:
        return x - y 
    
    # Prodotto dei valori inseriti
    @staticmethod
    def prodotto(x:int|float, y:int|float) -> int|float:
        return x * y

    # Quoziente dei valori inseriti 
    # Gestione errore tramite decoratore apposito
    # Dividendo necessariamente != 0
    @staticmethod
    @zero_division
    def quoziente(x:int|float, y:int|float) -> float:
        return x / y

    # Base elevato alla potenza entrambi scelti dall'utente
    # tramite l'utilizzo di pow()
    @staticmethod
    def potenza(x:int|float, y:int|float) -> int|float:
        return pow(x, y)

    # Radice con indice variabie dall'utente (non solo quadrata)
    # Gestione errore tramite decoratore apposito
    # Base (x) necessariamente positiva se indice pari (y)
    @staticmethod
    @base_radice
    def radice(x:int|float, y:int) -> float:
        return x ** (1/y)

    # fattoriale del valore inserito
    # Gestione di errore tramite decoratore apposito
    # Parametro necessariamente di tipo int
    @staticmethod
    @intero
    def fattoriale(x: int) -> int:
        return x * Calcola.fattoriale(x - 1) if x != 0 else 1
    
    
# Mostra opzioni all'utente --> stringa dell'operazione scelta 
def interfaccia_utente():
    print("- " * 8)
    print("Seleziona l'operazione che vuoi effettuare:\n")
    
    # Creazione tupla riassuntiva --> leggibilità migliore
    # Scelta della tupla per mantenere ordine e staticità
    menu = (
        "Somma",
        "Differenza",
        "Prodotto",
        "Quoziente",
        "Potenza",
        "Radice",
        "Fattoriale"
    )
    
    while True:
        
        for index, value in enumerate(menu, start=1):
            print(f"[{index}] - {value}")

        print("\nDigita \"esci\" per uscire dalla calcolatrice.\n")

        scelta = input("\nDigita indice corrispondente alla tua scelta: ").strip()

        if scelta.lower() == "esci":
            return "esci"
        
        elif scelta in [str(i) for i in range(1, len(menu) + 1)]:
            return menu[int(scelta) - 1]

        elif scelta not in [str(i) for i in range(1, len(menu) + 1)]:
            print("⚠️  Indice non esistente, riprovare.\n")

# Gestisce i risultati separando la parte intera dalla decimale
# Restituisce valore intero se la parte decimale == 0
def formatta_risultato(risultato):
    intero, decimale = str(risultato).split(".")
    if int(decimale) == 0:
        return int(intero)
    return round(float(risultato), 3)


# Funzione di avvio e gestione del flusso
def main():
    linea = "=" * 8
    print(f"\n{linea}  Calcolatrice by Tamati  {linea}\n")

    while True:
        
        operazione = interfaccia_utente().lower()

        if operazione == "esci":
            print("\n✅ Calcolatrice chiusa corretttamente.\n")
            break
        
        # Accesso ai metodi della classe in modo dinamico
        metodo = getattr(Calcola, operazione)

        if operazione == "fattoriale":
            print("\nCalcolo fattoriale...")

            valore_fattoriale = input("Inserisci un valore per il calcolo: ").strip()
            risultato_fattoriale = metodo(valore_fattoriale)

            print(f"\nIl fattoriale di {valore_fattoriale} corrisponde a --> {risultato_fattoriale}")

            continue

        elif operazione == "radice":
            print("\nCalcolo radice...")

            indice_radice = input("Inserisci l'indice della radice: ").strip()
            base_radice = input("Inserisci la base della radice: ").strip()

            risultato_radice = metodo(base_radice, indice_radice)

            # Verifica type() del risultato per separare 
            # messaggio di errore dal risultato effettivo
            if type(risultato_radice) is not float:
                print(f"Risultato --> {risultato_radice}")
            else:
                # Se indice pari gestione risultato con + - 
                # Potenza pari rende positiva la base 
                # quindi la radice restituisce 2 valori congruenti opposti
                if int(indice_radice) % 2 == 0:
                    risultato_piu_meno = formatta_risultato(risultato_radice)
                    print(f"Risultati --> +{risultato_piu_meno}, -{risultato_piu_meno}") 
                
                # Caso in cui la radice ha indice dispari
                # Soluzione unica 
                else:
                    print(f"Risultato --> {formatta_risultato(risultato_radice)}")
            
            continue

        elif operazione == "quoziente":
            print("\nCalcolo quoziente...")

            dividendo = input("Inserisci il dividendo: ").strip()
            divisore = input("Inserisci il divisore: ").strip()

            risultato_divisione = metodo(dividendo, divisore)
            
            if type(risultato_divisione) is not float:
                print(f"Risultato --> {risultato_divisione}")
            else:
                print(f"Risultato --> {formatta_risultato(risultato_divisione)}")

            continue

        elif operazione == "potenza":
            print("\nCalcolo potenza...")

            base_potenza = input("Inserisci la base: ").strip()
            esponente_potenza = input("Inserisci l'esponente: ").strip()

            risultato_potenza = metodo(float(base_potenza), float(esponente_potenza))
            print(f"Il risultato della potenza corrisponde a --> {formatta_risultato(risultato_potenza)}")

            continue

        # Somma, Differenza, Prodotto
        print(f"\nCalcolo {operazione}...")

        a = input("Inserisci primo valore: ").strip()
        b = input("Inserisci secondo valore: ").strip()

        try:
            a = float(a)
            b = float(b)

            risultato_operazione = metodo(a, b)
            print(f"Risultato --> {formatta_risultato(risultato_operazione)}")

        except ValueError:
            print("⚠️  Devi inserire un valore di tipo int o float.")

main()
