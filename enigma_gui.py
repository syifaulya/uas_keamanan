import tkinter as tk
from tkinter import ttk

class Enigma:
    def _init_(self, rotor1_pos=0, rotor2_pos=0, rotor3_pos=0):
        self.rotor1 = [4, 10, 12, 5, 11, 6, 3, 16, 21, 25, 13, 19, 14, 22, 24, 7, 23, 20, 18, 15, 0, 8, 1, 17, 2, 9]
        self.rotor2 = [0, 9, 3, 10, 18, 8, 17, 20, 23, 1, 11, 7, 22, 19, 12, 2, 16, 6, 25, 13, 15, 24, 5, 21, 14, 4]
        self.rotor3 = [1, 3, 5, 7, 9, 11, 2, 15, 17, 19, 23, 21, 25, 13, 24, 4, 8, 22, 6, 0, 10, 12, 20, 18, 16, 14]
        self.reflector = [24, 17, 20, 7, 16, 18, 11, 3, 15, 23, 13, 6, 14, 10, 12, 8, 4, 1, 5, 25, 2, 22, 21, 9, 0, 19]
        self.rotor1_pos = rotor1_pos
        self.rotor2_pos = rotor2_pos
        self.rotor3_pos = rotor3_pos
        self.inverse_rotor1 = self.inverse(self.rotor1)
        self.inverse_rotor2 = self.inverse(self.rotor2)
        self.inverse_rotor3 = self.inverse(self.rotor3)

    def inverse(self, rotor):
        inverse_rotor = [0] * 26
        for i in range(26):
            inverse_rotor[rotor[i]] = i
        return inverse_rotor

    def encrypt_decrypt_char(self, ch):
        if ch.isalpha():
            is_lower = ch.islower()
            ch = ch.upper()
            offset = ord(ch) - ord('A')

            # Rotor maju
            offset = (self.rotor1[(offset + self.rotor1_pos) % 26] - self.rotor1_pos) % 26
            offset = (self.rotor2[(offset + self.rotor2_pos) % 26] - self.rotor2_pos) % 26
            offset = (self.rotor3[(offset + self.rotor3_pos) % 26] - self.rotor3_pos) % 26

            # Reflektor
            offset = self.reflector[offset]

            # Rotor mundur (invers)
            offset = (self.inverse_rotor3[(offset + self.rotor3_pos) % 26] - self.rotor3_pos) % 26
            offset = (self.inverse_rotor2[(offset + self.rotor2_pos) % 26] - self.rotor2_pos) % 26
            offset = (self.inverse_rotor1[(offset + self.rotor1_pos) % 26] - self.rotor1_pos) % 26

            # Rotasi rotor setelah setiap karakter
            self.rotor1_pos = (self.rotor1_pos + 1) % 26
            if self.rotor1_pos == 0:
                self.rotor2_pos = (self.rotor2_pos + 1) % 26
                if self.rotor2_pos == 0:
                    self.rotor3_pos = (self.rotor3_pos + 1) % 26

            result = chr(offset + ord('A'))
            return result.lower() if is_lower else result
        else:
            return ch  # Mengembalikan karakter jika bukan huruf
        
    def process(self, text):
        return ''.join(self.encrypt_decrypt_char(ch) for ch in text)

def process_text():
    input_text = text_input.get("1.0", tk.END).strip()
    rotor1_pos = int(entry_rotor1.get())
    rotor2_pos = int(entry_rotor2.get())
    rotor3_pos = int(entry_rotor3.get())
    
    enigma = Enigma(rotor1_pos, rotor2_pos, rotor3_pos)
    
    if var.get() == 1:
        result = enigma.process(input_text)
    else:
        result = enigma.process(input_text)  # Untuk dekripsi, bisa ditambahkan logika lain jika diperlukan

    text_output.delete("1.0", tk.END)
    text_output.insert(tk.END, result)

# Setup GUI
root = tk.Tk()
root.title("Enigma Cipher")
root.geometry("800x600")
root.configure(bg="#dcedc8")  # Warna latar belakang hijau muda

# Main frame with rounded corners and shadow effect
frame_main = tk.Frame(root, bg="#ffffff", bd=0, relief="flat", padx=20, pady=20)
frame_main.place(relx=0.5, rely=0.5, anchor="center", width=760, height=540)

# Title label inside the frame
label_title = tk.Label(frame_main, text="Enigma Cipher", bg="#ffffff", font=("Helvetica", 24, "bold"), fg="#388e3c")
label_title.grid(row=0, column=0, columnspan=2, pady=(0, 20), sticky="nsew")

# Rotor position frames
frame_rotors = tk.Frame(frame_main, bg="#ffffff")
frame_rotors.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

label_rotor1 = tk.Label(frame_rotors, text="Rotor 1 Position:", bg="#ffffff", font=("Helvetica", 12, "bold"), fg="#388e3c")
label_rotor1.grid(row=0, column=0, padx=(0, 10), sticky="w")
entry_rotor1 = tk.Entry(frame_rotors, width=5, font=("Helvetica", 12), bd=3, relief="solid", bg="#dcedc8", fg="#388e3c")
entry_rotor1.grid(row=0, column=1, padx=10)

label_rotor2 = tk.Label(frame_rotors, text="Rotor 2 Position:", bg="#ffffff", font=("Helvetica", 12, "bold"), fg="#388e3c")
label_rotor2.grid(row=0, column=2, padx=(0, 10), sticky="w")
entry_rotor2 = tk.Entry(frame_rotors, width=5, font=("Helvetica", 12), bd=3, relief="solid", bg="#dcedc8", fg="#388e3c")
entry_rotor2.grid(row=0, column=3, padx=10)

label_rotor3 = tk.Label(frame_rotors, text="Rotor 3 Position:", bg="#ffffff", font=("Helvetica", 12, "bold"), fg="#388e3c")
label_rotor3.grid(row=0, column=4, padx=(0, 10), sticky="w")
entry_rotor3 = tk.Entry(frame_rotors, width=5, font=("Helvetica", 12), bd=3, relief="solid", bg="#dcedc8", fg="#388e3c")
entry_rotor3.grid(row=0, column=5, padx=10)

# Input text frame
frame_input = tk.Frame(frame_main, bg="#ffffff")
frame_input.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

label_input = tk.Label(frame_input, text="Input Text:", bg="#ffffff", font=("Helvetica", 12, "bold"), fg="#388e3c")
label_input.grid(row=0, column=0, padx=(0, 10), pady=(0, 5), sticky="w")

text_input = tk.Text(frame_input, height=6, width=70, font=("Helvetica", 12), bd=3, relief="solid", bg="#dcedc8", fg="#388e3c", wrap="word")
text_input.grid(row=1, column=0, pady=(5, 10), sticky="ew")

# Process buttons
frame_buttons = tk.Frame(frame_main, bg="#ffffff")
frame_buttons.grid(row=3, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

var = tk.IntVar()
var.set(1)

radio_encrypt = ttk.Radiobutton(frame_buttons, text="Encrypt", variable=var, value=1, style="TRadiobutton")
radio_encrypt.grid(row=0, column=0, padx=10, pady=5)

radio_decrypt = ttk.Radiobutton(frame_buttons, text="Decrypt", variable=var, value=2, style="TRadiobutton")
radio_decrypt.grid(row=0, column=1, padx=10, pady=5)

button_process = tk.Button(frame_buttons, text="Process Text", command=process_text, font=("Helvetica", 12), bg="#388e3c", fg="#ffffff", bd=0, width=15, height=1, relief="flat")
button_process.grid(row=0, column=2, padx=10, pady=5)

# Output text frame
frame_output = tk.Frame(frame_main, bg="#ffffff")
frame_output.grid(row=4, column=0, columnspan=2, padx=10, pady=(10, 20), sticky="nsew")

label_output = tk.Label(frame_output, text="Output:", bg="#ffffff", font=("Helvetica", 12, "bold"), fg="#388e3c")
label_output.grid(row=0, column=0, padx=(0, 10), pady=(0, 5), sticky="w")

text_output = tk.Text(frame_output, height=6, width=70, font=("Helvetica", 12), bd=3, relief="solid", bg="#dcedc8", fg="#388e3c", wrap="word")
text_output.grid(row=1, column=0, pady=(5, 10), sticky="ew")

# Run the main GUI loop
root.mainloop()
