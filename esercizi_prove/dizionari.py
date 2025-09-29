# diz_1 = {
#     "nome" : "mario",
#     "cognome" : "rossi",
#     "anni" : 27
#     }

# diz_2 = {
#     "comune" : "Roma",
#     "codice postale" : "00000"
# }


# for k, v in diz_1.items():
#     print(f"{k} - {v}")

# for k, v in diz_2.items():
#     print(f"{k} - {v}")

# diz_1.update(diz_2)


# print("dict unificato")
# for k, v in diz_1.items():
#     print(f"{k} - {v}")


# ------------------------------
# ------------------------------
# ------------------------------
# ------------------------------

# somma tutti gli elementi di un dizionario

# diz = {
#     "ford" : 1,
#     "ferrari" : 4,
#     "fiat" : 5
# }

# valori = diz.values()
# print(sum(valori))


# moltiplica tutti gli elementi di un dizionario
# valori = diz.values()
# prodotto = 1
# for i in valori:
#     prodotto *= i

# print("Il prodotto dei valori nel dizionario corrisponde a --> ", prodotto)

# rimuovi una chiave dal dizionario

# diz.pop("ford")
# print(diz)



# estrai il valore cyber
scuola = {
    "classe": {
        "studente": {
            "nome": "mario",
            "materie": {
                "it": 70,
                "cyber": 80
                }
            }
        }
    }

classe = scuola["classe"]["studente"]["materie"]["cyber"]
# studente = classe["studente"]
print(classe)


cyber = (
    scuola.get("classe")
    .get("studente")
    .get("materie")
    .get("cyber")
)

print(cyber)

