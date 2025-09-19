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
# lista_vuota_1 = list("")

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

lista = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

primo = lista[0]
ultimo = lista[-1]