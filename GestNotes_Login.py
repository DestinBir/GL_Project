import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import os

# Récupération du chemin du Bureau
CHEMIN_VERS_BUREAU = os.path.join(os.path.expanduser("~"), "Desktop")
logo_path = os.path.join(CHEMIN_VERS_BUREAU, "ucb logo.jpg")

# Création de la fenêtre principale
root = tk.Tk()
root.title("GEST NOTES")
root.geometry("400x500")  # Taille de la fenêtre
root.configure(bg="white")

# Centrer la fenêtre sur l'écran
root.update_idletasks()
width = root.winfo_width()
height = root.winfo_height()
x = (root.winfo_screenwidth() // 2) - (400 // 2)
y = (root.winfo_screenheight() // 2) - (500 // 2)
root.geometry(f"400x500+{x}+{y}")

# Charger le logo (Assurez-vous que l'image existe)
try:
    logo = Image.open(logo_path)
    logo = logo.resize((120, 100))  # Redimensionner le logo
    logo_tk = ImageTk.PhotoImage(logo)
    logo_label = tk.Label(root, image=logo_tk, bg="white")
    logo_label.pack(pady=10)
except Exception as e:
    print(f"Erreur lors du chargement du logo : {e}")
    logo_label = tk.Label(root, text="[Logo introuvable]", fg="red", bg="white", font=("Arial", 10))
    logo_label.pack(pady=10)

# Titre centré
title_label = tk.Label(root, text="GEST NOTES", fg="#f48024", bg="white", font=("Arial", 14, "bold"))
title_label.pack(pady=5)

# Conteneur du formulaire (centré)
frame = tk.Frame(root, bg="#0f2c4d", padx=20, pady=20)
frame.pack(pady=20)

# Centrer les widgets du frame
for widget in frame.winfo_children():
    widget.pack_configure(anchor="center")

# Champ Nom d'utilisateur
tk.Label(frame, text="Nom d'utilisateur", fg="white", bg="#0f2c4d", font=("Arial", 10)).pack(anchor="center")
username_entry = ttk.Entry(frame, width=30)
username_entry.pack(pady=5)

# Champ Mot de passe
tk.Label(frame, text="Mot de passe", fg="white", bg="#0f2c4d", font=("Arial", 10)).pack(anchor="center")
password_entry = ttk.Entry(frame, width=30, show="*")
password_entry.pack(pady=5)

# Case à cocher "Se souvenir"
remember_var = tk.BooleanVar()
remember_check = tk.Checkbutton(frame, text="Se souvenir de mon mot de passe", variable=remember_var, fg="white",
                                bg="#0f2c4d", font=("Arial", 9), selectcolor="#0f2c4d")
remember_check.pack(anchor="center", pady=5)

# Bouton Soumettre
submit_button = tk.Button(frame, text="Soumettre", bg="#f48024", fg="white", font=("Arial", 10, "bold"), width=15)
submit_button.pack(pady=10)

# Lancer l'application
root.mainloop()
