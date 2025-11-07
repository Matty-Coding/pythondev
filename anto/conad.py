import requests, os
from bs4 import BeautifulSoup
from PIL import Image

def crea_url_negozi():
    negozi = ["conad"]

    url_base = "https://www.tuttiprezzi.it"
    
    return f"{url_base}/conad.html", negozi, url_base
 
def prendi_url_immagini(link_negozio):
    try:
        response = requests.get(link_negozio)

        if response.status_code == 200:
            print(f"\n✅ Connesso a {link_negozio}!\n")

            soup = BeautifulSoup(response.text, "html.parser")
            elemento = soup.find_all("img")
            lista_url_immagini = []
            for url in elemento:
                all_img = url.get("src")
                img = all_img.split("/")[-1].split("_")[0] 
                if len(img.strip()) == 1:
                    lista_url_immagini.append(all_img)        

            return lista_url_immagini
        else:
            print(f"❌ Errore nella connessione a {link_negozio}, Status Code: {response.status_code}")
            return []

    except Exception as e:
        print(f"❌ Errore durante il download delle immagini da {link_negozio}: {e}")
        return []

def scarica_immagini(url_immagine, nome_negozio, url_base):
    try:
        # Scarica i dati dell'immagine
        immagine_data = requests.get(f"{url_base}/{url_immagine}").content

        # Crea la cartella se non esiste
        cartella = f"Images_{nome_negozio}"
        os.makedirs(cartella, exist_ok=True)

        # Nome file basato sull'URL
        nome_file = os.path.basename(url_immagine)

        # Salva l'immagine
        with open(f"{cartella}/{nome_file}", "wb") as file:
            file.write(immagine_data)  

        print(f"✅ Immagine salvata: {cartella}/{nome_file}")

    except Exception as e:
        print(f"❌ Errore nel download di {url_immagine}: {e}")

def crea_pdf(cartella):
    try:
        immagini = [os.path.join(cartella, img) for img in os.listdir(cartella) if img.endswith((".jpg", ".png"))]
        immagini.sort()  # Ordina le immagini per nome

        if immagini:
            immagini_aperture = [Image.open(img).convert("RGB") for img in immagini]

            # Salva le immagini come PDF
            pdf_path = os.path.join(cartella, "volantino_conad.pdf")
            immagini_aperture[0].save(pdf_path, save_all=True, append_images=immagini_aperture[1:])

            print(f"📄 PDF creato: {pdf_path}")
        else:
            print(f"⚠️ Nessuna immagine trovata in {cartella}, salto la creazione del PDF.")

    except Exception as e:
        print(f"❌ Errore nella creazione del PDF per {cartella}: {e}")

def main():
    link_negozi, nome_negozi, url_base = crea_url_negozi()

    for link_negozio, nome_negozio in zip(link_negozi, nome_negozi):
        link_immagini = prendi_url_immagini(link_negozio=link_negozio)

        if link_immagini:
            link_immagini.sort()
            print(f"\n🔹 Trovate {len(link_immagini)} immagini per {nome_negozio}")
        else:
            print(f"\n⚠️ Nessuna immagine trovata per {nome_negozio}")

        for url_immagine in link_immagini:
            scarica_immagini(url_immagine, nome_negozio, url_base)

        crea_pdf(f"Images_{nome_negozio}")

if __name__ == "__main__":
    main()