import tkinter as tk
from tkinter import font, messagebox, Canvas, Frame, Scrollbar
from functions import connect_to_db, get_promotions

class Promotion(tk.Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.master = master

        self.bg_color = "#0A2A43"
        self.text_color = "white"
        self.highlight_color = "#F28C28"
        self.button_bg = "#1572A1"
        self.button_hover_bg = "#1E90FF"

        self.title_font = font.Font(family="Arial", size=20, weight="bold")
        self.subtitle_font = font.Font(family="Arial", size=14, weight="bold")
        self.button_font = font.Font(family="Arial", size=12)

        self.create_widgets()

    def create_widgets(self):
        # Header
        title_frame = tk.Frame(self, bg="white", pady=10)
        title_frame.pack(fill="x")

        tk.Label(title_frame, text="PROMOTION", font=self.title_font, fg="black", bg="white").pack()
        tk.Label(title_frame, text="Choisir une promotion", font=self.subtitle_font, fg=self.highlight_color, bg="white").pack()

        # Scrollable promotions list
        container = Frame(self, bg="white")
        container.pack(expand=True, fill="both", padx=20, pady=10)

        canvas = Canvas(container, bg="white", highlightthickness=0)
        scrollbar = Scrollbar(container, orient="vertical", command=canvas.yview)
        scrollable_frame = Frame(canvas, bg="white")

        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        window = canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        # Fetch promotions
        promotions = get_promotions(connect_to_db())

        if not promotions:
            tk.Label(scrollable_frame, text="Aucune promotion disponible", font=self.subtitle_font, fg="red", bg="white").pack(pady=20)
            return

        for i, prom in enumerate(promotions):
            btn = tk.Button(
                scrollable_frame, text=prom[1], font=self.button_font, fg="white", bg=self.button_bg,
                width=25, height=2, bd=0, relief="flat",
                command=lambda p_id=prom[0], p_name=prom[1]: self.select_promotion(p_id, p_name)
            )
            btn.pack(pady=5, padx=10, fill="x")

            btn.bind("<Enter>", lambda e, b=btn: b.config(bg=self.button_hover_bg))
            btn.bind("<Leave>", lambda e, b=btn: b.config(bg=self.button_bg))

    def select_promotion(self, promotion_id, promotion_name):
        self.master.promotion_name = promotion_name
        self.master.promotion_id = promotion_id
        messagebox.showinfo("Promotion sélectionnée", f"Vous avez sélectionné {promotion_name}")
        self.master.liste_etudiant.update_promotion_info()
        self.master.transition(self.master.liste_etudiant)
