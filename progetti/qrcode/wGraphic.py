import tkinter as tk
from tkinter import ttk
from PIL import Image
import qrcode
import cv2

def getInfo(textUrl, textNme):
    nome = textNome.get()
    url = textUrl.get()
    textNome.set("")
    textUrl.set("")
    generate_qr_code(url, nome)
    show_qr_code(nome)

# funzione per generare il qrcode
def generate_qr_code(url, nome):
    img = qrcode.make(url)
    img.save(f'{nome}.png')

# funzione per visualizzare il qr code
def show_qr_code(nome):
    img = Image.open(f'{nome}.png')
    img.show()

# root window
root = tk.Tk()
root.geometry('300x200')
root.title('QR Code Generator')

# Entry
textNome = tk.StringVar()
textUrl = tk.StringVar()
textboxNome = ttk.Entry(root, textvariable=textNome)
textboxUrl = ttk.Entry(root, textvariable=textUrl)

textboxNome.pack(
    ipadx=5,
    ipady=5,
    expand=True
    )

textboxUrl.pack(
    ipadx=5,
    ipady=5,
    expand=True
    )

# ok button
ok_button = ttk.Button(
    root,
    text='Genera',
    command=lambda: getInfo(textUrl, textNome)
)

ok_button.pack(
    ipadx=5,
    ipady=5,
    expand=True
)

# exit button
exit_button = ttk.Button(
    root,
    text='Exit',
    command=lambda: root.quit()
)

exit_button.pack(
    ipadx=5,
    ipady=5,
    expand=True
)

# QR code label
qr_label = ttk.Label(root)
qr_label.pack(ipadx=5, ipady=5, expand=True)

root.mainloop()


