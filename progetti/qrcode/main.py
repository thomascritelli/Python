import tkinter as tk
from tkinter import ttk
import qrcode
from PIL import Image, ImageTk

def generate_qr_code(s):
    img = qrcode.make(s)
    img.save('qrcode.png')

def show_qr_code():
    image = Image.open('qrcode.png')
    photo = ImageTk.PhotoImage(image)
    qr_label.config(image=photo)
    qr_label.image = photo

# root window
root = tk.Tk()
root.geometry('300x200')
root.title('QR Code Generator')




# Entry
text = tk.StringVar()
textbox = ttk.Entry(root, textvariable=text)

textbox.pack(
    ipadx=5,
    ipady=5,
    expand=True
    )

# ok button
ok_button = ttk.Button(
    root,
    text='Genera',
    command=lambda: generate_qr_code(text.get())
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


