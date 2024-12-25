import tkinter as tk
from tkinter import filedialog, ttk
from stegano import lsb
import os

def browse_image(entry):
    img_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png *.jpg")])
    if img_path:
        entry.delete(0, tk.END)
        entry.insert(0, img_path)

def browse_save_path(entry):
    save_path = filedialog.asksaveasfilename(defaultextension=".png",
                                             filetypes=[("PNG Files", "*.png")])
    if save_path:
        entry.delete(0, tk.END)
        entry.insert(0, save_path)

def hide_message():
    img_path = hide_img_path_entry.get().strip()
    message = hide_message_entry.get().strip()
    save_path = hide_save_path_entry.get().strip()

    if not img_path or not os.path.exists(img_path):
        hide_result_label.config(text="Error: Path gambar tidak valid.", fg="red")
        return

    if not message:
        hide_result_label.config(text="Error: Pesan tidak boleh kosong.", fg="red")
        return

    if not save_path:
        hide_result_label.config(text="Error: Path penyimpanan tidak valid.", fg="red")
        return

    try:
        secret = lsb.hide(img_path, message)
        secret.save(save_path)
        hide_result_label.config(text=f"Pesan berhasil disembunyikan di: {save_path}", fg="green")
    except Exception as e:
        hide_result_label.config(text=f"Error: {e}", fg="red")

def show_message():
    img_path = show_img_path_entry.get().strip()

    if not img_path or not os.path.exists(img_path):
        show_result_label.config(text="Error: Path gambar tidak valid.", fg="red")
        return

    try:
        clear_message = lsb.reveal(img_path)
        if clear_message:
            show_result_label.config(text=f"Pesan tersembunyi: {clear_message}", fg="green")
        else:
            show_result_label.config(text="Tidak ada pesan tersembunyi dalam gambar.", fg="orange")
    except Exception as e:
        show_result_label.config(text=f"Error: {e}", fg="red")

# Warna tema
bg_color = "#2C3E50"  # Dark Blue Gray
header_color = "#34495E"  # Elegant Dark Blue
button_color = "#5DADE2"  # Light Blue
text_color = "#ECF0F1"  # Light Gray

# Set up root window
root = tk.Tk()
root.title("Steganography Tool with Tabs")
root.configure(bg=bg_color)
root.geometry("600x400")
root.resizable(True, True)

# Heading
header_label = tk.Label(root, text="Steganography Tool", font=("Arial", 18, "bold"), bg=header_color, fg=text_color, pady=10)
header_label.pack(fill="x")

# Notebook (tab container)
notebook = ttk.Notebook(root)
notebook.pack(pady=10, padx=10, expand=True, fill="both")

# Tab 1: Sembunyikan Pesan
hide_tab = ttk.Frame(notebook)
notebook.add(hide_tab, text="Sembunyikan Pesan")

hide_img_path_label = tk.Label(hide_tab, text="Path Gambar:", font=("Arial", 12), bg=bg_color, fg=text_color)
hide_img_path_label.grid(row=0, column=0, sticky="w", pady=5)
hide_img_path_entry = tk.Entry(hide_tab, font=("Arial", 12))
hide_img_path_entry.grid(row=0, column=1, sticky="ew", pady=5, padx=5)
hide_browse_img_button = tk.Button(hide_tab, text="Browse", command=lambda: browse_image(hide_img_path_entry), bg=button_color, font=("Arial", 10))
hide_browse_img_button.grid(row=0, column=2, padx=5)

hide_message_label = tk.Label(hide_tab, text="Pesan:", font=("Arial", 12), bg=bg_color, fg=text_color)
hide_message_label.grid(row=1, column=0, sticky="w", pady=5)
hide_message_entry = tk.Entry(hide_tab, font=("Arial", 12))
hide_message_entry.grid(row=1, column=1, sticky="ew", pady=5, padx=5)

hide_save_path_label = tk.Label(hide_tab, text="Simpan ke:", font=("Arial", 12), bg=bg_color, fg=text_color)
hide_save_path_label.grid(row=2, column=0, sticky="w", pady=5)
hide_save_path_entry = tk.Entry(hide_tab, font=("Arial", 12))
hide_save_path_entry.grid(row=2, column=1, sticky="ew", pady=5, padx=5)
hide_browse_save_button = tk.Button(hide_tab, text="Browse", command=lambda: browse_save_path(hide_save_path_entry), bg=button_color, font=("Arial", 10))
hide_browse_save_button.grid(row=2, column=2, padx=5)

hide_button = tk.Button(hide_tab, text="Sembunyikan Pesan", command=hide_message, bg=button_color, font=("Arial", 12))
hide_button.grid(row=3, column=1, pady=10)

hide_result_label = tk.Label(hide_tab, text="", font=("Arial", 12), bg=bg_color, fg=text_color)
hide_result_label.grid(row=4, column=0, columnspan=3, pady=5)

# Tab 2: Tampilkan Pesan
show_tab = ttk.Frame(notebook)
notebook.add(show_tab, text="Tampilkan Pesan")

show_img_path_label = tk.Label(show_tab, text="Path Gambar:", font=("Arial", 12), bg=bg_color, fg=text_color)
show_img_path_label.grid(row=0, column=0, sticky="w", pady=5)
show_img_path_entry = tk.Entry(show_tab, font=("Arial", 12))
show_img_path_entry.grid(row=0, column=1, sticky="ew", pady=5, padx=5)
show_browse_img_button = tk.Button(show_tab, text="Browse", command=lambda: browse_image(show_img_path_entry), bg=button_color, font=("Arial", 10))
show_browse_img_button.grid(row=0, column=2, padx=5)

show_button = tk.Button(show_tab, text="Tampilkan Pesan", command=show_message, bg=button_color, font=("Arial", 12))
show_button.grid(row=1, column=1, pady=10)

show_result_label = tk.Label(show_tab, text="", font=("Arial", 12), bg=bg_color, fg=text_color)
show_result_label.grid(row=2, column=0, columnspan=3, pady=5)

# Configure grid weights
for frame in [hide_tab, show_tab]:
    frame.columnconfigure(1, weight=1)

root.mainloop()
