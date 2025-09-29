import os, sys, shutil

# dato un path di input, verifica se è un file o una cartella

# path_utente = input("Inserisci path da analizzare: \n--> ").strip()

# def analizza_path(path):
#     if os.path.isfile(path):
#         print("Il path inserito è un file.")
    
#     elif os.path.isdir(path):
#         print("Il path inserito è una cartella.")

#     else:
#         print("Path non trovato.")

# analizza_path(path_utente)


# ---------------


# crea cartella backup in cui copi tutti i file .txt presenti

# try:
#     path_corrente = os.getcwd()
#     path_new_file = os.path.join(path_corrente, "backup")
#     if not os.path.exists(path_new_file):
#         backup_folder = os.makedirs("backup")
#         print(f"Cartella backup creata in {path_corrente}")
#     else:
#         print("Cartella non creata, esiste già.")

#     contenuto = os.listdir(path_corrente)

#     for i in contenuto:
#         if i.endswith(".txt"):
#             shutil.copy(os.path.join(path_corrente, f"{i}"), path_new_file)
#             print(f"{i} spostato in {path_new_file}")

# except Exception as e:
#     print("Errore -->", e)


# ---------------


# mostra tutti i file in una cartella con la relativa dimensione in byte

# cartella_corrente = os.getcwd()
# contenuto = os.listdir(cartella_corrente)

# for i in contenuto:
#     print(f"{os.path.getsize(i)} byte --> {i}")


# -------------


# prendi input da linea di comando e stampa somma
# a = sys.argv[1]
# b = sys.argv[2]

# print(int(a) + int(b))
    

# --------------


# mostra versione python
# piattaforma
# percorso moduli importati

# print(f"Piattaforma --> {sys.platform}")
# print(f"Versione --> {sys.version}")
# print(f"Percorso moduli importati --> {sys.path}")


# --------------


# prendi file come argomento lo legge riga per riga
# stampa su stdout

# input_file = sys.argv[1]
# with open(input_file, "r") as f:
#     for i in f:
#         sys.stdout.write(i)


# --------------


# ricevi da linea di comando un path
# se è un file stampa dimensione
# se è una cartella elenca i file
# usa decoratore per loggare ogni chiamata alla funzione (timestamp)

# import datetime

# def log_function(func):
#     logger = {}
#     def wrapper(*args, **kwargs):
#         timestamp = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
#         logger["timestamp"] = timestamp
#         print(f"Log: {logger}")
#         return func(*args, **kwargs)
#     return wrapper

# @log_function
# def analizza_path(path):
#     if os.path.isfile(path):
#         print(f"file di dimensione --> {os.path.getsize(path)} byte.")
    
#     elif os.path.isdir(path):
#         print("Cartella con i seguenti file:")
#         for i in os.listdir(path):
#             print(i)

#     else:
#         print("Path non trovato.")

# path_utente = sys.argv[1]
# analizza_path(path_utente)


