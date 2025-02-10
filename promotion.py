import tkinter as tk
from tkinter import font, messagebox
from functions import connect_to_db, get_promotions

class Promotion(tk.Frame):
    def __init__(self, master, **kwargs):
        super().__init__(**kwargs)
        self.master = master
        self.selected_promotion = None # Variable pour stocker la promotion sélectionnée
        self.selected_promotion_id = None
        
        # Définition des couleurs et polices
        self.bg_color = "#0A2A43"  # Bleu foncé des blocs
        self.text_color = "white"
        self.highlight_color = "#F28C28"  # Orange pour le titre BAC

        self.title_font = font.Font(family="Arial", size=20, weight="bold")
        self.subtitle_font = font.Font(family="Arial", size=14, weight="bold")
        self.desc_font = font.Font(family="Arial", size=12)
        
        self.Contener()

    def Contener(self):
        # Création du titre principal
        title_frame = tk.Frame(self, bg="white")
        title_frame.pack(fill="x", pady=10)

        title_label = tk.Label(title_frame, text="PROMOTION", font=self.title_font, fg="black", bg="white")
        title_label.pack()

        subtitle_label = tk.Label(title_frame, text="Choisir une promotion pour continuer", font=self.subtitle_font, fg=self.highlight_color, bg="white")
        subtitle_label.pack()

        # Conteneur principal
        main_frame = tk.Frame(self, bg="white")
        main_frame.pack(expand=True, fill="both")

        # Récupération des promotions
        promotions = get_promotions(connect_to_db())
        
        if not promotions:
            no_promo_label = tk.Label(main_frame, text="Aucune promotion disponible", font=self.subtitle_font, fg="red", bg="white")
            no_promo_label.pack(pady=20)
            return
        
        # Création des blocs par promotion (max 4 par ligne)
        row_frame = None
        for i, prom in enumerate(promotions):
            if i % 4 == 0:
                row_frame = tk.Frame(main_frame, bg="white")
                row_frame.pack(fill="x", padx=20)
            
            self.create_bac_block(row_frame, prom[1], prom[0])
        
        # Ajout du bouton de retour
        return_button = tk.Button(self, text="Retour", font=self.subtitle_font, fg="white", bg="orange", command=self.master.previous_screen)
        return_button.pack(pady=10)

    # Fonction pour gérer la sélection de promotion
    def select_promotion(self, promotion_id, promotion_name):
        self.selected_promotion = promotion_name
        self.selected_promotion_id = promotion_id
        print(f"Promotion sélectionnée : {self.selected_promotion} ID: {self.selected_promotion_id}")
        self.master.transition(self.master.liste_etudiant)

    # Fonction pour créer un bloc BAC sous forme de bouton
    def create_bac_block(self, parent, title, promotion_id):
        button = tk.Button(parent, text=title + "\n\nEn savoir plus\nListe des étudiants...",
                           font=self.subtitle_font, fg=self.text_color, bg=self.bg_color, wraplength=250,
                           width=18, height=8, relief="raised", bd=3,
                           command=lambda: self.select_promotion(promotion_id, title))
        button.pack(side="left", expand=True, padx=10, pady=10)
