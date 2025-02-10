import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import tkinter.font as tkFont
from functions import *  # Import des fonctions de gestion des étudiants

class ListeEtudiant(tk.Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.master = master

        # Récupération des infos de promotion
        self.TEXT_PROMOTION = self.master.promotion_name
        self.ID_PROMOTION = self.master.promotion_id

        # Styles et couleurs
        self.bg_color = "#2C2C2C"
        self.sidebar_color = "#0A1F44"
        self.button_color = "#F28C28"
        self.button_hover_color = "#F4A261"
        self.text_color = "white"

        # Polices
        self.title_font = tkFont.Font(family="Arial", size=22, weight="bold")
        self.subtitle_font = tkFont.Font(family="Arial", size=14, weight="bold")

        self.configure(bg=self.bg_color)

        # Création de l'UI
        self.create_widgets()

    def create_widgets(self):
        """Crée les éléments de l'interface utilisateur"""

        # ----- MENU LATÉRAL -----
        menu = tk.Frame(self, width=120, bg=self.sidebar_color)
        menu.pack(side="left", fill="y")

        title = tk.Label(menu, text="Gest Notes", fg="white", bg=self.sidebar_color, font=("Arial", 22, "bold"))
        title.pack(pady=20)

        # Séparateur vertical
        ligne_verticale = tk.Frame(self, bg="black", width=2)
        ligne_verticale.pack(side="left", fill="y")

        # ----- CONTENU PRINCIPAL -----
        content = tk.Frame(self, bg="white")
        content.pack(expand=True, fill="both", padx=10, pady=10)

        # Label de la promotion
        self.label_promotion = tk.Label(content, text=f"Promotion : {self.TEXT_PROMOTION}",
                                        font=("Arial", 18, "bold"), bg="white", fg="#333")
        self.label_promotion.pack(pady=10)

        # Tableau des étudiants
        columns = ("Matricule", "Nom", "Postnom", "Sexe", "Lieu de naissance", "Date de naissance")
        self.tree = ttk.Treeview(content, columns=columns, show="headings", height=10)

        # Configuration des colonnes
        for col in columns:
            self.tree.heading(col, text=col, anchor="center")
            self.tree.column(col, width=150, anchor="center")

        self.tree.pack(expand=True, fill="both", padx=10, pady=10)

        # ----- BOUTONS -----
        button_frame = tk.Frame(content, bg="white")
        button_frame.pack(pady=10)

        btn_insert_student = tk.Button(button_frame, text="Ajouter les étudiants", font=self.subtitle_font,
                                       fg="white", bg=self.button_color, relief="flat", width=20, height=2,
                                       cursor="hand2", command=self.fenetre_de_selection_de_fichier_xlsx)
        btn_insert_student.pack(side="left", padx=10)

        btn_insert_student.bind("<Enter>", lambda e: btn_insert_student.config(bg=self.button_hover_color))
        btn_insert_student.bind("<Leave>", lambda e: btn_insert_student.config(bg=self.button_color))

        btn_back = tk.Button(button_frame, text="Retour", font=self.subtitle_font,
                             fg="white", bg=self.bg_color, relief="flat", width=15, height=2,
                             cursor="hand2", command=self.master.previous_screen)
        btn_back.pack(side="left", padx=10)

        btn_back.bind("<Enter>", lambda e: btn_back.config(bg="#444"))
        btn_back.bind("<Leave>", lambda e: btn_back.config(bg=self.bg_color))

        self.update_promotion_info()

    def update_promotion_info(self):
        """Met à jour les informations de la promotion sélectionnée"""
        self.TEXT_PROMOTION = self.master.promotion_name
        self.ID_PROMOTION = self.master.promotion_id
        self.label_promotion.config(text=f"Promotion : {self.TEXT_PROMOTION}")
        self.actualiser_liste()

    def fenetre_de_selection_de_fichier_xlsx(self):
        """Ouvre une boîte de dialogue pour sélectionner un fichier Excel et inscrire les étudiants"""
        chemin_fichier = filedialog.askopenfilename(
            title="Sélectionner fiche étudiant",
            filetypes=(("Fichier Excel", "*.xlsx"), ("Tous les fichiers", "*.*"))
        )
        if chemin_fichier:
            etat = inscrire_etudiant_depuis_excel(chemin_fichier, connect_to_db(),
                                                  self.ID_PROMOTION, "2024-2025", "Semestre 1")
            if etat:
                messagebox.showinfo("Succès", "L'inscription des étudiants a été effectuée.")
                self.actualiser_liste()
            else:
                messagebox.showerror("Erreur", "Échec de l'inscription des étudiants.")
        else:
            messagebox.showwarning("Annulé", "Aucun fichier sélectionné.")

    def actualiser_liste(self):
        """Actualise la liste des étudiants affichée"""
        for item in self.tree.get_children():
            self.tree.delete(item)

        data = get_etudiant_by_promotion_per_semester(connect_to_db(), self.ID_PROMOTION, "Semestre 1")

        if data:
            for row in data:
                self.tree.insert("", "end", values=row)
        else:
            self.tree.insert("", "end", values=("Aucun étudiant", "", "", "", "", ""))
