# # ANALIZZATORE TESTO
# # tot parole, tot vocali, 5 parole lunghe, diz {conta : [parole]}, palindrome

# testo = """Python è un linguaggio fantastico per imparare 
#          la programmazione. È versatile e potente."""

# # creo lista parole e con la sua len ho il totale
# lista_parole = testo.replace(".", "").strip().split()
# print(f"Il testo ha {len(lista_parole)} parole.")

# # conta vocali (accentate escluse)
# # crea lista [[parola, len[parola]]]
# vocali = ("a", "e", "i", "o", "u")
# conta_vocali = 0
# parole_lettere = []
# for parola in lista_parole:
#     parole_lettere.append([parola, len(parola)])
#     for lettera in parola:
#         if lettera.lower() in vocali:
#             conta_vocali += 1
# else:
#     print(f"Il testo ha {conta_vocali} vocali.")

# # ordinamento lista [[parola, lettere della parola]] + top 5
# ordina_parole = sorted(parole_lettere, key=lambda x: x[1], reverse=True)[:5]
# for i, v in enumerate(ordina_parole, start=1):
#     print(f"\n{i}. {v[0].upper()} con {v[1]} lettere.")

# # creazione dict {conta_lettere : [lista parole]}
# diz_testo = {}
# for parola, lettere in parole_lettere:
#     if lettere not in list(diz_testo.keys()):
#         diz_testo[lettere] = [parola]
#     else:
#         diz_testo[lettere] += [parola]

# for k, v in diz_testo.items():
#     print(f"Conta lettere: {k} - Lista parole: {v}")

# # trova parole palindrome se presenti
# palindrome = [i[0] for i in parole_lettere if i[0].lower() == i[0][::-1].lower() and len(i[0]) > 1]
# print(f"Lista parole palindrome --> {palindrome}")



# ---------------------------------



# CARRELLO DELLA SPESA
# sconto 10% se totale maggiore di 50
# sconto 15% se totale maggiore di 100
# spedizione gratuita sopra i 30 (altrimenti 5)
# calcola totale

# catalogo = {
#     # "pasta":1.20,
#     "pasta" : 26,
#     "pomodoro": 2.50,
#     "mozzarella": 4.80,
#     "basilico": 1.00,
#     "olio": 8.50,
#     "pane": 1.50,
#     "acqua": 0.50
# }

# carrello = [
#     {"prodotto": "pasta", "quantita": 2}
#     # {"prodotto": "pomodoro", "quantita": 1}
#     # {"prodotto": "mozzarella", "quantita": 2},
#     # {"prodotto": "acqua", "quantita": 6}
# ]

# # calcolo del totale
# totale = sum([q["quantita"] * catalogo[q["prodotto"]] for q in carrello])

# # verifichiamo il totale per assegnare:
# # costo spedizione e sconti condizionali
# if totale < 30:
#     totale += 5

# if totale > 100:
#     totale -= (15 * totale) / 100
# elif totale > 50:
#     totale -= (10 * totale) / 100

# print(f"Totale del carrello: {totale}€.")



# -------------------------



# VALIDATORE PASSWORD
# lunghezza minima 8 caratteri
# almeno una maiuscola
# almeno una minuscola
# almeno un numero
# almeno un carattere speciale
# Ritorna: 
# (True, "Password valida")
# (False, [lista_errori])
# Bonus: calcola un punteggio di forza (debole/media/forte)

# Test
# # passwords = ["abc123", "Password1!", "TUTTO_MAIUSCOLO", "Sicura123!"]
# passwords = ["Abcdef#45", "ForzaM3dia!", "@Str0ngPW!!", "ciao123"]

# # funzione di controllo requisiti password
# def valida_password(password):
#     tupla_speciali = ("!", "@", "#", "$", "%", "^", "&", "*")
#     lista_errori = []
#     punteggio = 0
    
#     # check lunghezza
#     if len(password) > 8:
#         lunghezza = True
#         punteggio += 1
#     else:
#         lunghezza = False
#         lista_errori.append("lunghezza")
    
#     # inizializzazione contatori
#     maiuscole = 0
#     minuscole = 0
#     speciali = 0
#     numeri = 0

#     for carattere in password:
#         # check maiuscole
#         if carattere.isupper():
#             maiuscole += 1
#             punteggio += 1
#         # check minuscole
#         elif carattere.islower():
#             minuscole += 1
#             punteggio += 1
#         # check speciali
#         elif carattere in tupla_speciali:
#             speciali += 1
#             punteggio += 2
#         # check numeri
#         elif carattere.isdigit():
#             numeri += 1
#             punteggio += 1
        
#     if maiuscole == 0:
#         lista_errori.append("maiuscole") 
#     if minuscole == 0:
#         lista_errori.append("minuscole") 
#     if numeri == 0:
#         lista_errori.append("numeri") 
#     if speciali == 0:
#         lista_errori.append("speciali") 

#     if maiuscole != 0 and minuscole != 0 and speciali != 0 and numeri != 0 and lunghezza is True:
#         return (True, "Password valida", punteggio)
    
#     return (False, lista_errori)

# for i in passwords:
#     print("\n-->", i)
#     validazione = valida_password(i)
#     if validazione[0] is True:
#         if validazione[2] == 11:
#             print(validazione[1], "--> Debole 🟠")
#         elif 12 <= validazione[2] < 15:
#             print(validazione[1] ,"--> Mediocre 🟡")
#         elif validazione[2] >= 15:
#             print(validazione[1], "--> Forte 🟢")
#     else:
#         print("❌ Password non valida i seguenti criteri non sono rispettati -->", validazione[1])



# --------------------------



# AGENDA APPUNTAMENTI
# data in stringa del tipo YYYY--MM-DD
# ora in stringa del tipo HH:MM
# descrizioneliberi
# durata in minuti
# funzionalità da implementare:
# aggiungi appuntamento (controlla conflitti)
# cancella appuntamento
# mostra appuntamenti del giorno
# trova posto libero di x durata minima

# agenda = {
#     "2024-01-15": [
#         {"ora": "09:00", "desc": "Riunione", "durata": 60},
#         {"ora": "14:30", "desc": "Call cliente", "durata": 30}
#     ]
# }

# # creazione funzione di visualizzazione dati agenda
# def visualizza_agenda():
#     for index, (k_data, v_ora) in enumerate(agenda.items(), start=1):
#         print(f"{index} - {k_data}")
#         for i in v_ora:
#             print("    ", i)

# # creazione funzione che prende i dati dell'appuntamento
# def dati_appuntamento():
#     giorno = input("Inserisci numero del giorno (2 cifre) --> ")
#     mese = input("Inserisci numero del mese (2 cifre) --> ")
#     anno = input("Inserisci numero del anno (4 cifre) --> ")

#     return f"{anno}-{mese}-{giorno}"
    
# def aggiungi_appuntamento(data):
#     if data in agenda.keys():
#         print("La data inserita ha già degli appuntamenti.")
#         for k, v in agenda.items():
#             print(k, "\n    ", v)

#         orario = input("Indica l'orario (4 cifre con : separatori) --> ")

#     else:
#         print("La data inserita non ha appuntamenti prenotati, tutti i posti sono disponibili.")
#         orario = input("Indica l'orario (4 cifre con : separatori) --> ")

#     scelta_durata = input("Indica la durata dell'appuntamento: [1] - 60min oppure [2] - 30min --> ")
#     if scelta_durata == "1":
#         durata = 60
#     else:
#         durata = 30

#     descrizione = input("Scrivi una breve descrizione dell'appuntamento: ")
       
#     if data in agenda:
#         for appuntamento in agenda[data]:
#             if appuntamento["ora"] == orario:
#                 print("Esiste già un appuntamento a quell'orario.")
                
#                 return agenda
    
#     # aggiungo dati all'agenda, segnalando eventuali conflitti di orario
#     if data not in list(agenda.keys()):
#         agenda[data] = [{"ora" : orario, "desc" : descrizione, "durata" : durata}]
#     else:
#         agenda[data] += [{"ora" : orario, "desc" : descrizione, "durata" : durata}]

#     return agenda

# print("Inserisci dati per prenotare appuntamento:")
# aggiungi_appuntamento(dati_appuntamento())
# visualizza_agenda()

# def cancella_appuntamento():
#     scelta_data = input("Inserisci indice corrispondente alla data contenente l'appuntamento che si vuole eliminare: ")
#     for i, (k, v) in enumerate(agenda.items(), start=1):
#         if str(i) == scelta_data:
#             for indice, appuntamento in enumerate(v, start=1):
#                 print(indice, "-", appuntamento)
            
#             data_scelta = k
#             break

#     scelta_appuntamento = input("\nInserisci indice corrispondente all'appuntamento che vuoi eliminare: ")
#     for i, (k, v) in enumerate(agenda.items(), start=1):
#         if k == data_scelta:
#             v.pop(int(scelta_appuntamento) - 1)
#             break

#     return agenda

# visualizza_agenda()
# cancella_appuntamento()
# visualizza_agenda()



# --------------



# CONVERTITORE UNITA DI MISURA
# lunghezza (metri, piedi, pollici)
# peso (kg, libbre, once)
# temperatura (Celsius, Fahrenheit, Kelvin)
# gestisci input non validi


# conversioni = {
#     "lunghezza": {
#         "metri_piedi": 3.28084,
#         "piedi_metri": 0.3048,
#         "metri_pollici": 39.3700787,
#         "pollici_metri": 0.0254,
#         "piedi_pollici": 12.0,
#         "pollici_piedi": 1/12.0
#     },
#     "peso": {
#         "kg_libbre": 2.20462262185,
#         "libbre_kg": 0.45359237,
#         "once_kg": 0.02834952,
#         "kg_once": 1/0.02834952,
#         "once_libbre": 1/16.0,
#         "libbre_once": 16.0
#     },
#     "temperatura": {
#         "celsius_fahrenheit": lambda x: (x * 9/5) + 32,
#         "fahrenheit_celsius": lambda x: (x - 32) * 5/9,
#         "celsius_kelvin": lambda x: x + 273.15,
#         "kelvin_celsius": lambda x: x - 273.15,
#         "fahrenheit_kelvin": lambda x: (x - 32) * 5/9 + 273.15, 
#         "kelvin_fahrenheit": lambda x: (x - 273.15) * 9/5 + 32 
#     }
# }


# # accede al valore scelto per la conversione
# # effettua il calcolo e ritorna il risultato
# def converti(valore, tipo_unita, unita1, unita2):
#     # formatto il tipo di conversione 
#     tipo_conversione = "_".join([unita1, unita2]).lower()

#     # trovo il valore di conversione 
#     valore_di_conversione = conversioni[tipo_unita][tipo_conversione]

#     # effettuo il calcolo tramite la funzione specifica della conversione
#     if tipo_unita == "temperatura":
#         return valore_di_conversione(valore)
    
#     # effettuo il calcolo e ritorno il valore 
#     return valore * valore_di_conversione


# def main():
#     print("\n   -----  CONVERTITORE DI UNITA  -----\n")

#     while True:
#         for i, v in enumerate(conversioni.keys(), start=1):
#             print(f"[{i}] - {v.upper()}")

#         scelta_tipo_conversione = input("Inserisci l'indice corrispondente al tipo di conversione che vuoi fare: ").strip()
#         indici_conversioni = ("1", "2", "3")
#         if scelta_tipo_conversione not in indici_conversioni:
#             print("Scelta non disponibile, riprovare.")
#             continue
        
#         valore = input("Inserisci il valore che vuoi convertire: ").strip()
#         try:
#             if float(valore):
#                 valore = float(valore)
                
#         except ValueError as e:
#             print(f"Il valore inserito non è valido, riprovare.\nTipo di errore --> {e}") 
#             continue
        
#         tipo_conversione_scelta = list(conversioni.keys())[int(scelta_tipo_conversione) - 1]
#         tupla_conversioni = tuple((k.split("_")[0], k.split("_")[1]) for k in conversioni[tipo_conversione_scelta].keys())
#         for i, v in enumerate(tupla_conversioni, start=1):
#             print(f"[{i}]  {v[0].capitalize()} --> {v[1].capitalize()}")

#         indici_ultima_scelta = ("1", "2", "3", "4", "5", "6")
#         scelta_unita_conversione = input("Inserisci indice corrispondente alla conversione desiderata: ").strip()

#         if scelta_unita_conversione not in indici_ultima_scelta:
#             print("Scelta non disponibile, riprovare.")
#             continue

#         unita1, unita2 = tupla_conversioni[int(scelta_unita_conversione) - 1]
        
#         # richiamo la funzione per calcolare la conversione 
#         risultato_conversione = converti(valore, tipo_conversione_scelta, unita1, unita2)
#         print(f"Risultato conversione: {valore} {unita1.capitalize()} --> {risultato_conversione} {unita2.capitalize()}.")
#         break

# main()
