# funzione che calcola una divisione e in caso di errore gestirli correttamente. 
# richiama la funzione due volte per verificare l'output 


# def divisione(a, b):
#     # validazione elementi
#     try:
#         numeratore = float(a)
#         denominatore = float(b)
#         quoziente = numeratore / denominatore
#         return round(quoziente, 3)

#     except ZeroDivisionError as e:
#         return e
    
# print(divisione(5.7, 1.2))

# -----------------------------------------------
# funzione che moltiplica ogni elemento di una lista e calcola la risultante. se il risultato è < 0 gestire eccezione.
# richiama la funzione per verificare

# def moltiplica_lista(lista):
#     prodotto = 1
#     for i in lista:
#         prodotto *= i
    
#     if prodotto < 0:
#         raise ValueError ("Il prodotto è negativo!")
    
#     return round(prodotto, 3)

# valori = [3, -5.4, 2] # genera errore
# # valori = [3, 5.4, 2] 
# prodotto = moltiplica_lista(lista=valori)
# print(f"Il prodotto della lista corrisponde a --> {prodotto}")

# --------------------------------------------
# funzione che calcola somma valori in una lista
# solleva eccezione --> somma > 50
# aggiungi finally per fare somma / 2


# def somma_valori_lista(lista):
#     try:
#         somma = sum(lista)
#         if somma >= 50:
#             raise ValueError ("La somma è maggiore di 50!")

#     finally:
#         print("Calcolo la metà della somma...")
#     return somma / 2


# valori = [10, 31, 53] # genera errore 
# # valori = [10, 31, 2]  

# half_sum = somma_valori_lista(lista=valori)
# print(f"La metà della somma corrisponde a --> {half_sum}")


