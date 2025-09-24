# una sola @
# caratteri speciali (. _ % + -)
# local part con caratteri speciali ma non iniziali/finali 
# il carattere "." non presente due volte consecutivamente
# domain diverso da @tempmail.com 
# prova richieste http al domain della mail == 200
# implementazione requests


import requests

def check_mail(mail):
    if "@" not in mail:
        return "❌ Mail non valida"
    
    local, domain = mail.split("@")
    speciali = (".", "_", "%", "+", "-")
    
    for i in speciali:
        if local.startswith(i) or local.endswith(i):
            return "❌ Mail non valida"
    
    if domain == "tempmail.com":
        return "❌ Mail non valida"

    if "." not in domain:
        return "❌ Mail non valida"
    
    index = local.find(".")
    if index:
        if local[index - 1] == "." or local[index + 1] == ".":
            return "❌ Mail non valida"

    url = f"https://{domain}"

    richiesta = requests.get(url)
    if richiesta.status_code != 200:
        raise ConnectionError
    
    return "✅ Mail valida", url


lista_mail = ["ciao1234.gmail.com", ".ciao@libero.it", "prova.@yahoo.it", "mail_valida@tempmail.com", "duepun..tii@gmail.com", "mailgiusta_34@gmail.com"]

for i in lista_mail:
    valida = check_mail(i)  
    print(valida)