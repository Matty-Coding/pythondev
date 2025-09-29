# Esercizi Python Completi
## Dalle Basi Assolute agli Argomenti Avanzati



## **PARTE 1: VARIABILI E TIPI - ESERCIZI FACILISSIMI**

### Esercizio 1.1 - Prima Variabile 


# Crea una variabile chiamata 'nome' con il tuo nome
# Stampala


### Esercizio 1.2 - Tipi Base 

# Crea queste variabili:
# - intero con valore 42
# - decimale con valore 3.14
# - testo con valore "Python"
# - booleano con valore True
# Stampa il tipo di ciascuna usando type()


### Esercizio 1.3 - Nomi Variabili 

# Quali di questi nomi sono VALIDI? (non eseguire, rispondi)
# 1. mia_variabile
# 2. 123abc
# 3. _private
# 4. class
# 5. MiaVariabile
# 6. mia-variabile
# 7. mia variabile
# 8. π
# 9. __dunder__
# 10. True


### Esercizio 1.4 - Assegnazione Multipla 

# Assegna in UNA sola riga:
# x = 1, y = 2, z = 3
# Poi scambia x e y in una riga


### Esercizio 1.5 - Costanti 

# Python non ha vere costanti. Come le indichiamo per convenzione?
# Crea una "costante" PI_GRECO
# Crea una "costante" GIORNI_SETTIMANA


### Esercizio 2.1 - Casting Base (2 minuti)

# Converti:
# "100" in intero
# 3.7 in intero (cosa succede?)
# 42 in stringa
# "3.14" in float
# 0 in booleano
# "" in booleano


### Esercizio 2.2 - Casting Problematico 

# Prova questi casting e gestisci gli errori:
# int("3.14") - fallisce!
# int("abc")
# float("12,34") - virgola invece di punto
# list("Python")
# str([1,2,3])
# bool("False") - risultato inaspettato!


### Esercizio 2.3 - Casting Avanzato 

# Converti:
# Lista [1,2,3] in stringa "123"
# Stringa "1,2,3,4,5" in lista di interi
# Dizionario {'a':1, 'b':2} in lista di tuple
# Lista di tuple [(1,2), (3,4)] in dizionario
# Range(5) in lista


### Esercizio 2.4 - Casting Particolare 

# Casi strani:
# bool("0") vs bool(0)
# int(True) + int(False)
# str(None)
# list("") vs list(" ")
# float('inf')
# complex("1+2j")




# IF/ELIF/ELSE - PROGRESSIONE

### Esercizio 3.1 - If Singolo 

# Scrivi un if che stampa "Maggiorenne" se età >= 18
eta = 20


### Esercizio 3.2 - If-Else 

# Numero pari o dispari?
numero = 7


### Esercizio 3.3 - If-Elif-Else 

# Classifica un voto:
# >= 90: Eccellente
# >= 80: Ottimo  
# >= 70: Buono
# >= 60: Sufficiente
# < 60: Insufficiente
voto = 75


### Esercizio 3.4 - If Annidati 

# Sistema di accesso:
# Prima controlla username
# Poi controlla password
# Poi controlla se account è attivo
username = "admin"
password = "12345"
attivo = True


### Esercizio 3.5 - Operatore Ternario 

# Riscrivi con operatore ternario:
# if x > 0:
#     segno = "positivo"
# else:
#     segno = "non positivo"


### Esercizio 3.6 - If con In 

# Controlla se:
# - Una lettera è vocale
# - Un numero è in una lista
# - Una chiave è in un dizionario
# - Una sottostringa è in una stringa


### Esercizio 3.7 - Casi Particolari If 

# Cosa stampano? (rispondi prima di eseguire)
if []:
    print("A")

if [0]:
    print("B")

if "":
    print("C")
    
if " ":
    print("D")

if 0.0:
    print("E")

if None:
    print("F")

x = 5
if 0 < x < 10:  # Chained comparison
    print("G")




# LISTE - TUTTI I LIVELLI

### Esercizio 4.1 - Creazione Liste 

# Crea:
# Lista vuota (2 modi)
# Lista di numeri 1-5
# Lista mista [1, "due", 3.0, True]
# Lista da stringa "Python"
# Lista da range(10)


### Esercizio 4.2 - Accesso Elementi 

lista = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# Estrai:
# Primo elemento
# Ultimo elemento
# Elemento centrale
# Primi 3 elementi
# Ultimi 3 elementi
# Elementi dal 3° al 7°
# Elementi a indici pari
# Lista inversa


### Esercizio 4.3 - Modifica Liste 

numeri = [1, 2, 3, 4, 5]
# Esegui:
# Aggiungi 6 alla fine
# Inserisci 0 all'inizio
# Rimuovi il 3
# Sostituisci 4 con 40
# Estendi con [7, 8, 9]
# Svuota la lista


### Esercizio 4.4 - Metodi Liste 

frutti = ["mela", "banana", "mela", "pera", "banana", "mela"]
# Usa:
# count() per contare le mele
# index() per trovare la prima banana
# reverse() per invertire
# sort() per ordinare
# copy() per fare una copia
# pop() per rimuovere l'ultimo
# clear() per svuotare


### Esercizio 4.5 - List Comprehension 

# Crea con list comprehension:
# Quadrati da 0 a 9
# Numeri pari da 0 a 20
# Lettere maiuscole da una stringa
# Lista di (numero, quadrato) per 1-5
# Numeri divisibili per 3 o 5 fino a 30


### Esercizio 4.6 - Liste Annidate 

# Crea e manipola:
# Matrice 3x3 di zeri
# Accedi all'elemento [1][2]
# Modifica una riga intera
# Estrai una colonna
# Appiattisci la matrice


### Esercizio 4.7 - Casi Particolari Liste 

# Spiega cosa succede:

# Caso 1: Moltiplicazione lista
a = [[0] * 3] * 3
a[0][0] = 1
print(a)  # Perché modifica tutte le righe?

# Caso 2: Modifica durante iterazione
numeri = [1, 2, 3, 4, 5]
for i in range(len(numeri)):
    if numeri[i] % 2 == 0:
        numeri.remove(numeri[i])  # Problema?

# Caso 3: Lista come default parameter
def aggiungi(item, lista=[]):
    lista.append(item)
    return lista

print(aggiungi(1))
print(aggiungi(2))  # Perché [1, 2] invece di [2]?

# Caso 4: Slicing con step negativo
x = [0, 1, 2, 3, 4, 5]
print(x[5:2:-1])
print(x[::-2])




#PARTE 5: DIZIONARI - COMPLETO

### Esercizio 5.1 - Creazione Dizionari 

# Crea:
# Dizionario vuoto (2 modi)
# {"nome": "Mario", "età": 25}
# Da lista di tuple: [(1, 'uno'), (2, 'due')]
# Da due liste con zip()
# Con dict comprehension da range(5)


### Esercizio 5.2 - Accesso e Modifica 

persona = {"nome": "Anna", "età": 30, "città": "Roma"}
# Esegui:
# Accedi a 'nome'
# Accedi a 'lavoro' con get() (non esiste)
# Aggiungi 'lavoro': 'Ingegnere'
# Modifica 'età' a 31
# Rimuovi 'città'
# Controlla se 'email' esiste


### Esercizio 5.3 - Metodi Dizionari 

d1 = {"a": 1, "b": 2}
d2 = {"b": 3, "c": 4}
# Usa:
# keys(), values(), items()
# update() per unire d2 in d1
# pop() per rimuovere con default
# setdefault() per aggiungere se non esiste
# copy() per copiare


### Esercizio 5.4 - Dict Comprehension 

# Crea:
# {x: x**2} per x da 1 a 5
# Inverti chiavi e valori di un dizionario
# Filtra dizionario per valori > 10
# Crea da stringa: conta lettere
# Raggruppa lista di tuple per primo elemento


### Esercizio 5.5 - Dizionari Annidati 

# Gestisci:
scuola = {
    "classe_1A": {
        "studenti": 25,
        "voti": {"mario": 8, "anna": 9}
    },
    "classe_1B": {
        "studenti": 22,
        "voti": {"luigi": 7, "sara": 10}
    }
}
# Accedi al voto di Anna
# Aggiungi nuovo studente in 1A
# Calcola media voti 1B
# Trova classe con più studenti


### Esercizio 5.6 - Casi Particolari Dizionari 

# Cosa succede?

# Caso 1: Chiavi mutabili
# d = {[1,2]: "lista"}  # Errore!

# Caso 2: fromkeys con valore mutabile
d = dict.fromkeys(['a', 'b', 'c'], [])
d['a'].append(1)
print(d)  # Tutte le chiavi condividono la lista!

# Caso 3: Dizionario che cambia durante iterazione
d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
    if d[key] == 2:
        del d[key]  # RuntimeError!

# Caso 4: ChainMap
from collections import ChainMap
default = {'color': 'red', 'size': 10}
custom = {'color': 'blue'}
combined = ChainMap(custom, default)
print(combined['color'])  # ?
print(combined['size'])   # ?




#FOR LOOPS - PROGRESSIVO**

### Esercizio 6.1 - For Base 

# Itera su:
# range(5)
# Lista [10, 20, 30]
# Stringa "Python"
# Dizionario {"a": 1, "b": 2}


### Esercizio 6.2 - For con Range 

# Stampa:
# Numeri da 1 a 10
# Numeri da 10 a 1 (decrescente)
# Numeri pari da 0 a 20
# Multipli di 5 da 0 a 50
# Tabellina del 7


### Esercizio 6.3 - For con Break e Continue 

# In una lista di numeri 1-20:
# Trova il primo multiplo di 7 (break)
# Stampa solo i dispari (continue)
# Cerca un numero, stampa posizione o "non trovato" (else)


## Esercizio 6.4 - For Annidati 

# Crea:
# Tabella pitagorica 5x5
# Pattern:
#   *
#   **
#   ***
#   ****
# Tutte le coppie possibili da due liste


### Esercizio 6.5 - For su Strutture Complesse 

# Itera su:
studenti = [
    {"nome": "Mario", "voti": [8, 7, 9]},
    {"nome": "Anna", "voti": [10, 9, 10]},
    {"nome": "Luigi", "voti": [6, 7, 6]}
]
# Calcola media per ogni studente
# Trova studente con media più alta
# Stampa tutti i voti > 8


# Esercizio 6.6 - Casi Particolari For 

# Analizza:

# Caso 1: Modifica lista durante iterazione
lista = [1, 2, 3, 4, 5]
for x in lista:
    lista.append(x * 2)  # Loop infinito!

# Caso 2: For con else
for i in range(5):
    if i == 10:
        break
else:
    print("Completato")  # Quando viene eseguito?

# Caso 3: Unpacking in for
points = [(1, 2), (3, 4), (5, 6)]
for x, y in points:
    print(f"x={x}, y={y}")

# Caso 4: For su dictionary.items()
d = {'a': 1, 'b': 2}
for k, v in d.items():
    print(k, v)




#PARTE 7: ENUMERATE, ZIP, MAP, FILTER**

### Esercizio 7.1 - Enumerate Base

frutti = ["mela", "banana", "pera"]
# Stampa:
# 0: mela
# 1: banana
# 2: pera
# Poi con start=1 per numerazione da 1


### Esercizio 7.2 - Enumerate Avanzato

# Usa enumerate per:
# Trovare indici di tutti gli elementi > 5 in una lista
# Creare dizionario {indice: valore}
# Modificare elementi a indici pari
# Trovare posizione prima occorrenza di un valore


# Esercizio 7.3 - Zip Base

nomi = ["Mario", "Anna", "Luigi"]
età = [25, 30, 22]
città = ["Roma", "Milano", "Napoli"]
# Combina in:
# Lista di tuple
# Dizionario nome->età
# Stampa formattata di tutti i dati


# Esercizio 7.4 - Zip Avanzato

# Con zip:
# Trasponi una matrice
# Unisci liste di lunghezza diversa (cosa succede?)
# Crea coppie consecutive [1,2,3,4] -> [(1,2), (2,3), (3,4)]
# Unzip: separa lista di tuple in liste separate


### Esercizio 7.5 - Map Base 

numeri = [1, 2, 3, 4, 5]
# Usa map per:
# Calcolare quadrati
# Convertire in stringhe
# Applicare funzione personalizzata


### Esercizio 7.6 - Map Avanzato

# Con map:
# Applica funzione a multiple liste
# map con lambda
# map con metodi: lista.upper() su lista stringhe
# Combina map con altri iteratori


# Esercizio 7.7 - Filter Base

numeri = range(1, 21)
# Filtra:
# Numeri pari
# Numeri > 10
# Numeri primi 


### Esercizio 7.8 - Filter Avanzato 

# Con filter:
parole = ["python", "java", "c++", "javascript", "go", "rust"]
# Parole con lunghezza > 3
# Parole che iniziano con 'j'
# Parole che contengono 'a'
# Combina più filtri


### Esercizio 7.9 - Combinazioni 

# Combina enumerate, zip, map, filter:

# Data: lista di dizionari studenti
studenti = [
    {"nome": "Mario", "età": 22, "voto": 85},
    {"nome": "Anna", "età": 21, "voto": 92},
    {"nome": "Luigi", "età": 23, "voto": 78},
    {"nome": "Sara", "età": 20, "voto": 95}
]

# 1. Enumera studenti con voto > 80
# 2. Crea zip di (nomi, voti) solo per maggiorenni
# 3. Map per aumentare tutti i voti del 10%
# 4. Filter + map: nomi in maiuscolo di chi ha > 90
# 5. Crea ranking con enumerate dopo sort per voto


### Esercizio 7.10 - Casi Particolari 

# Situazioni strane:

# zip con lunghezze diverse
a = [1, 2, 3]
b = ['a', 'b']
print(list(zip(a, b)))  # Cosa manca?

# zip per unzip
pairs = [(1, 'a'), (2, 'b'), (3, 'c')]
numbers, letters = zip(*pairs)  # Unpacking

# map con None (Python 2 legacy, non funziona in Python 3)
# map(None, [1,2], ['a','b'])

# filter con None
print(list(filter(None, [0, 1, '', 'hello', [], [1]])))  # Filtra "falsy"

# enumerate su dizionario
d = {'a': 1, 'b': 2}
for i, (k, v) in enumerate(d.items()):
    print(i, k, v)

# zip stesso iterabile
nums = [1, 2, 3, 4]
for a, b in zip(nums, nums[1:]):
    print(f"{a} -> {b}")  # Coppie consecutive

# map con più argomenti
def somma(x, y, z):
    return x + y + z
result = list(map(somma, [1,2], [10,20], [100,200]))




# ESERCIZI MISTI AVANZATI

### Esercizio 8.1 - Sistema Voti 

# Crea un sistema che:
# 1. Accetta lista di studenti con voti
# 2. Calcola medie
# 3. Assegna lettere (A, B, C, D, F)
# 4. Trova top 3 studenti
# 5. Identifica chi deve recuperare
# Usa: dict comprehension, filter, map, sorted


### Esercizio 8.2 - Analisi Testo

testo = """Python è un linguaggio di programmazione. 
           Python è facile da imparare. 
           Python è potente e versatile."""

# Calcola:
# 1. Parole più frequenti (usa Counter o manualmente)
# 2. Lunghezza media parole
# 3. Frasi che contengono "Python"
# 4. Rimuovi duplicati mantenendo ordine
# 5. Crea indice: {parola: [posizioni]}


### Esercizio 8.3 - Gestione Inventario 

inventario = {
    "mele": {"quantità": 50, "prezzo": 0.5},
    "banane": {"quantità": 30, "prezzo": 0.3},
    "arance": {"quantità": 0, "prezzo": 0.4}
}

ordini = [
    {"prodotto": "mele", "quantità": 10},
    {"prodotto": "banane", "quantità": 35},  # Non disponibile
    {"prodotto": "pere", "quantità": 5}      # Non esiste
]

# Implementa:
# 1. Controlla disponibilità
# 2. Processa ordini validi
# 3. Aggiorna inventario
# 4. Calcola totale vendite
# 5. Trova prodotti esauriti
# 6. Suggerisci riordino (< 10 pezzi)


### Esercizio 8.4 - Matrice Operations 

# Senza NumPy, implementa:
matrice = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# 1. Trasponi
# 2. Somma righe
# 3. Somma colonne
# 4. Diagonale principale
# 5. Diagonale secondaria
# 6. Ruota 90° clockwise
# 7. Trova max/min
# 8. Appiattisci


### Esercizio 8.5 - Parser CSV Semplice

csv_data = """nome,età,città,salario
Mario,25,Roma,30000
Anna,30,Milano,45000
Luigi,22,Napoli,28000
Sara,28,Torino,38000"""

# Senza librerie esterne:
# 1. Parse in lista di dizionari
# 2. Filtra per età > 25
# 3. Ordina per salario
# 4. Calcola salario medio
# 5. Raggruppa per città
# 6. Trova min/max salario
# 7. Converti in formato JSON-like




#PARTE 9: CASI SUPER STRANI**

### Esercizio 9.1 - Python Quirks 

# Predici output senza eseguire:

# 1. Integers caching
a = 256
b = 256
print(a is b)  # ?

a = 257
b = 257
print(a is b)  # ?

# 2. Mutable default
def f(x, lista=[]):
    lista.append(x)
    return lista

print(f(1))
print(f(2))  # ?

# 3. Late binding closure
funcs = []
for i in range(3):
    funcs.append(lambda: i)

for f in funcs:
    print(f())  # ?

# 4. Chained operations
a = [1, 2]
b = a
a = a + [3]
print(b)  # ?

a = [1, 2]
b = a
a += [3]
print(b)  # ?


### Esercizio 9.2 - Type Coercion 

# Cosa succede?

print(True + True)  # ?
print(False - True)  # ?
print(True * 50)  # ?

print("5" * 3)  # ?
print(3 * "5")  # ?

print([] + [])  # ?
print({} or "default")  # ?
print("" or "default")  # ?

print(all([]))  # ?
print(any([]))  # ?

print(bool("False"))  # ?
print(bool(" "))  # ?


### Esercizio 9.3 - Scope Traps 

# Trova e correggi i problemi:

# 1.
x = 10
def func():
    print(x)  # UnboundLocalError!
    x = 20

# 2.
total = 0
def add(val):
    total += val  # UnboundLocalError!
    return total

# 3.
for i in range(5):
    pass
print(i)  # i esiste qui!

# 4.
[x for x in range(5)]
print(x)  # x esiste? 


### Esercizio 9.4 - Dictionary Madness 

# Casi estremi:

# 1. Keys must be immutable
d = {}
d[(1, 2)] = "ok"  # Tuple ok
# d[[1, 2]] = "no"  # List no!
d[frozenset([1, 2])] = "ok"  # Frozenset ok

# 2. Dictionary cambia durante iterazione
d = {i: i**2 for i in range(5)}
for k in list(d.keys()):  # Perché list()?
    if k % 2 == 0:
        del d[k]

# 3. setdefault magic
d = {}
d.setdefault('key', []).append(1)
d.setdefault('key', []).append(2)
print(d)  # ?

# 4. Dictionary merge evolution
d1 = {'a': 1, 'b': 2}
d2 = {'b': 3, 'c': 4}
# Python 3.5+
d3 = {**d1, **d2}
# Python 3.9+
d4 = d1 | d2


# Esercizio 9.5 - List Mutation Chaos 

# Comportamenti inaspettati:

# 1. Slice assignment
a = [1, 2, 3, 4, 5]
a[1:4] = [20]  # Sostituisce 3 elementi con 1
print(a)  # ?

# 2. Extended slicing
a = list(range(10))
a[::2] = [99] * 5  # Sostituisce elementi a indici pari
print(a)  # ?

# 3. List multiplication trap
matrix = [[0] * 3] * 3
matrix[0][0] = 1
print(matrix)  # Tutte le righe cambiate!

# 4. In-place vs new object
a = [1, 2, 3]
b = a
a += [4]  # In-place
print(b)  # ?

a = [1, 2, 3]
b = a
a = a + [4]  # New object
print(b)  # ?

# 5. Sort vs Sorted
a = [3, 1, 2]
b = sorted(a)  # Returns new
c = a.sort()   # Returns None!
print(a, b, c)  # ?




#PARTE 10: SFIDE

### Sfida 1 - One-Liners 

# Risolvi in UNA riga:
# 1. FizzBuzz da 1 a 100
# 2. Palindromo checker
# 3. Fibonacci fino a n
# 4. Trova tutti i primi fino a 100
# 5. Transpose matrix
# 6. Flatten nested list
# 7. Remove duplicates mantenendo ordine
# 8. Anagramma checker


### Sfida 2 - No Loops Challenge 

# Risolvi SENZA for/while (usa map, filter, reduce, comprehension):
# 1. Somma numeri da 1 a 100
# 2. Prodotto elementi lista
# 3. Conta occorrenze elemento
# 4. Trova massimo
# 5. Reverse stringa
# 6. Check se tutti elementi sono unici


### Sfida 3 - Type Gymnastics 

# Converti tra tutti questi formati:
data_dict = {"a": 1, "b": 2, "c": 3}
data_list = [("a", 1), ("b", 2), ("c", 3)]
data_str = "a=1,b=2,c=3"
data_json = '{"a": 1, "b": 2, "c": 3}'
data_keys = ["a", "b", "c"]
data_values = [1, 2, 3]

# Implementa conversioni in tutte le direzioni


### Sfida 4 - Iterator Protocol 

# Crea classe che:
# 1. È iterabile
# 2. Genera numeri di Fibonacci
# 3. Ha limite massimo
# 4. Può essere resettata
# 5. Supporta slicing [start:stop]


### Sfida 5 - Meta Programming 

# Crea dizionario che:
# 1. Logga tutti gli accessi
# 2. Conta quante volte ogni chiave è acceduta
# 3. Previene eliminazione di certe chiavi
# 4. Auto-salva su file ogni modifica
# 5. Ha history degli ultimi 10 cambiamenti
