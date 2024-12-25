from Crypto.Cipher import DES
import tkinter as tk
from tkinter import ttk, messagebox

# Fungsi untuk padding
def pad(text):
    while len(text) % 8 != 0:
        text += ' '
    return text

# Fungsi untuk enkripsi
def encrypt(plain_text, key):
    des = DES.new(key.encode('utf-8'), DES.MODE_ECB)
    padded_text = pad(plain_text)
    encrypted_text = des.encrypt(padded_text.encode('utf-8'))
    return encrypted_text.hex()

# Fungsi untuk dekripsi
def decrypt(encrypted_text, key):
    des = DES.new(key.encode('utf-8'), DES.MODE_ECB)
    encrypted_text_bytes = bytes.fromhex(encrypted_text)
    decrypted_text = des.decrypt(encrypted_text_bytes).decode('utf-8').rstrip(' ')
    return decrypted_text

# Fungsi untuk memproses teks
def process_text():
    text = text_input.get("1.0", tk.END).strip()
    key = entry_key.get()
    
    if len(key) != 8:
        messagebox.showerror("Error", "Key harus terdiri dari 8 karakter.")
        return

    if var.get() == 1:  # Encrypt
        result = encrypt(text, key)
    else:  # Decrypt
        result = decrypt(text, key)

    text_output.delete("1.0", tk.END)
    text_output.insert(tk.END, result)

# Setup GUI
root = tk.Tk()
root.title("DES Encryption/Decryption")
root.geometry("1000x800")
root.configure(bg="#FFF5F2")  

# Gaya umum
style = {
    "bg": "#FFF5F2",  
    "frame_bg": "#FFE8E2",  
    "font": ("Arial", 14),
    "title_font": ("Arial", 26, "bold"),
    "entry_bg": "#FFFFFF",  
    "input_fg": "#333333",  
    "btn_bg": "#FF8A80",  
    "btn_fg": "#FFFFFF",  
    "btn_hover": "#E57373",  
    "padx": 20,
    "pady": 20,
    "text_width": 50,
    "text_height": 8,
}

# Frame utama
frame_main = tk.Frame(root, bg=style["frame_bg"], padx=style["padx"], pady=style["pady"], relief="groove", bd=3)
frame_main.place(relx=0.5, rely=0.5, anchor="center")

# Judul aplikasi
label_title = tk.Label(frame_main, text="DES Encryption/Decryption Tool", bg=style["frame_bg"], font=style["title_font"], fg="#D84315")
label_title.grid(row=0, column=0, columnspan=2, pady=(10, 30), sticky="nsew")

# Frame untuk input key
frame_key = tk.Frame(frame_main, bg=style["frame_bg"])
frame_key.grid(row=1, column=0, columnspan=2, sticky="we", pady=10)

label_key = tk.Label(frame_key, text="Key (8 Characters):", bg=style["frame_bg"], font=style["font"], fg="#BF360C")
label_key.pack(side=tk.LEFT, padx=10)

entry_key = tk.Entry(frame_key, width=10, font=style["font"], bg=style["entry_bg"], fg=style["input_fg"])
entry_key.pack(side=tk.LEFT)

# Frame untuk input/output teks
frame_texts = tk.Frame(frame_main, bg=style["frame_bg"])
frame_texts.grid(row=2, column=0, columnspan=2, sticky="nsew", pady=20)

# Input teks
frame_input = tk.Frame(frame_texts, bg=style["frame_bg"], padx=10, pady=10, relief="groove", bd=2)
frame_input.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

label_input = tk.Label(frame_input, text="Input Text:", bg=style["frame_bg"], font=style["font"], fg="#BF360C")
label_input.pack(anchor="w")

text_input = tk.Text(frame_input, width=style["text_width"], height=style["text_height"], font=style["font"], bg=style["entry_bg"], fg=style["input_fg"], wrap=tk.WORD)
text_input.pack(padx=10, pady=10)

# Output teks
frame_output = tk.Frame(frame_texts, bg=style["frame_bg"], padx=10, pady=10, relief="groove", bd=2)
frame_output.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")

label_output = tk.Label(frame_output, text="Output Text:", bg=style["frame_bg"], font=style["font"], fg="#BF360C")
label_output.pack(anchor="w")

text_output = tk.Text(frame_output, width=style["text_width"], height=style["text_height"], font=style["font"], bg=style["entry_bg"], fg=style["input_fg"], wrap=tk.WORD)
text_output.pack(padx=10, pady=10)

# Tombol dan pilihan
frame_controls = tk.Frame(frame_main, bg=style["frame_bg"])
frame_controls.grid(row=3, column=0, columnspan=2, pady=10)

var = tk.IntVar(value=1)
radio_encrypt = tk.Radiobutton(frame_controls, text="Encrypt", variable=var, value=1, bg=style["frame_bg"], font=style["font"], fg="#FF7043")
radio_encrypt.pack(side=tk.LEFT, padx=10)

radio_decrypt = tk.Radiobutton(frame_controls, text="Decrypt", variable=var, value=2, bg=style["frame_bg"], font=style["font"], fg="#FF7043")
radio_decrypt.pack(side=tk.LEFT, padx=10)

button_process = tk.Button(frame_controls, text="Process", command=process_text, font=("Arial", 16), bg=style["btn_bg"], fg=style["btn_fg"], padx=20, pady=10)
button_process.pack(side=tk.LEFT, padx=20)

# Animasi hover pada tombol
def on_enter(event):
    event.widget.config(bg=style["btn_hover"])

def on_leave(event):
    event.widget.config(bg=style["btn_bg"])

button_process.bind("<Enter>", on_enter)
button_process.bind("<Leave>", on_leave)

# Responsiveness
frame_main.grid_rowconfigure(2, weight=1)
frame_main.grid_columnconfigure(0, weight=1)
frame_main.grid_columnconfigure(1, weight=1)
frame_texts.grid_rowconfigure(0, weight=1)
frame_texts.grid_columnconfigure(0, weight=1)
frame_texts.grid_columnconfigure(1, weight=1)

# Loop utama
root.mainloop()
