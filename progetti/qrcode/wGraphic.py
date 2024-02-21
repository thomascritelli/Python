import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import qrcode

# funzione per generare il qrcode
def generate_qr_code(url, nome):
    img = qrcode.make(url)
    img.save(f'{nome}.png')
    show_qr_code(nome)

# funzione per visualizzare il qr code nella finestra
def show_qr_code(nome):
    image = Image.open(f'{nome}.png')
    photo = ImageTk.PhotoImage(image)
    qr_label.config(image=photo)
    qr_label.image = photo

# root window
root = tk.Tk()
root.geometry('900x700')
root.title('QR Code Generator')

# Entry
nome = tk.StringVar()
url = tk.StringVar()
textboxNome = ttk.Entry(root, textvariable=nome)
textboxUrl = ttk.Entry(root, textvariable=url)

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
    command=lambda: generate_qr_code(url.get(), nome.get())
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


