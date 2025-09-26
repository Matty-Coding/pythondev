import re

# VALIDAZIONE CODICE FISCALE 
# XXXXXXnnXnnXnnnX
def codice_fiscale(stringa):
    pattern = r"[A-Z]{6}\d{2}[A-Z]\d{2}[A-Z]\d{3}[A-Z]"
    return bool(re.match(pattern, stringa))

# print(codice_fiscale("QWERTY22K56U978S"))  # True
# print(codice_fiscale("Q3ERTY22K56U978S"))  # False

# -----------

# ESTRAZIONE PREZZI
# estrai tutti i prezzi da un testo 
# formato prezzo --> €XX,XX o €XXX,XX
def estrai_prezzo(testo):
    pattern = r"€\d{2,3},\d{2}"
    return re.findall(pattern, testo)

# print(estrai_prezzo("testo con prezzi €34,23."))
# print(estrai_prezzo("oggi ho speso €433,99 la mattina e €54,76 la sera."))

# ------------

# TROVA CIFRE SINGOLE
# estrai da un testo tutte le cifre singole
def estrai_cifre_singole(testo):
    pattern = r" \d{1} "
    return re.findall(pattern, testo)

# print(estrai_cifre_singole("Ho 5 gatti, 3 cani e 12 pesci"))


# ---------

# VALIDAZIONE CODICE POSTALE ITALIANO
# nnnnn
def valida_codice_postale(stringa):
    pattern = r"^\d{5}$"
    return bool(re.match(pattern, str(stringa)))

# print(valida_codice_postale("34256"))
# print(valida_codice_postale(32155))
# print(valida_codice_postale(3215))

# ------------

# SOSTITUZIONE SPAZI MULTIPLI
# sostituisci serie di spazi multipli con uno spazio singolo
def sostituisci_spazi(testo):
    pattern = r"\s{2,}"
    return re.sub(pattern, " ", testo)

# print(sostituisci_spazi("ciao   sono luca  spazio."))

# -----------

# TROVA PAROLE CON INIZIALE MAIUSCOLA
# estrai tutte le parole che iniziano con una maiuscola
def trova_maiuscole(stringa):
    pattern = r"[A-Z]\w+"
    return re.findall(pattern, stringa)

# print(trova_maiuscole("Mario e Luigi vivono a Roma con Anna"))

# --------

# VALIDAZIONE NUMERO DI TELEFONO ITALIANO
# 02-12345678
# +39 339 1234567
# 339 1234567

def validazione_numero(telefono: str) -> str:
    pattern = [
        r"0\d{1}-\d{8}",
        r"\+39 3\d{2} \d{7}",
        r"3\d{2} \d{7}"
        ]
    
    for i in pattern:
        valido = bool(re.match(i, telefono))
        if valido is True:
            return valido
        
    return valido

# print(validazione_numero(1234567890))
# print(validazione_numero("01-12345678"))
# print(validazione_numero("39 339 1234567"))
# print(validazione_numero("+39 339 1234567"))
# print(validazione_numero("339 1234567"))

# ---------

# ESTRAZIONE HASHTAG
# estrai tutte le parole che iniziano con #
def estrai_hashtag(testo):
    pattern = r"#\w+"
    return re.findall(pattern, testo)

# print(estrai_hashtag("Amo #Python e #regex! #coding è fantastico"))

# ----------

# CENSURA NUMERI CARTA DI CREDITO
# censura tutti i numeri della carta di credito
# sostituisci numeri con * 
# mostra solo ultime 4 cifre
def censura(testo):
    # trovo ed estraggo il numero della carta per lavorarlo
    pattern = r"\d{4}-\d{4}-\d{4}-\d{4}"
    match = re.search(pattern, testo)
    
    numero_carta = match.group()

    ultime_4_cifre = numero_carta[-4:]
    prime_cifre = numero_carta[:-4]

    cifre_censurate = ""
    for i in prime_cifre:
        if i != "-":
            cifre_censurate += "*"
        else:
            cifre_censurate += "-"

    numero_carta_censurato = cifre_censurate + ultime_4_cifre

    testo_censurato = re.sub(pattern, numero_carta_censurato, testo)
    
    return testo_censurato

# print(censura("La mia carta è 1234-5678-9012-3456"))

# ----------

# ESTRAZIONE DOMINI DA URL
# estrai solo il dominio da una lista di url
def estrai_dominio(url: str) -> str:
    # con le tonde separo i blocchi
    # ?: interno ad un blocco lo esclude
    # \. escape per consdierare il . come tale
    # ? in mezzo e non \w per una maggiore generalità (es. altri .)
    # ^ ad inizio di un blocco lo nega, tranne elementi specificati
    # il + esterno alla fine per prendere più caratteri
    pattern = r"://(?:www\.)?([^/]+)"
    return re.search(pattern, url).group(1)

urls = [
    "https://www.google.com/search",
    "http://facebook.com/profile", 
    "https://youtube.com"
    ] 
    
# print(estrai_dominio("https://www.google.com/search"))

# -----------

# FORMATTAZIONE NUMERI DI TELEFONO
# preso un numero di telefono "sporco"
# con spazi, trattini e parentesi
# formattarlo in --> XXX-XXXXXXX
def formatta_numero(numero):
    # trovo tutti i non numeri
    # sostituisco con "" --> rimuovo il non numero
    # ottengo stringa, solo numeri
    numero_pulito = re.sub(r"[^\d]", "", numero)

    # formattazione 
    numero_formattato = f"{numero_pulito[:3]}-{numero_pulito[3:]}"
    return numero_formattato

numeri_telefono = ["339 123-4567", "(02) 1234 567", "01234-(56)  789"]

# print([formatta_numero(numero) for numero in numeri_telefono])