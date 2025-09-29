# Scrivi un decoratore che stampa 
# Inizio prima di una funzione
# Fine dopo la funzione

# def decoratore1(funzione):
#     def wrapper(*args, **kwargs):
#         print("Inizio")
#         funzione(*args, **kwargs)
#         print("Fine")
#     return wrapper

# @decoratore1
# def funzione():
#     print("Sono la parte centrale!")

# funzione()


# ------------


# Crea un decoratore che conta quante volte 
# viene richiamata una funzione
# def conta_volte(funzione):
#     conta = 0
#     def wrapper(*args, **kwargs):
#         nonlocal conta
#         funzione(*args, **kwargs)
#         conta += 1
#         if conta == 1:
#             print(f"Hai richiamato la funzione per la {conta} volta")
#         else:
#             print(f"Hai richiamato la funzione {conta} volte")
#     return wrapper

# @conta_volte
# def prova():
#     pass

# prova()
# prova()
# prova()
# prova()


# -----------


# Scrivi un decoratore che stampa il tempo
# di esecuzione di una funzione
# import time

# def timing(funzione):
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         funzione(*args, **kwargs)
#         end = time.time()
#         print(f"La funzione ha impiegato {round(end - start, 2)} secondi.")
#     return wrapper

# @timing
# def provaa():
#     for _ in range(1, 1000000):
#         pass

# provaa()


# -----------


# Scrivi un decoratore che prende un parametro n
# esegue la funzione n volte
# def ripeti(n):
#     def decora(f):
#         def wrapper():
#             for _ in range(n):
#                 f()
#         return wrapper
#     return decora

# @ripeti(3)
# def funzione():
#     print("ripeto la funzione")

# funzione()


# ---------


# Scrivi un decoratore che esegue la funzione
# solo se l'utente ha un ruolo di admin
# altrimenti stampa messaggio di errore
# def check_admin(f):
#     def wrapper():
#         if utente.get("ruolo") == "admin":
#             f()
#         else:
#             print(f"Errore di permessi, non sei admin")
#     return wrapper


# @check_admin
# def esegui():
#     print("Sto eseguendo il codice, admin verificato")

# utente = {"id" : 7, "ruolo" : "admin"}
# esegui()


# -------------------


# Scrivi un decoratore che memorizza i risultati
# di una funzione costosa in una cache
def cached(f):
    cache = []
    def wrapper(*args):
        if args in cache:
            print("\nUtilizzando la cache...")
            print("\n\nCache secondaria -->", cache)
            return cache
        
        print("\nCaching dei dati in corso...")
        cache.append(f())

    return wrapper

@cached
def fun():
    tot = 0
    for n in range(10000000000):
        tot += n
        
    return tot

import time
start1 = time.time()
fun()
print(f"La funzione chiamata la prima volta impiega --> {round(time.time()-start1, 2)} secondi.")

start2 = time.time()
fun()
print(f"La funzione chiamata la seconda volta impiega --> {round(time.time()-start2, 2)} secondi.")
