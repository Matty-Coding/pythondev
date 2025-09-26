
# Decoratore per gestire divisione per 0
def zero_division(f):
    def wrapper(x, y):
        try:
            x = float(x)
            y = float(y)

            return f(x, y)
        
        except ZeroDivisionError:
            return "⚠️  Non posso effettuare divisione per 0."
        
    return wrapper


# Decoratore per gestire basi delle radici
# Se esponente pari allora base > 0
def base_radice(f):
    def wrapper(x, y):
        x = float(x)
        y = float(y)

        if x < 0 and y % 2 == 0:
            return "⚠️  La base dev'essere positiva se l'indice della radice è pari."
        elif y == 0:
            return "⚠️  L'indice della radice deve essere diverso da 0."
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
        
        except ValueError:
            return "⚠️  Devi inserire un valore intero positivo."
    
    return wrapper


# Classe senza costruttore, non necessario  
# In questo caso la Classe raccoglie solamente le funzioni
# Mantengo codice ordinato e pulito 
class Calcola:
    # non necessario l'accesso ai dati della classe
    @staticmethod    
    def somma(x:int|float, y:int|float) -> int|float:
        return x + y
    
    @staticmethod
    def differenza(x:int|float, y:int|float) -> int|float:
        return (x - y) if x > y else (- (y - x))
    
    @staticmethod
    def prodotto(x:int|float, y:int|float) -> int|float:
        return x * y

    @staticmethod
    # Gestione errore tramite decoratore apposito
    # Dividendo necessariamente != 0
    @zero_division
    def quoziente(x:int|float, y:int|float) -> float:
        return x / y

    @staticmethod
    def potenza(x:int|float, y:int|float) -> int|float:
        return x ** y

    @staticmethod
    # Gestione errore tramite decoratore apposito
    # Base (x) necessariamente positiva se indice pari (y)
    @base_radice
    def radice(x:int|float, y:int) -> float:
        return x ** (1/y)

    @staticmethod
    # Gestione di errore tramite decoratore apposito
    # Parametro necessariamente di tipo int
    @intero
    def fattoriale(x: int) -> int:
        return x * Calcola.fattoriale(x - 1) if x != 0 else 1
    
    
# Mostra opzioni all'utente --> stringa dell'operazione scelta 
def interfaccia_utente():
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



def main():
    linea = "=" * 8
    print(f"\n{linea}  Calcolatrice by Tamati  {linea}\n")

    while True:
        
        operazione = interfaccia_utente().lower()

        if operazione == "esci":
            print("\nChiusura della calcolatrice.")
            break
        
        metodo = getattr(Calcola, operazione)

        if operazione == "fattoriale":
            print("\nCalcolo fattoriale...")

            valore_fattoriale = input("Inserisci un valore per il calcolo: ").strip()
            risultato_fattoriale = metodo(valore_fattoriale)

            print(f"\nIl fattoriale di {valore_fattoriale} corrisponde a --> {risultato_fattoriale}")

    
        elif operazione == "radice":
            print("\nCalcolo radice...")

            indice_radice = input("Inserisci l'indice della radice: ").strip()
            base_radice = input("Inserisci la base della radice: ").strip()

            risultato_radice = metodo(base_radice, indice_radice)
            print(f"Risultato --> {risultato_radice}")
            # gestisci round + errore per output adeguati in ogni caso


        elif operazione == "quoziente":
            print("\nCalcolo quoziente...")

            dividendo = input("Inserisci il dividendo: ").strip()
            divisore = input("Inserisci il divisore: ").strip()

            risultato_divisione = metodo(dividendo, divisore)
            print(f"Il quoziente della divisione corrisponde a --> {risultato_divisione}")
    

        elif operazione == "potenza":
            print("\nCalcolo potenza...")

            base_potenza = input("Inserisci la base: ").strip()
            esponente_potenza = input("Inserisci l'esponente: ").strip()

            risultato_potenza = metodo(float(base_potenza), float(esponente_potenza))
            print(f"Il risultato della potenza corrisponde a --> {risultato_potenza}")


        # Somma, Differenza, Prodotto
        print(f"\nCalcolo {operazione}...")

        a = input("Inserisci primo valore: ").strip()
        b = input("Inserisci secondo valore: ").strip()

        try:
            a = float(a)
            b = float(b)

            risultato_operazione = metodo(a, b)
            print(f"Risultato --> {risultato_operazione}")

        except ValueError:
            print("⚠️  Devi inserire un valore di tipo int o float.")

main()
