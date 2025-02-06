import tkinter as tk
from tkinter import font

# Création de la fenêtre principale
root = tk.Tk()
root.title("Promotion")
root.state("zoomed")  # Plein écran

# Définition des couleurs et polices
bg_color = "#0A2A43"  # Bleu foncé des blocs
text_color = "white"
highlight_color = "#F28C28"  # Orange pour le titre BAC

title_font = font.Font(family="Arial", size=20, weight="bold")
subtitle_font = font.Font(family="Arial", size=14, weight="bold")
desc_font = font.Font(family="Arial", size=12)

# Création du titre principal
title_frame = tk.Frame(root, bg="white")
title_frame.pack(fill="x", pady=10)

title_label = tk.Label(title_frame, text="PROMOTION", font=title_font, fg="black", bg="white")
title_label.pack()

subtitle_label = tk.Label(title_frame, text="choisir une promotion pour continuer", font=subtitle_font, fg=highlight_color, bg="white")
subtitle_label.pack()

# Conteneur principal
main_frame = tk.Frame(root, bg="white")
main_frame.pack(expand=True, fill="both")

# Fonction pour ouvrir une nouvelle fenêtre
def open_new_window(bac_title):
    new_window = tk.Toplevel(root)
    new_window.title(bac_title)
    new_window.geometry("500x300")
    
    label = tk.Label(new_window, text=f"Bienvenue dans la section {bac_title} !", font=subtitle_font, fg="black")
    label.pack(expand=True)

# Fonction pour créer un bloc BAC sous forme de bouton
def create_bac_block(parent, title):
    button = tk.Button(parent, text=title + "\n\nDescription privilèges\nLorem ipsum dolor sit amet...",
                       font=subtitle_font, fg=text_color, bg=bg_color, wraplength=250,
                       width=25, height=10, relief="raised", bd=3,
                       command=lambda: open_new_window(title))
    button.pack(side="left", expand=True, fill="both", padx=10, pady=20)

# Création des trois boutons BAC
create_bac_block(main_frame, "BAC 1")
create_bac_block(main_frame, "BAC 2")
create_bac_block(main_frame, "BAC 3")

# Lancement de l'application
root.mainloop()
