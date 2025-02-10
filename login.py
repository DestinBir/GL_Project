import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import os


class Login(tk.Frame):
    def __init__(self, master, **kwargs):
        super().__init__(**kwargs)
        self.master = master
        self.Contener()
        
    def Contener(self):
        # Récupération du chemin du Bureau
        CHEMIN_VERS_BUREAU = os.path.join(os.path.expanduser("~"), "Desktop")
        logo_path = os.path.join(CHEMIN_VERS_BUREAU, "Logo-UCB.png")

        self.frame = tk.Frame(self, width=200, height=200)
        self.frame.place(relx=0.5, rely=0.5, anchor="center")

        # Charger le logo (Assurez-vous que l'image existe)
        try:
            logo = Image.open(logo_path)
            logo = logo.resize((120, 100))  # Redimensionner le logo
            self.logo_tk = ImageTk.PhotoImage(logo)  # Stocker l'image dans un attribut
            logo_label = tk.Label(self.frame, image=self.logo_tk, bg="#FFFFFF")  # Blanc
            logo_label.pack(pady=10)
        except Exception as e:
            print(f"Erreur lors du chargement du logo : {e}")
            logo_label = tk.Label(self.frame, text="[Logo introuvable]", fg="red", bg="#FFFFFF", font=("Arial", 10))
            logo_label.pack(pady=10)


        # Titre centré
        title_label = tk.Label(self.frame, text="GEST NOTES", fg="#f48024", bg="white", font=("Arial", 14, "bold"))
        title_label.pack(pady=5)

        # Conteneur du formulaire (centré)
        frame1 = tk.Frame(self.frame, bg="#0f2c4d", padx=20, pady=20)
        frame1.pack(pady=20)

        # Centrer les widgets du frame
        for widget in frame1.winfo_children():
            widget.pack_configure(anchor="center")

        # Champ Nom d'utilisateur
        tk.Label(frame1, text="Nom d'utilisateur", fg="white", bg="#0f2c4d", font=("Arial", 10)).pack(anchor="center")
        username_entry = ttk.Entry(frame1, width=30)
        username_entry.pack(pady=5)

        # Champ Mot de passe
        tk.Label(frame1, text="Mot de passe", fg="white", bg="#0f2c4d", font=("Arial", 10)).pack(anchor="center")
        password_entry = ttk.Entry(frame1, width=30, show="*")
        password_entry.pack(pady=5)

        # Case à cocher "Se souvenir"
        remember_var = tk.BooleanVar()
        remember_check = tk.Checkbutton(frame1, text="Se souvenir de mon mot de passe", variable=remember_var, fg="white",
                                        bg="#0f2c4d", font=("Arial", 9), selectcolor="#0f2c4d")
        remember_check.pack(anchor="center", pady=5)

        # Bouton Soumettre
        submit_button = tk.Button(frame1, text="Soumettre", bg="#f48024", fg="white", font=("Arial", 10, "bold"), width=15, command=lambda : self.master.transition(self.master.promotion))
        submit_button.pack(pady=10)
    
    def Connexion(self):
        pass