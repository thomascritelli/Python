import qrcode
nomeFile = str(input("Inserisci il nome dell'immagine: "))
url = str(input("metti il link: "))
img = qrcode.make(url)
img.save(f'{nomeFile}.jpg')