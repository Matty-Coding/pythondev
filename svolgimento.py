# VARIABILI E TIPI - ESERCIZI FACILISSIMI

# Esercizio 1.1 - Prima Variabile

# nome = "Mattia"
# print(nome)


# Esercizio 1.2 - Tipi Base

# intero = int(42)
# decimale = float(3.14)
# testo = str("Python")
# booleano = bool(True)

# print(type(intero))
# print(type(decimale))
# print(type(testo))
# print(type(booleano))


# Esercizio 1.3 - Nomi Variabili

# 1, 3, 5, 9


# Esercizio 1.4 Assegnazione Multipla

# y, x, z = 2, 1, 3


# Esercizio 1.5 - Costanti

# PI_GRECO = float(3.14)
# GIORNI_SETTIMANA = int(7)


# Esercizio 2.1 - Casting Base 

# a = int("100")
# b = int(3.7)  # valore decimale rimosso senza arrotondamento
# c = str(42)
# d = float("3.14")
# e = bool(0)  # return False
# f = bool("") # return False


# Esercizio 2.2 - Casting Problematico

# a = int("3.14") # servirebbe double casting --> int(float(a))
# b = int("abc") # non possibile, stringe alfanumeriche non possono essere interi
# c = float("12,34") # non possibile, la virgola viene presa come carattere di stringa servirebbe una sostituzione --> 12.34
# d = list("Python")
# e = str([1, 2, 3]) # non possibile, servirebbe iterare nella lista e convertire i valori singoli
# f = bool("False") # non corretto, bool si chiede True, False ma la stringa risulta True se pur sia scritto False come caratteri interni 


# Esercizio 2.3 - Casting Avanzato

# lista = [1, 2, 3]
# stringa = ""
# for i in lista:
#     stringa += str(i)

# print(stringa)
# print(type(stringa))

# --------------------

# stringa = "1,2,3,4,5"
# lista = []
# for i in stringa:
#     try:
#         i = int(i)
#         lista.append(i)
#         print(f"{i} convertibile in intero, aggiunto alla lista")

#     except ValueError:
#         print(f"{i} non convertibile in intero, escluso dalla lista")

# print(lista)
# print(type(lista[0]))

# ---------------------

# dizionario = {"a" : 1, "b" : 2}
# lista = []
# for k, v in dizionario.items():
#     lista.append((k, v))

# print(lista)
# print(type(lista[0]))

# ----------------------

# lista = [(1, 2), (3, 4)]
# dizionario = {}
# for i in lista:
#     dizionario[i[0]] = i[1]

# print(dizionario)
# print(type(dizionario))

# ----------------------

# a = range(5)
# lista = []
# for i in a:
#     lista.append(i)

# print(lista)
# print(type(lista))


# Esercizio 2.4 - Casting Particolare

# true (stringa è vera) vs false (0 è falso)
# binary --> int(True) = 1, int(False) = 0 --> 1 + 0 = 1
# str(None) --> istruzione python per identificare valore non presente, non causa errore
# list("") = lista vuota vs list(" ") = lista con un elemento di tipo stringa vuota (spazio)
# float non converte correttamente le stringhe ma non da errore
# ritorna il numero complesso con le parentesi

# -- curiosità --
# print(float('inf'))   # infinite
# print(float('-inf'))  # -infinite
# print(float('nan'))   # nan (not a number)
# print(float('nan') == float('nan'))  # False
# print(float('nan') is float('nan'))  # False
# print(float('nan') != float('nan'))  # True
# print(type(float('nan')))  # <class 'float'>
# print(int(float('nan')))  # Errore ValueError
# print(int(float('inf')))  # Errore OverflowError
# print(str(float('inf')))  # "inf"


# IF/ELIF/ELSE - PROGRESSIONE

# Esercizio 3.1 - If Singolo

# eta = 20
# if eta >= 18:
#     print("Maggiorenne")


# Esercizio 3.2 - If-Else

# numero = 10
# if numero % 2 == 0:
#     print("Numero pari")
# else:
#     print("Numero dispari")


# Esercizio 3.3 - If-Elif-Else

# voto = 75
# if voto >= 90:
#     print("Eccellente")
# elif voto >= 80:
#     print("Ottimo")
# elif voto >= 70:
#     print("Buono")
# elif voto >= 60:
#     print("Sufficiente")
# elif voto < 60:
#     print("Insufficiente")
# else:
#     print("Valore inserito non valido, stringhe non consentite")


# Esercizio 3.4 - If Annidati

# username = "admin"
# password = "12345"
# attivo = True
# if username:
#     if password:
#         if attivo == True:
#             pass


# Esercizio 3.5 - Operatore Ternario

# x = 3
# segno = "positivo" if x > 0 else "non positivo"


# Esercizio 3.6 - If con In

# vocali = ("a", "e", "i", "o", "u")
# lettera = "a" # vero
# # lettera = "r" # falso
# if lettera in vocali:
#     print(lettera, "è una vocale")
# else:
#     print(lettera, "non presente")

# # -------------------------

# lista = [2, 3, 5, 6]
# # numero = 3 # vero
# numero = 1 # falso
# if numero in lista:
#     print(numero, "è nella lista")
# else:
#     print(numero , "non presente")

# # -------------------------

# dizionario = {"nome" : "mario", "cognome" : "rossi", "anni" : 33}
# # chiave = "anni" # vero
# chiave = "casa" # falso
# if chiave in dizionario.keys():
#     print(chiave, "è nel dizionario")
# else:
#     print(chiave, "non presente")

# # -------------------------

# stringa = "michiamoluca"
# # string = "luca" # vero
# string = "mario" # falso
# if string in stringa:
#     print(string, "è nella stringa")
# else:
#     print(string, "non è presente")


# Esercizio 3.7 - Casi Particolari If

# if []:
#     print("A")   # lista vuota, il print NON si verifica

# if [0]:
#     print("B")   # lista con elemento, il print SI verifica

# if "":
#     print("C")   # stringa vuota, il print NON si verifica

# if " ":
#     print("D")   # stringa con spazio (elemento valido), il print SI verifica

# if 0.0:
#     print("E")     # valore nullo, il print NON si verifica 

# if None:
#     print("F")       # None (elemento nullo di Python), il print NON si verifica

# x = 5
# if 0 < x < 10:         # il valore è compreso (rispetta almeno uno delle condizioni (OR))
    
#     print("G")        # il print SI verifica


# LISTE - TUTTI I LIVELLI

# Esercizio 4.1 - Creazione Liste

# lista_vuota = []
# print(lista_vuota, type(lista_vuota))

# lista_vuota1 = list()
# print(lista_vuota1, type(lista_vuota1))

# ------------------

# lista_1_5 = [i + 1 for i in range(5)] # metodo 1
# lista_1_5 = [i for i in range(1, 6)]  # metodo 2

# -------------------

#lista_mista = [1, "due", 3.0, True]

# ----------------------

# stringa = "Python"
# lista = []
# for i in stringa:
#     lista.append(i)

# print(lista)

# ---------------------------

# a = range(10)
# lista = []
# for i in a:
#     lista.append(i)

# print(lista)
 

# Esercizio 4.2 - Accesso Elementi

# lista = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# primo = lista[0]
# ultimo = lista[-1]

# elementi = len(lista)
# if elementi % 2 == 0:
#     a = int(len(lista) / 2)
#     centrale = [lista[a - 1], lista[a]]
# else:
#     centrale = lista[int(len(lista) / 2)]

# print(centrale)

# primi3 = lista[:3]
# ultimi3 = lista[-3:]
# terzo_settimo = lista[2:7]

# indici_pari = [v for i, v in enumerate(lista, 1) if i % 2 == 0]
# print(indici_pari)

# lista.reverse()
# print(lista)


# Esercizio 4.3 - Modifica Liste

# numeri = [1, 2, 3, 4, 5]

# numeri.append(6)
# print(numeri)

# numeri.insert(0, 0)
# print(numeri)

# numeri.remove(3)
# print(numeri)

# indice_sostituisci = numeri.index(4)
# numeri.pop(indice_sostituisci)
# sostituisci = numeri.insert(indice_sostituisci, 40)
# print(numeri)

# estendi = [7, 8, 9]
# numeri.extend(estendi)
# print(numeri)

# numeri.clear()
# print(numeri)


# Esercizio 4.4 - Metodi Liste

# frutti = ["mela", "banana", "mela", "pera", "banana", "mela"]

# mele = frutti.count("mele")
# print(mele)

# prima_banana = frutti.index("banana")
# print(prima_banana)

# frutti.reverse()  
# print(frutti)

# frutti.sort()
# print(frutti)

# copia = frutti.copy()
# print(frutti, "\n", copia)

# frutti.pop(-1)
# print(frutti)

# frutti.clear()
# print(frutti)


# Esercizio 4.5 - List Comprehension

# quadrati = [i ** 2 for i in range(10)]
# print(quadrati)

# pari = [i for i in range(21) if i % 2 == 0]
# print(pari)

# maiuscole = [i for i in "AbCdE" if i == i.capitalize()]
# print(maiuscole)

# lista = [[i, i ** 2] for i in range(1, 6)]
# print(lista)

# divisibili = [i for i in range(1, 31) if i % 3 == 0 or i % 5 == 0]
# print(divisibili)


# Esercizio 4.7 - Casi Particolari Liste

# a = [[0] * 3] * 3
# creazione lista, con dentro una lista con 3 elementi (inizializzati a 0) 
# moltiplicato 3 volte (quindi 3 liste del tipo precedentemente detto)

# a[0][0] = 1
# sto accedendo alla lista generale e poi nidificando al primo elemento del singolo assegnando valore 1

# print(a)
# si verifica in tutte le liste poichè accedendo alla lista, in-line è specificato di creare 3 liste uguali

# --------------------

# numeri = [1, 2, 3, 4, 5]
# for i in range(len(numeri)):
#     if numeri[i] % 2 == 0:
#         numeri.remove(numeri[i])  

# eseguire operazioni sugli indici all'interno di un ciclo (specie rimozione/aggiunta) 
# comporta un'alterazione degli stessi, si finisce in un errore di indicizzazione

# ------------------------

# def aggiungi(item, lista=[]):
#     lista.append(item)
#     return lista

# print(aggiungi(1))
# print(aggiungi(2))  

# richiamando la funzione una seconda volta la lista non sarà più vuota ma corrisponderà a [1]
# pertanto passando come nuovo parametro l'elemento di valore 2 il risultato in output sarà [1, 2]

# --------------------------

# x = [0, 1, 2, 3, 4, 5]

# print(x[5:2:-1])
# va interpretato come la funzione range(x, y, z) con 3 elementi dove (x = inizio, y = fine, z = progressione) quindi:
# si parte da x[5] 
# si arriva fino a x[3] poichè in reverse l'indice minore viene escluso dallo slicing 
# infine si specifica la progressione -1
# si ha quindi --> x[3:5] in reverse di 1 (non salta valori), ovvero --> [5, 4, 3]

# print(x[::-2])
# seguendo il ragionamento descritto per l'esercizio precedente...
# si ha come inizio x[:] --> ovvero tutta la lista
# si ha come fine x[:] --> ovvero tutta la lista 
# infine si specifica la progressione -2
# si ha quindi --> x[:] in reverse di 2 (salta valori a 2 a 2), ovvero --> [5, 3, 1]



# DIZIONARI - COMPLETO

# Esercizio 5.1 - Creazione Dizionari

# diz_vuoto = {}
# print(diz_vuoto, type(diz_vuoto))

# diz_vuoto1 = dict()
# print(diz_vuoto1, type(diz_vuoto1))

# -----------------

# diz = {"nome" : "Mario", "età" : 25}
# print(diz, type(diz))

# ------------------

# lista_tuple = [(1, "uno"), (2, "due")]
# diz = {}
# for i in lista_tuple:
#     diz[i[0]] = i[1]

# print(diz)

# ------------------------

# lista = ["nome", "cognome"]
# lista1 = ["mario", "rossi"]
# diz = {}
# for i, k in zip(lista, lista1):
#     diz[i] = k

# print(diz)

# ------------------

# diz = {f"chiave{i}" : f"valore{i}" for i in range(5)}
# print(diz)


# Esercizio 5.2 - Accesso e Modifica

# persona = {"nome": "Anna", "età": 30, "città": "Roma"}

# nome = persona["nome"]
# print(nome)

# lavoro = persona.get("lavoro", "lavoro predefinito")
# # il secondo parametro nella funzione get per accedere ai valori di un dict 
# # imposta tale parametro come valore di default qualora la ricerca restituisse None
# print(lavoro)

# persona["lavoro"] = "Ingegnere"
# print(persona)

# persona["età"] = 31
# print(persona)

# persona.pop("città")
# print(persona)

# if "email" in persona:
#     print("La key 'email' esiste.")
# else:
#     print("La key 'email' non esiste.")


# Esercizio 5.3 - Metodi Dizionari

# d1 = {"a": 1, "b": 2}
# d2 = {"b": 3, "c": 4}

# print(d1.keys())
# print(d1.values())
# print(d1.items())

# d1.update(d2)
# print(d1)
# # si noti la presenza di chiavi con stesso nome
# # la chiave presente nel dict che viene implementato sostituirà il suo valore
# # rimpiazzando quello presente alla stessa chiave nel dict primario

# rimozione = d2.pop("e", "default (non è presente la chiave inserita)")
# print(d2, "valore della chiave rimossa -->", rimozione)

# d2.setdefault("email")
# print(d2)

# d3 = d2.copy()
# print(d3)


# Esercizio 5.4 - Dict Comprehension

# diz = {x : x ** 2 for x in range(1, 6)}
# print(diz)

# diz1 = {v : k for k, v in diz.items()}
# print(diz1)

# diz2 = {k : v for k, v in diz.items() if v > 10}
# print(diz2) 

# stringa = "sonounastringa"
# diz3 = {i : k for i, k in enumerate(stringa, 1)}
# print(diz3)

# lista_tuple = [("a", 1), ("b", 2), ("a", 4)]
# diz4 = {i[0] : [k[1] for k in lista_tuple if k[0] == i[0]] for i in lista_tuple}
# print(diz4)


# Esercizio 5.5 - Dizionari Annidati

# scuola = {
#     "classe_1A": {
#         "studenti": 25,
#         "voti": {"mario": 8, "anna": 9}
#     },
#     "classe_1B": {
#         "studenti": 22,
#         "voti": {"luigi": 7, "sara": 10}
#     }
# }

# voto_anna = scuola.get("classe_1A").get("voti").get("anna")
# print(voto_anna)

# scuola["classe_1A"]["studenti"] = 26
# scuola["classe_1A"]["voti"] = {"luca" : 7}
# print(scuola)

# voti1B = scuola["classe_1B"]["voti"]
# media1B = round(sum(voti1B.values()) / len(voti1B.values()), 2)
# print(media1B)

# studenti_1A = scuola["classe_1A"]["studenti"]
# studenti_1B = scuola["classe_1B"]["studenti"]

# if int(studenti_1A) > int(studenti_1B):
#     print("La classe con più studenti corrisponde a -->", studenti_1A)
# else:
#     print("La classe con più studenti corrisponde a -->", studenti_1B)


# Esercizio 5.6 - Casi Particolari Dizionari

# d = {[1, 2] : "lista"}
# le chiavi di un dict DEVONO necessariamente essere un singolo elemento e non mutabile

# ----------------

# d = dict.fromkeys(['a', 'b', 'c'], [])
# d['a'].append(1)
# print(d) 
# si sta assegnando la medesima lista a tutte le chiavi del dict

# ---------------------

# d = {'a': 1, 'b': 2, 'c': 3}
# for key in d:
#     if d[key] == 2:
#         del d[key]  # RuntimeError!

# non si possono effettuare operazioni che alterano la dimensione del dict all'interno di un ciclo

# ----------------------

# from collections import ChainMap

# default = {'color': 'red', 'size': 10}
# custom = {'color': 'blue'}
# combined = ChainMap(custom, default)
# # la funzione utilizzata crea una lista di dizionari 
# # per poterli visualizzare tutti insieme

# print(combined['color']) 
# # accedendo ad una chiave ripetuta
# # si prende come valore il primo che si trova
# # la funzione cercherà in ordine di come sono stati assegnati i dict

# print(combined['size'])   
# # accedendo ad una chiave presente una sola volta
# # si prende il valore corrispondente come in un normale dizionario singolo



# FOR LOOPS - PROGRESSIVO

# Esercizio 6.1 - For Base

# for i in range(5):
#     print(i)

# lista = [10, 20, 30]
# for i in lista:
#     print(i)

# stringa = "Python"
# for i in stringa:
#     print(i)

# dizionario = {"a" : 1, "b" : 2}
# for i in dizionario:
#     print(i)


# Esercizio 6.2 - For con Range

# for i in range(1, 11):
#     print(i)

# for i in range(10, 0, -1):
#     print(i)

# for i in range(0, 21, 2):
#     print(i)

# for i in range(0, 51, 5):
#     print(i)

# for i in range(7, 71, 7):
#     print(i)


# Esercizi 6.3 - For con Break e Continue

# lista = [i for i in range(1, 21)]

# for i in lista:
#     if i / 7 == 2:
#         print("Il primo multiplo di 7 corrisponde a -->", i)
#         break
    
# for i in lista:
#     if i % 2 == 0:
#         continue
#     print("Numero disparo -->", i)

# from random import randint

# n = randint(1, 30)
# for i, k in enumerate(lista):
#     if k == n:
#         print(n, "si trova in posizione", i)
#         break
# else:
#     print(n, "non trovato")


# Esercizio 6.4 - For Annidati

# for i in range(1, 5):
#     print("*" * i)

# lista = [1, 2, 3]
# lista1 = [4, 5, 6]

# coppie = []
# for i in lista:
#     for k in lista1:
#         coppie.append([i, k])

# print(coppie)


# Esercizio 6.5 - For su Strutture Complesse

# studenti = [
#     {"nome": "Mario", "voti": [8, 7, 9]},
#     {"nome": "Anna", "voti": [10, 9, 10]},
#     {"nome": "Luigi", "voti": [6, 7, 6]}
# ]

# medie = []
# for i in studenti:
#     media = round(sum(i["voti"]) / len(i["voti"]), 2)
#     medie.append([media, i["nome"]])

# print(medie)

# medie.sort(reverse=True)
# migliore = medie[0]
# print(migliore[1], migliore[0])

# for i in medie:
#     if i[0] > 8:
#         print(i[1], i[0])


# Esercizio 6.6 - Casi Particolari For

# lista = [1, 2, 3, 4, 5]
# for x in lista:
#     lista.append(x * 2)  # Loop infinito!

# aggiungere elementi ad una lista mentre si itera su di essa genera un loop infinito

# ---------------

# for i in range(5):
#     if i == 10:
#         break
# else:
#     print("Completato")  # Quando viene eseguito?

# il print nell'else di un for si verifica al termine del ciclo

# --------------------

# points = [(1, 2), (3, 4), (5, 6)]
# for x, y in points:
#     print(f"x={x}, y={y}")

# assegno le coppie di valori delle tuple nella lista
# a due variabili x, y ad ogni ciclo

# ----------------------

# d = {'a': 1, 'b': 2}
# for k, v in d.items():
#     print(k, v)

# itera ad ogni ciclo le coppie chiave : valore di un 



# ENUMERATE, ZIP, MAP, FILTER


# Esercizio 7.1 - Enumerate Base

# frutti = ["mela", "banana", "pera"]

# for index, value in enumerate(frutti):
#     print(f"{index}: {value}")

# for index, value in enumerate(frutti, start=1):
#     print(f"{index}: {value}")


# Esercizio 7.2 - Enumerate Avanzato

# lista = [6, 1, 5, 7]
# for i, v in enumerate(lista):
#     if v > 5:
#         print(f"{i} corrisponde all'indice di un elemento con valore superiore a 5")

# diz = {i : v for i, v in enumerate(lista, 1)}
# print(diz)

# for i, v in enumerate(lista):
#     if i % 2 == 0:
#         lista[i] = v + 1

# print(lista)

# for i, v in enumerate(lista):
#     if v == 6:
#         print(f"6 si trova in posizione {i} nella lista.")
#         break 


# Esercizio 7.3 - Zip Base

# nomi = ["Mario", "Anna", "Luigi"]
# età = [25, 30, 22]
# città = ["Roma", "Milano", "Napoli"]

# lista_tuple = [(a, b, c) for a, b, c in zip(nomi, età, città)]
# print(lista_tuple)

# diz = {a : b for a, b in zip(nomi, età)}
# print(diz)

# for i in lista_tuple:
#     print(f"{i[0]} ha {i[1]} anni e vive a {i[2]}")


# Esercizio 7.4 - Zip Avanzato

# matrice = [
#     [1, 2, 3],
#     [4, 5, 6]
# ]

# trasposta = [
#     [1, 4],
#     [2, 5],
#     [3, 6]
# ]

# trasposizione (inversione righe, colonne di una matrice)

# matrice_trasposta = [[a, b] for a, b in zip(matrice[0], matrice[1])]

# print("Matrice originale:")
# for i in matrice:
#     print(i)

# print("Matrice Trasposta")
# for i in matrice_trasposta:
#     print(i)

# lista_unita = [[a, b] for a, b in zip(matrice[0], matrice_trasposta[0])]
# print(lista_unita)

# quello che accade è che le due liste vengono unite solo fin quando
# risulta esserci una corrispondenza in termini di numero elementi tra le due liste

# ------------------------

# lista = [1, 2, 3, 4]

# coppie_consecutive = [(a, b) for a, b in zip(lista, lista[1:])]
# print(coppie_consecutive)

# # funzione zip utilizzata al contrario tramite l'aggiunta di "*" 
# # prima della lista che si vuole unzippare
# unzip, unzip1 = list(zip(*coppie_consecutive))
# print(unzip)
# print(unzip1)


# Esercizio 7.5 - Map Base

# numeri = [1, 2, 3, 4, 5]

# def pew(x):
#     return x ** 2

# quadrati = list(map(pow, numeri, [2]*len(numeri)))
# quadrati = list(map(pew, numeri))
# print(quadrati)

# -----------------------

# def converti(x):
#     return str(x)

# stringhe = list(map(converti, numeri))
# print(stringhe)

# funzione personalizzata applicata l'esercizio precedente


# Esercizio 7.6 - Map Avanzato

# def somma(a, b, c):
#     return a + b + c

# somma_liste = list(map(somma, [1, 2], [3, 4], [5, 6]))
# print(somma_liste)

# ------------------

# radice = list(map(lambda x: x ** 0.5, [9, 25, 64]))
# print(radice)

# -----------------

# def maiusc(x):
#     return x.upper()

# maiuscole = list(map(maiusc, ["hello", "world"]))
# print(maiuscole)

# --------------

# def incrementa(x):
#     return x + 5

# lista = [[1, 2, 5], [10, 12, 15]]
# lista_incrementata = []
# for i in lista:
#     lista_incrementata.append(list(map(incrementa, i)))

# print(lista_incrementata)


# Esercizio 7.7 - Filter Base

# numeri = range(1, 21)

# def pari(x):
#     if x % 2 == 0:
#         return True

# def dieci(x):
#     if x > 10:
#         return True
    
# def primo(x):
#     if x < 2:
#         return False
    
#     for i in range(2, x):
#         if x % i == 0:
#             return False
        
#     return True
    
# pari = list(filter(pari, numeri))
# print(pari)

# dieci = list(filter(dieci, numeri))
# print(dieci)

# primo = list(filter(primo, numeri))
# print(primo)


# Esercizio 7.8 - Filter Avanzato

# parole = ["python", "java", "c++", "javascript", "go", "rust"]

# def conta_len(x):
#     if len(x) > 3:
#         return True

# parole3 = list(filter(conta_len, parole))
# print(parole3)

# # --------------

# def iniziale(x):
#     if str(x).startswith("j"):
#         return True
    
# inizia = list(filter(iniziale, parole))
# print(inizia)

# # ---------------

# def presenza(x):
#     if "a" in x:
#         return True
    
# contiene = list(filter(presenza, parole))
# print(contiene)

# # -----------------

# def quattro(x):
#     if len(x) <= 10:
#         return True
    
# def trova_t(x):
#     if "t" in x:
#         return True
    
# t_quattro = list(filter(quattro, filter(trova_t, parole)))
# print(t_quattro)


# Esercizio 7.9 - Combinazioni

# studenti = [
#     {"nome": "Mario", "età": 22, "voto": 85},
#     {"nome": "Anna", "età": 21, "voto": 92},
#     {"nome": "Luigi", "età": 23, "voto": 78},
#     {"nome": "Sara", "età": 20, "voto": 95}
# ]

# for i, v in enumerate(studenti, 1):
#     voto = v["voto"]
#     if voto > 80:
#         print(f"{i}. {v['nome']} - {voto}")

# nomi = [i["nome"] for i in studenti]
# anni = [i["età"] for i in studenti]
# voti = [i["voto"] for i in studenti]

# maggiorenni = [(n, v) for n, a, v in zip(nomi, anni, voti) if a > 18]
# print(maggiorenni)

# ----------------

# def aumenta(x):
#     return x + (x * 10) / 100

# voti_aumentati = list(map(aumenta, voti))
# print(voti_aumentati)

# ----------------------

# def trova_nomi(x):
#     return True if x["voto"] > 90 else False
    
# def maiuscolo(x):
#     return x.upper()

# trovati = list(filter(trova_nomi, studenti))
# print(trovati)

# nomi_maiuscoli = list(map(maiuscolo, [i["nome"] for i in trovati]))
# print(nomi_maiuscoli)

# ---------------------

# ordina_voto = [i["voto"] for i in studenti]
# ordina_voto.sort(reverse=True)
# for i, v in enumerate(ordina_voto, 1):
#     print(f"{i}. {v}")


# Esercizio 7.10 - Casi Particolari

# a = [1, 2, 3]
# b = ['a', 'b']
# print(list(zip(a, b)))  # Cosa manca?

# essendo liste incongruenti in termini di lunghezza (conta elementi)
# la nuova lista avrà le tuple con le coppie abbinate 
# solo fin quando la lunghezza è uguale
# in questo caso il 3 viene 

# --------------------

# pairs = [(1, 'a'), (2, 'b'), (3, 'c')]
# numbers, letters = zip(*pairs)  # Unpacking

# stiamo creando due liste di elementi a cui assegnamo
# in una i primi elementi interi alle tuple
# nell'altra i secondi elementi
# abbiamo buildato una specie di zip() inversa

# ------------------

# map con None (Python 2 legacy, non funziona in Python 3)
# map(None, [1,2], ['a','b'])

# -------------

# print(list(filter(None, [0, 1, '', 'hello', [], [1]])))  

# in questo caso il None viene passato come funzione
# restituisce tutto cià che risulta True, effettua una specie di BOOLEAN

# ---------------

# d = {'a': 1, 'b': 2}
# for i, (k, v) in enumerate(d.items()):
#     print(i, k, v)

# possiamo applicare la funzione enumerate() anche ad un dict

# ------------------

# nums = [1, 2, 3, 4]
# for a, b in zip(nums, nums[1:]):
#     print(f"{a} -> {b}")  

# possiamo creare in questo modo una serie di valori consecutivi

# ---------------------

# def somma(x, y, z):
#     return x + y + z
# result = list(map(somma, [1,2], [10,20], [100,200]))

# la funzione map() può essere applicata anche a più argomenti
# in questo caso però la funzione usata deve prendere in input
# quel determinato quantitativo di elementi per poter essere eseguita



# ESERCIZI MISTI AVANZATI


# Esercizio 8.1 - Sistema Voti

# studenti = {
#     "Mario" : [4, 5, 6],
#     "Luca" : [7, 5, 8],
#     "Giulia" : [6, 3, 5],
#     "Alice" : [5, 4, 5]
# }

# medie = {nome : round(sum(voti) / len(voti), 2) for nome, voti in studenti.items()}
# print(medie)

# ---------

# ordina = sorted(medie.items(), key=lambda item : item[1], reverse=True)
# print(dict(ordina[:3]))

# sorted --> builtin di python che funziona su ogni iterabile
# in questo caso ho bisogno di ordinare per medie
# le medie sono i valori delle chiavi di un dizionario
# quindi itero su tutto il dict, dichiaro una funzione in line con lambda
# la assegno alla key di sorted (non key del dict)
# nella lambda specifico di prendere elemento in posizione 1 quindi il valore
# e ordina in reverse quindi decrescente
# infine tramite slicing prendo i primi 3 elementi della lista creatasi

# -------------

# def recuperare(x):
#     return x[1] < 6

# def nomi_recuperi(x):
#     return x[0]

# recuperi = list(filter(recuperare, medie.items()))
# insufficienti = list(map(nomi_recuperi, recuperi))

# for i in insufficienti:
#     print(f"{i} deve recuperare")


# Esercizio 8.2 - Analisi Testo

# from collections import Counter

# testo = """Python è un linguaggio di programmazione. 
#            Python è facile da imparare. 
#            Python è potente e versatile."""

# parole = testo.split()
# pulizia del testo da caratteri nascosti/indesiderati

# conteggi = Counter(parole)
# utilizzo della funzione Counter() del modulo collections
# restituisce un'assocazione della parola trova e il relativo conteggio

# lunghezze_parole = ([len(i) for i in conteggi])
# creazione lista con solo valori relativi al conteggio delle parole

# media_lunghezza_parole = sum(lunghezze_parole) / len(lunghezze_parole)
# sum() per avere somma degli elementi della lista
# len() per avere il numero di elementi nella lista
# alternativa: importare funzione mean() dal modulo numpy

# print(round(media_lunghezza_parole, 2))
# round() per arrotondare e ridurre i decimali del risultato di tipo float

# -------------

# frasi = testo.split(".")
# conta_frasi = 0
# for i in frasi:
#     if "Python" in i:
#         conta_frasi += 1
#         print(i)

# print("Le frasi che contengono la parola \"Python\" sono", conta_frasi)

# -------------

# parole = testo.replace(".", "").split()
# nuova_stringa = ""
# for i in parole:
#     if i not in nuova_stringa:
#         if i == "imparare":
#             nuova_stringa += f"{i}, "
#         elif i == parole[-1]:
#             nuova_stringa += f"{i}."
#         else:
#             nuova_stringa += f"{i} "
#     elif i == "e":
#         nuova_stringa += f"{i} "

# print(nuova_stringa)

# -----------------

# parole = testo.split()
# indice = {}
# for i, v in enumerate(parole):
#     if v in indice:
#         indice[v].append(i)
#     else:
#         indice[v] = [i]

# print(indice)


# Esercizio 8.3 - Gestione Inventario

# inventario = {
#     "mele": {"quantità": 50, "prezzo": 0.5},
#     "banane": {"quantità": 30, "prezzo": 0.3},
#     "arance": {"quantità": 0, "prezzo": 0.4}
# }

# ordini = [
#     {"prodotto": "mele", "quantità": 10},
#     {"prodotto": "banane", "quantità": 35},  # Non disponibile
#     {"prodotto": "pere", "quantità": 5}      # Non esiste
# ]

# for k, v in inventario.items():
#     if v["quantità"] > 0:
#         print(f"{k} disponibili {v["quantità"]}")
    
#     elif v["quantità"] == 0:
#         print(f"{k} prodotto esaurito.")

#     elif v["quantità"] < 10:
#         print(f"{k} in esaurimento... fare nuovo ordine.")

# ---------

# for i in ordini:
#     if i["prodotto"] not in inventario.keys():
#         print(f"{i["prodotto"]} non esiste nell'inventario.")
#     else:   
#         if i["quantità"] <= inventario[i["prodotto"]]["quantità"]:
#             inventario[i["prodotto"]]["quantità"] -= i["quantità"]
#             vendite = inventario[i["prodotto"]]["prezzo"] * i["quantità"]
#             print(f"{i["prodotto"]} acquistate")
#             print(f"Disponibilità {i["prodotto"]} aggiornata a {inventario[i["prodotto"]]["quantità"]}")
#             print(f"Totale vendite di {i["prodotto"]}:")
#             print(f"{i["quantità"]} {i["prodotto"]} vendute.")
#             print(f"Spesa totale: {vendite}")
#         else:
#             print(f"La quantità di {i["prodotto"]} richiesta non è disponibile.")


# Esercizio 8.4 - Matrice Operations

# matrice = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# trasposta = [[a, b, c] for a, b, c in zip(matrice[0], matrice[1], matrice[2])]

# for i in trasposta:
#     print(i)

# --------------

# def righe(x):
#     return sum(x)

# somma_righe = list(map(righe, matrice))
# print(somma_righe)

# ------------

# somma_colonne = list(map(righe, trasposta))
# print(somma_colonne)

# -----------

# diagonale = [matrice[0][0], matrice[1][1], matrice[2][2]]
# diagonale secondaria (?)

# -----------

# matrice_ruotata = [
#     [7, 4, 1],
#     [8, 5, 2],
#     [9, 6, 3]
# ]

# ruotata = [[c, b, a] for a, b, c in zip(matrice[0], matrice[1], matrice[2])]

# for i in ruotata:
#     print(i)

# il procedimento è quello di una trasposizione creando le liste in reverse

# --------------------

# massimo = max(list(map(max, matrice)))
# print(massimo)

# minimo = min(list(map(min, matrice)))
# print(minimo)

# applico la funzione max() a tutte le liste nella matrice con map()
# si crea una lista con list() di questi valori e con il max() esterno
# posso trovare il valore più alto tra i più alti delle singole liste 

# ---------------------

# appiattisci (?)


# Esercizio 8.5 - Parser CSV Semplice

# csv_data = """nome,eta,citta,salario
# Mario,25,Roma,30000
# Anna,30,Milano,45000
# Luigi,22,Napoli,28000
# Sara,28,Torino,38000"""

# data = csv_data.split("\n")

# chiavi = data[0].split(",")

# dizionari = []

# for i in data[1:]:
#     valori = i.split(",")
#     diz = {chiave : valore for chiave, valore in zip(chiavi, valori)}
#     dizionari.append(diz)

# for i in dizionari:
#     print(i)

# -------------

# eta_25 = list(filter(lambda x : int(x["età"]) > 25, dizionari))
# for i in eta_25:
#     print(i)

# --------------

# dizionari.sort(key=lambda x: int(x["salario"]))
# for i in dizionari:
#     print(i)

# ---------------

# salari = [int(i["salario"]) for i in dizionari]
# salario_medio = round(sum(salari) / len(salari), 2)
# salario_massimo = max(salari)
# salario_minimo = min(salari)
# print(salario_medio)
# print(salario_massimo)
# print(salario_minimo)

# -------------

# from json import dumps

# stringa_json = dumps(dizionari, indent=4)
# print(stringa_json)


# PARTE 9: CASI SUPER STRANI


# Esercizio 9.1 - Python Quirks

# a = 256
# b = 256
# print(a is b)  # ?
# # il risultato atteso è True, poichè a e b coincidono

# a = 257
# b = 257
# print(a is b)  # ?
# # il risultato atteso è True, poichè a e b coincidono

# ---------------

# def f(x, lista=[]):
#     lista.append(x)
#     return lista

# print(f(1))
# print(f(2))  # ?

# la funzione viene definita con un parametro x 
# e con un secondo parametro, una lista vuota di default
# dopo il primo utilizzo il parametro di default non rimane tale
# si ha quindi il primo output [1] e il secondo [1, 2]

# --------------

# funcs = []
# for i in range(3):
#     funcs.append(lambda: i)

# print(funcs)
# for f in funcs:
#     print(f())  # ?

# lista vuota funcs
# aggiunta elementi del tipo lambda : i dove i = 0, 1, 2
# lambda per tenere il valore va scritto lambda i = i : i
# con questa sintassi dell'esempio il valore trattenuto è l'ultimo inserito
# quindi tutte le funzioni lambda in funcs quando richiamate stamperanno 2

# ------------------------

# a = [1, 2]
# b = a
# a = a + [3]
# print(b)  # ?
# qui sto creando una nuova variabile a
# assegnandogli la lista di a + [3]
# quindi b prende il valore della prima a 

# a = [1, 2]
# b = a
# a += [3]
# print(b)  # ?
# qui sto incrementando una variabile ma senza cambiarla
# quindi b verrà aggiornata a sua volta



# Esercizio 9.2 - Type Coercion

# print(True + True)  # ?
# print(False - True)  # ?
# print(True * 50)  # ?
# True e False corrispondono a dei valori interi binari 1 0

# print("5" * 3)  # ?
# print(3 * "5")  # ?
# ripeto la stringa 3 volte, output atteso --> "555"

# print([] + [])  # ?
# sommando due liste vuote, si ottiene una lista singola vuota

# print({} or "default")  # ?
# print("" or "default")  # ?
# creando elementi impostando una condizione qualora fossero vuoti
# output atteso --> "default"

# print(all([]))  # ?
# sto esaminando tutti gli elementi di una lista vuota 
# True per convenzione

# print(any([]))  # ?
# cerco qualcosa di specifico ma essendo vuoto risulta False

# print(bool("False"))  # ?
# bool di una stringa con elementi --> True

# print(bool(" "))  # ?
# bool di una stringa con elementi (lo spazio conta come elemento)
# output atteso --> True


# Esercizio 9.3 - Scope Traps

# x = 10
# def func():
#     print(x)  # UnboundLocalError!
#     x = 20

# x è dichiarata fuori dalla funzione
# internamente si prova a stampare ma non esiste al momento del print
# la si dichiara successivamente ma non viene considerata
# si può dichiarare internamente prima del print

# ------------

# total = 0
# def add(val):
#     total += val  # UnboundLocalError!
#     return total

# stessa spiegazione di prima
# inoltre la funzione se non richiamata non può eseguire il codice da sola

# ------------

# for i in range(5):
#     pass
# print(i)  # i esiste qui!

# se pur la variabile i esiste salva solo l'ultimo elemento noto 
# da 0, 1, 2, 3, 4 --> ultimo elemento corrisponde a 4
# se si vuole mostrare il range completo dell'iterazione
# bisogna spostare il print internamente al for indentandolo 
# togliere il pass per eseguire istruzioni

# ------------

# [x for x in range(5)]
# print(x)  # x esiste? 

# no, è dichiarata e usata nel for interno alla list comprehension
# non è accessibile esternamente

# --------------


# Esercizio 9.4 - Dictionary Madness

# d = {}
# d[(1, 2)] = "ok"  # Tuple ok
# # d[[1, 2]] = "no"  # List no!
# d[frozenset([1, 2])] = "ok"  # Frozenset ok

# per una corretta creazione delle chiavi di un dict
# occorre avere un elemento IMMUTABILE
# ecco perchè tupla e frozenset si, e la lista ad esempio no.

# ---------------

# d = {i: i**2 for i in range(5)}
# for k in list(d.keys()):  # Perché list()?
#     if k % 2 == 0:
#         del d[k]

# senza il list stiamo modificando la grandezza di un elemento
# all'interno di un ciclo, darà errore
# con list() si crea una corrispondenza dell'elemento usato
# quindi non stiamo alterando la dimensione dell'iterabile
# ma solo dell'elemento originale

# ------------

# d = {}
# d.setdefault('key', []).append(1)
# d.setdefault('key', []).append(2)
# print(d)  # ?

# output atteso --> {key : [1 ,2]}
# setdefault() non restituisce errore se la chiave non è presente nel dict
# crea una chiave per una corrispondenza
# e assegna di default una lista vuota in questo caso
# successivamente viene riempita con gli elementi 1, 2

# ------------------

# d1 = {'a': 1, 'b': 2}
# d2 = {'b': 3, 'c': 4}
# # Python 3.5+
# d3 = {**d1, **d2}
# # Python 3.9+
# d4 = d1 | d2

# metodi alternativi per unificare i dict 
# fare attenzione alle versioni di Python


# Esercizio 9.5 - List Mutation Chaos

# a = [1, 2, 3, 4, 5]
# a[1:4] = [20]  # Sostituisce 3 elementi con 1
# print(a)  # ?

# in questo modo non vengono modificati i valori 
# nel range indicato dallo slicing
# ma vengono rimossi e sostituiti

# ------------------

# a = list(range(10))
# a[::2] = [99] * 5  # Sostituisce elementi a indici pari
# print(a)  # ?

# lo slicing ha 3 elementi, inizio fine e progressione
# : (tutto), : (tutto), 2 (progressione + 2)
# verranno sostituiti gli elementi con indici pari 

# ---------------------

# matrix = [[0] * 3] * 3
# matrix[0][0] = 1
# print(matrix)  # Tutte le righe cambiate!

# si è creata una matrice 3x3 composta da 0
# si accede alle coordinate dell'elemento i prima posizione
# da dichiarazione la matrice è composta da 3 liste uguali 
# assegnando un nuovo valore ad una cella viene replicato

# ---------------

# a = [1, 2, 3]
# b = a
# a += [4]  # In-place
# print(b)  # ?

# output atteso --> [1, 2, 3, 4]
# b prende il valore di a
# prima di essere stampato a viene incrementata
# quindi anche b in output prende la modifica

# ----------------

# a = [1, 2, 3]
# b = a
# a = a + [4]  # New object
# print(b)  # ?

# output atteso --> [1, 2, 3]
# similmente all'esercizio di prima
# però stavolta si sta creando una nuova variabile a
# gli viene assegnato tutto a + [4] 
# ma b ha preso la prima a
# differentemente a prima si ha una nuova variabile e non la stessa modificata

# -----------------

# a = [3, 1, 2]
# b = sorted(a)  # Returns new
# c = a.sort()   # Returns None!
# print(a, b, c)  # ?

# sorted() restituisce una lista ordinata
# .sort() è un metodo delle liste che agisce su di esse 
# ma non restituisce nulla ecco il motivo del None in ouput



# PARTE 10: SFIDE


# Sfida 1 - One-Liners

# multiplo 3 = fizz
# multiplo 5 = buzz
# multiplo 3 e 5 = fizzbuzz

# fizzbuzz = ["FizzBuzz" if i % 15 == 0 else "Fizz" if i % 3 == 0 else "Buzz" if i % 5 == 0 else i for i in range(1, 101)]
# print(fizzbuzz)

# ----------------

# palindromo = lambda x : x.lower().replace(" ", "") == x.lower().replace(" ", "")[::-1]
# print(palindromo("otto"))
# print(palindromo("ciao"))

# -----------------

# fibo = lambda n, start = [0, 1] : None if n < 2 else start + [start.append(start[-1] + start[-2]) or start[-1] for _ in range(2, n)]
# print(fibo(10))

# lambda dichiara : istruzioni
# .append() restituisce None
# con or start[-1] ci assicuriamo che l'ultimo valore inserito
# sia letto e incrementato a sua volta

# ------------------

# primi = lambda : [i for i in range(2, 101) if not any(i % j == 0 for j in range(2, i))]
# print(primi())

# list comprehension per aggiungere tutti i numeri da 2 a 100 
# se il modulo del numero in questione diviso (un ciclo di numeri)
# che va da 2 al numero in questione sia almeno una volta 0
# allora non è primo, in caso contrario si aggiunge l'elemento alla lista