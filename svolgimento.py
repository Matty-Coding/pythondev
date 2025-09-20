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
# creazione lista, con dentro una lista con 3 elementi (inizializzati a 0) moltiplicato 3 volte (quindi 3 liste del tipo precedentemente detto)

# a[0][0] = 1
# sto accedendo alla lista generale e poi nidificando al primo elemento del singolo assegnando valore 1

# print(a)
# si verifica in tutte le liste poichè accedendo alla lista, in-line è specificato di creare 3 liste uguali

# --------------------

# numeri = [1, 2, 3, 4, 5]
# for i in range(len(numeri)):
#     if numeri[i] % 2 == 0:
#         numeri.remove(numeri[i])  

# eseguire operazioni sugli indici all'interno di un ciclo (specie rimozione/aggiunta) comporta un'alterazione degli stessi, si finisce in un errore di indicizzazione

# ------------------------

# def aggiungi(item, lista=[]):
#     lista.append(item)
#     return lista

# print(aggiungi(1))
# print(aggiungi(2))  

# richiamando la funzione una seconda volta la lista non sarà più vuota ma corrisponderà a [1], pertanto passando come nuovo parametro l'elemento di valore 2 il risultato in output sarà [1, 2]

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
# # il secondo parametro nella funzione get per accedere ai valori di un dict imposta tale parametro come valore di default qualora la ricerca restituisse None
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
# # la chiave presente nel dict che viene implementato sostituirà il suo valore rimpiazzando quello presente alla stessa chiave nel dict primario

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

lista_tuple = [("a", 1), ("b", 2), ("a", 4)]
diz4 = {i[0] : [k[1] for k in lista_tuple if k[0] == i[0]] for i in lista_tuple}
print(diz4)


# Esercizio 5.5 - Dizionari Annidati