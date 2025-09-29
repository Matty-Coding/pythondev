# Esercizi Misti Python
## Imparare a Combinare le Risorse


#  Analizzatore di Parole
### Combina: Stringhe, Liste, Dizionari, Comprehension
"""
Dato un testo, crea un analizzatore che:

1. Conta le parole totali
2. Trova le 5 parole più lunghe
3. Conta le vocali totali
4. Crea un dizionario con lunghezza parole -> lista parole
5. Trova parole palindrome (se esistono)

Usa list/dict comprehension dove possibile
"""

testo = """Python è un linguaggio fantastico per imparare 
         la programmazione. È versatile e potente."""




# -----------------------------------------------------------------

# Carrello della Spesa
### Combina: Dizionari, Liste, For, If, Operazioni matematiche
"""
Simula un carrello della spesa online.

Catalogo prodotti con prezzi
Carrello utente con quantità
Applica sconti condizionali:
- 10% se totale > 50€
- 15% se totale > 100€
- Spedizione gratis sopra 30€ (altrimenti 5€)

Calcola il totale finale
"""

catalogo = {
    "pasta": 1.20,
    "pomodoro": 2.50,
    "mozzarella": 4.80,
    "basilico": 1.00,
    "olio": 8.50,
    "pane": 1.50,
    "acqua": 0.50
}

carrello = [
    {"prodotto": "pasta", "quantità": 2},
    {"prodotto": "pomodoro", "quantità": 1},
    {"prodotto": "mozzarella", "quantità": 2},
    {"prodotto": "acqua", "quantità": 6}
]

# Calcola il totale con sconti e spedizione...

# -----------------------------------------------------------------


# Validatore Password
### Combina: Stringhe, If, For, Any/All, Return multipli

"""
Crea un validatore di password che controlla:
- Lunghezza minima 8 caratteri
- Almeno una maiuscola
- Almeno una minuscola
- Almeno un numero
- Almeno un carattere speciale (!@#$%^&*)

Ritorna:
- (True, "Password valida") se ok
- (False, [lista_errori]) se non valida

Bonus: calcola un punteggio di forza (debole/media/forte)
"""

def valida_password(password):
    # Il tuo codice qui...
    pass

# Test
passwords = ["abc123", "Password1!", "TUTTO_MAIUSCOLO", "Sicura123!"]

# -----------------------------------------------------------------


# Agenda Appuntamenti
### Combina: Dizionari annidati, Date/orari (stringhe), Sorting

"""
Gestisci un'agenda di appuntamenti.

Ogni appuntamento ha:
- data (stringa "YYYY-MM-DD")
- ora (stringa "HH:MM")
- descrizione
- durata (minuti)

Implementa:
1. Aggiungi appuntamento (controlla conflitti)
2. Cancella appuntamento
3. Mostra appuntamenti del giorno
4. Trova prossimo slot libero di almeno X minuti
"""

agenda = {
    "2024-01-15": [
        {"ora": "09:00", "desc": "Riunione", "durata": 60},
        {"ora": "14:30", "desc": "Call cliente", "durata": 30}
    ]
}

# Implementa le funzioni...


# -----------------------------------------------------------------

# Convertitore Unità
### Combina: Dizionari, Funzioni, Input/Output formattato
"""
Crea un convertitore universale di unità.

Supporta:
- Lunghezza (metri, piedi, pollici)
- Peso (kg, libbre, once)
- Temperatura (Celsius, Fahrenheit, Kelvin)

Struttura suggerita: dizionario di dizionari con fattori di conversione
Gestisci input non validi
"""

conversioni = {
    "lunghezza": {
        "metri_piedi": 3.28084,
        "piedi_metri": 0.3048,
        # aggiungi altre...
    },
    "temperatura": {
        # Le temperature hanno formule, non solo fattori!
    }
}

def converti(valore, da_unita, a_unita):
    # Il tuo codice qui...
    pass


# -----------------------------------------------------------------

# Gioco Carte
### Combina: Liste, Random, Classi (opzionale), Logica gioco
"""
Implementa un semplice gioco di carte (es: Blackjack semplificato)

1. Crea un mazzo di carte (usa liste/tuple)
2. Mischia il mazzo
3. Distribuisci carte a giocatori
4. Calcola punteggi
5. Determina vincitore
6. Gestisci casi speciali (es: Asso vale 1 o 11)
"""

import random

# Suggerimento struttura
semi = ['♠', '♥', '♦', '♣']
valori = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

# Crea mazzo, mischia, distribuisci...


# -----------------------------------------------------------------

#  Tracker Abitudini
### Combina: Date, Dizionari, Statistiche, Visualizzazione testuale

"""
Traccia abitudini giornaliere per un mese.

Per ogni giorno, segna se hai completato l'abitudine (True/False)
Calcola:
- Streak corrente (giorni consecutivi)
- Streak più lungo
- Percentuale completamento
- Pattern settimanale (quale giorno più successo)

Visualizza calendario testuale
"""

# Esempio: 30 giorni di dati
import random
abitudini = {
    "esercizio": {f"2024-01-{i:02d}": random.choice([True, False]) 
                  for i in range(1, 31)},
    "lettura": {f"2024-01-{i:02d}": random.choice([True, False]) 
                for i in range(1, 31)}
}

# Analizza e visualizza...

# -----------------------------------------------------------------

#  Text Adventure 
### Combina: Dizionari, Input utente, Logica di gioco, State management



"""
Crea una mini avventura testuale.

Il giocatore naviga tra stanze, raccoglie oggetti, risolve puzzle.
Struttura:
- Stanze collegate tra loro
- Oggetti da raccogliere
- Inventario giocatore
- Condizioni vittoria

Comandi: vai [direzione], prendi [oggetto], usa [oggetto], guarda
"""

gioco = {
    "stanze": {
        "ingresso": {
            "descrizione": "Sei nell'ingresso. C'è una porta a nord.",
            "direzioni": {"nord": "corridoio"},
            "oggetti": ["chiave"]
        },
        "corridoio": {
            "descrizione": "Un lungo corridoio. Porte a est e ovest.",
            "direzioni": {"sud": "ingresso", "est": "cucina", "ovest": "studio"},
            "oggetti": []
        }
        # aggiungi altre stanze...
    },
    "inventario": [],
    "posizione": "ingresso"
}

# Game loop...


# -----------------------------------------------------------------

# Generatore Report
### Combina: Formattazione stringhe, Tabelle testuali, Aggregazioni

"""
Genera un report vendite formattato.

Input: lista transazioni con data, prodotto, quantità, prezzo
Output: report testuale con:
- Tabella vendite per prodotto
- Totali per giorno
- Prodotto più venduto
- Giorno con più incasso
- Formattazione aligned e bordi ASCII
"""

vendite = [
    {"data": "2024-01-15", "prodotto": "Laptop", "qta": 2, "prezzo": 800},
    {"data": "2024-01-15", "prodotto": "Mouse", "qta": 5, "prezzo": 20},
    {"data": "2024-01-16", "prodotto": "Laptop", "qta": 1, "prezzo": 800},
    {"data": "2024-01-16", "prodotto": "Tastiera", "qta": 3, "prezzo": 50}
]

# Genera report formattato...
# ++-+-+--+
# | Prodotto   | Quantità | Prezzo| Totale |
# ++-+-+--+
# | Laptop     |     3    |  800  |  2400  |
# etc...


# -----------------------------------------------------------------

# Sistema Votazioni
### Combina: Counter, Validazione, Risultati ranked



"""
Sistema di votazione con diverse modalità:

1. Voto singolo: ogni utente vota un'opzione
2. Voto ranked: ordina preferenze
3. Voto multiplo: scegli fino a N opzioni

Calcola:
- Vincitore assoluto (>50%)
- Ballottaggio se necessario
- Distribuzione percentuale
- Voti per demografia (se fornita)

Previeni voti duplicati per utente
"""

votazioni = {
    "opzioni": ["Pizza", "Pasta", "Risotto", "Lasagne"],
    "voti": [],  # {utente: id, voto: opzione}
    "tipo": "singolo"  # o "ranked" o "multiplo"
}

def vota(utente_id, scelta):
    # Gestisci votazione
    pass

def calcola_risultati():
    # Determina vincitore
    pass


# -----------------------------------------------------------------


#  Convertitore Valuta
### Combina: API simulate, Cache, Gestione errori



"""
Convertitore valuta con tassi di cambio.

Simula API con dizionario tassi (base EUR)
Supporta conversioni tra qualsiasi valuta
Cache risultati per 60 secondi
Gestisci valute non supportate
Arrotondamento appropriato

Bonus: storico conversioni, valuta preferita
"""

# Simula tassi di cambio (base EUR)
tassi_cambio = {
    "EUR": 1.0,
    "USD": 1.08,
    "GBP": 0.85,
    "JPY": 158.50,
    "CHF": 0.94,
    "CAD": 1.47
}

def converti_valuta(importo, da, a, usa_cache=True):
    """
    Converte importo tra valute
    Ritorna: (risultato, tasso_usato)
    """
    # Il tuo codice qui...
    pass

# Test conversioni varie

# -----------------------------------------------------------------

## NOTE PER L'USO

# ### Obiettivi degli esercizi:
# - Imparare a combinare diversi concetti
# - Sviluppare problem solving con strumenti multipli
# - Capire quando usare quale struttura dati
# - Praticare casi realistici di programmazione

# ### Come affrontarli:
# 1. Leggi tutto l'esercizio prima di iniziare
# 2. Pianifica la struttura dati da usare
# 3. Inizia semplice, poi aggiungi features
# 4. Testa incrementalmente** ogni funzione
# 5. Refactor quando funziona

# ### Suggerimenti:
# - Non cercare la perfezione al primo tentativo
# - Usa print() per debug
# - Dividi problemi complessi in funzioni piccole
# - Commenta il codice mentre scrivi
# - Confronta diverse soluzioni possibili



