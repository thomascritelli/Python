import qrcode
img = qrcode.make(input("metti il link: "))
img.save(f'{(input("Inserisci il nome dell'immagine: "))}.png')