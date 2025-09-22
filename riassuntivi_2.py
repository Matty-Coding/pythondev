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
