import tkinter as tk
from tkinter import font, messagebox
from functions import connect_to_db, get_promotions

class Promotion(tk.Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.master = master

        # Couleurs
        self.bg_color = "#0A2A43"
        self.text_color = "white"
        self.highlight_color = "#F28C28"
        self.button_hover_color = "#F4A261"

        # Polices
        self.title_font = font.Font(family="Arial", size=22, weight="bold")
        self.subtitle_font = font.Font(family="Arial", size=14, weight="bold")
        self.button_font = font.Font(family="Arial", size=12)

        # Construire l'interface
        self.create_widgets()

    def create_widgets(self):
        # Frame du titre
        title_frame = tk.Frame(self, bg="white", pady=10)
        title_frame.pack(fill="x")

        tk.Label(title_frame, text="PROMOTION", font=self.title_font, fg="black", bg="white").pack()
        tk.Label(title_frame, text="Choisir une promotion", font=self.subtitle_font, fg=self.highlight_color, bg="white").pack()

        # Frame principale
        main_frame = tk.Frame(self, bg="white", padx=20, pady=10)
        main_frame.pack(expand=True, fill="both")

        # Récupération des promotions
        promotions = get_promotions(connect_to_db())

        if not promotions:
            tk.Label(main_frame, text="Aucune promotion disponible", font=self.subtitle_font, fg="red", bg="white").pack(pady=20)
            return

        # Affichage des boutons des promotions
        for prom in promotions:
            btn = tk.Button(main_frame, text=prom[1], font=self.button_font, fg="white", bg=self.bg_color,
                            width=25, height=2, relief="flat", bd=3, cursor="hand2",
                            command=lambda p_id=prom[0], p_name=prom[1]: self.select_promotion(p_id, p_name))
            btn.pack(pady=8, ipadx=5)

            # Effet de survol
            btn.bind("<Enter>", lambda e, b=btn: b.config(bg=self.button_hover_color))
            btn.bind("<Leave>", lambda e, b=btn: b.config(bg=self.bg_color))

    def select_promotion(self, promotion_id, promotion_name):
        self.master.promotion_name = promotion_name
        self.master.promotion_id = promotion_id
        messagebox.showinfo("Promotion sélectionnée", f"Vous avez sélectionné {promotion_name}")
        self.master.liste_etudiant.update_promotion_info()
        self.master.transition(self.master.liste_etudiant)
