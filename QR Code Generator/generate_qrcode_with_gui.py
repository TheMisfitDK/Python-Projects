import qrcode
import os
import tkinter as tk
from tkinter import messagebox

def generate_qr():
    url = url_entry.get().strip()
    filename = filename_entry.get().strip()

    if not url:
        messagebox.showerror("Error", "Enter a URL.")
        return

    if not filename:
        filename = "default_qrcode"

    os.makedirs("qrcodes", exist_ok=True)
    path = f"qrcodes/{filename}.png"

    img = qrcode.make(url)
    img.save(path)

    messagebox.showinfo("Done", f"QR code saved as:\n{path}")

# GUI
root = tk.Tk()
root.title("QR Code Maker")

tk.Label(root, text="URL:").pack()
url_entry = tk.Entry(root, width=40)
url_entry.pack()

tk.Label(root, text="Filename:").pack()
filename_entry = tk.Entry(root, width=40)
filename_entry.pack()

tk.Button(root, text="Generate", command=generate_qr).pack(pady=10)

root.mainloop()