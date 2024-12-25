import tkinter as tk
from tkinter import ttk

# Fungsi enkripsi menggunakan algoritma Caesar Cipher
def enkripsi(plain_text, shift):
    cipher_text = ""
    for char in plain_text:
        if char.isupper():
            cipher_text += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.islower():
            cipher_text += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            cipher_text += char
    return cipher_text

# Fungsi deskripsi menggunakan algoritma Caesar Cipher
def deskripsi(cipher_text, shift):
    plain_text = ""
    for char in cipher_text:
        if char.isupper():
            plain_text += chr((ord(char) - shift - 65) % 26 + 65)
        elif char.islower():
            plain_text += chr((ord(char) - shift - 97) % 26 + 97)
        else:
            plain_text += char
    return plain_text

# Fungsi untuk memproses teks berdasarkan pilihan enkripsi atau deskripsi
def proses_teks():
    text = text_input.get("1.0", tk.END).strip()
    shift = int(entry_shift.get())
    if var.get() == 1:
        result = enkripsi(text, shift)
    else:
        result = deskripsi(text, shift)
    text_output.delete("1.0", tk.END)
    text_output.insert(tk.END, result)

# Setup GUI
root = tk.Tk()
root.title("Caesar Cipher Encryption Machine")
root.geometry("1000x1000")  
root.resizable(True, True)  
root.configure(bg="#f7edf8")  

# Mengatur gaya
style = {
    "bg": "#f7edf8",  
    "font": ("Arial", 14),
    "title_font": ("Arial", 28, "bold"),
    "padx": 0,
    "pady": 0,
    "btn_bg": "#B39DDB",  
    "btn_fg": "#FFFFFF",  
    "entry_bg": "#ffffff", 
    "input_fg": "#331637",  
    "frame_bg": "#e6c8e9", 
    "text_height": 8,  
    "text_width": 40,  
}

# Frame utama di tengah
frame_main = tk.Frame(root, bg=style["bg"], padx=40, pady=40)
frame_main.pack(fill=tk.BOTH, expand=True)

# Judul aplikasi
label_title = tk.Label(frame_main, text="Cipher Encryption Machine", bg=style["bg"], font=style["title_font"], fg="#B39DDB")
label_title.grid(row=0, column=0, columnspan=2, pady=(10, 30), sticky="nsew")

# Menambahakan pengaturan agar frame utama mengisi ruang secara fleksibel
frame_main.grid_rowconfigure(0, weight=1)  
frame_main.grid_columnconfigure(0, weight=1)  
frame_main.grid_columnconfigure(1, weight=1)  

# Frame untuk nilai shift di atas
frame_shift = tk.Frame(frame_main, bg=style["bg"])
frame_shift.grid(row=1, column=0, columnspan=2, padx=style["padx"], pady=(10), sticky="w")

label_shift = tk.Label(frame_shift, text="Set Shift Value:", bg=style["bg"], font=style["font"], fg="#4A148C")
label_shift.pack(side=tk.LEFT)

entry_shift = tk.Entry(frame_shift, width=6, font=style["font"], bg=style["entry_bg"], justify="center", fg="#331637")
entry_shift.pack(side=tk.LEFT, padx=10)

# Frame untuk input dan output teks sejajar di bawah, memastikan berada di tengah
frame_input_output = tk.Frame(frame_main, bg=style["bg"], padx=20, pady=20)
frame_input_output.grid(row=2, column=0, columnspan=2, padx=20, pady=30, sticky="nsew")

# Menambahkan pengaturan untuk memastikan row dan column bisa mengembang dengan baik
frame_main.grid_rowconfigure(2, weight=1)  
frame_main.grid_columnconfigure(0, weight=1)  
frame_main.grid_columnconfigure(1, weight=1)  

# Bagian input teks
frame_input = tk.Frame(frame_input_output, bg=style["frame_bg"], bd=3, relief="solid", padx=10, pady=10)
frame_input.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

label_input = tk.Label(frame_input, text="Input Text to Encrypt/Decrypt:", bg=style["frame_bg"], font=style["font"], fg="#4A148C")
label_input.pack(anchor="w")

# Menyesuaikan lebar dan tinggi input agar lebih kecil dan sama dengan output
text_input = tk.Text(frame_input, height=style["text_height"], width=style["text_width"], font=style["font"], bg=style["entry_bg"], fg=style["input_fg"], wrap=tk.WORD)
text_input.pack(padx=style["padx"], pady=style["pady"])

# Bagian output teks
frame_output = tk.Frame(frame_input_output, bg=style["frame_bg"], bd=3, relief="solid", padx=10, pady=10)
frame_output.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")

label_output = tk.Label(frame_output, text="Output:", bg=style["frame_bg"], font=style["font"], fg="#4A148C")
label_output.pack(anchor="w")

# Menyesuaikan lebar dan tinggi output agar lebih kecil dan sama dengan input
text_output = tk.Text(frame_output, height=style["text_height"], width=style["text_width"], font=style["font"], bg=style["entry_bg"], fg=style["input_fg"], wrap=tk.WORD)
text_output.pack(padx=style["padx"], pady=style["pady"])

# Menambahkan pengaturan untuk grid dalam frame_input_output agar kolom-kolom bisa mengembang
frame_input_output.grid_rowconfigure(0, weight=1)  
frame_input_output.grid_columnconfigure(0, weight=1)  
frame_input_output.grid_columnconfigure(1, weight=1)  


# Tombol dan pilihan enkripsi/deskripsi
frame_buttons = tk.Frame(frame_main, bg=style["bg"])
frame_buttons.grid(row=3, column=0, columnspan=2, padx=style["padx"], pady=style["pady"])

var = tk.IntVar()
var.set(1)

# Menempatkan pilihan Enkripsi dan Deskripsi di tengah dengan pack() dan anchor
radio_encrypt = tk.Radiobutton(frame_buttons, text="Encrypt", variable=var, value=1, bg=style["bg"], font=style["font"], fg="#4A148C")
radio_encrypt.pack(side=tk.LEFT, padx=20, pady=10)

radio_decrypt = tk.Radiobutton(frame_buttons, text="Decrypt", variable=var, value=2, bg=style["bg"], font=style["font"], fg="#4A148C")
radio_decrypt.pack(side=tk.LEFT, padx=20, pady=10)

# Tombol untuk proses enkripsi/deskripsi
button_process = tk.Button(frame_buttons, text="Process Text", command=proses_teks, font=("Arial", 16), bg=style["btn_bg"], fg=style["btn_fg"], relief="raised", width=20)
button_process.pack(pady=20)

# Menambahkan animasi hover untuk tombol
def on_enter(event):
    event.widget.config(bg="#9575CD")

def on_leave(event):
    event.widget.config(bg=style["btn_bg"])

button_process.bind("<Enter>", on_enter)
button_process.bind("<Leave>", on_leave)

# Mengatur frame_buttons agar berada di tengah
frame_buttons.grid_rowconfigure(0, weight=1)  
frame_buttons.grid_columnconfigure(0, weight=1)  
frame_buttons.grid_columnconfigure(1, weight=1)  

# Menjalankan loop utama GUI
root.mainloop()
