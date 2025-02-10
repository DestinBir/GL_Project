import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import tkinter.font as tkFont
from functions import *  # Import des fonctions de gestion des étudiants

class ListeEtudiant(tk.Frame):
    def __init__(self, master, **kwargs):
        super().__init__(**kwargs)
        self.master = master

        self.TEXT_PROMOTION = self.master.promotion_name
        self.ID_PROMOTION = self.master.promotion_id
        self.subtitle_font = tkFont.Font(family="Arial", size=14, weight="bold")
        self.configure(bg="#2C2C2C")

        self.Contener()

    def update_promotion_info(self):
        """Met à jour les informations de la promotion sélectionnée"""
        self.TEXT_PROMOTION = self.master.promotion_name
        self.ID_PROMOTION = self.master.promotion_id
        self.label_promotion.config(text=f"Promotion : {self.TEXT_PROMOTION}")
        self.actualiser_liste()

    def fenetre_de_selection_de_fichier_xlsx(self):
        chemin_fichier = filedialog.askopenfilename(
            title="Sélectionner fiche étudiant",
            filetypes=(("Fichier Excel", "*.xlsx"), ("Tous les fichiers", "*.*"))
        )
        if chemin_fichier:
            etat = inscrire_etudiant_depuis_excel(chemin_fichier, connect_to_db(), self.ID_PROMOTION, "2024-2025", "Semestre 1")
            if etat: 
                messagebox.showinfo("Succès", "L'inscription des étudiants a été effectuée.")
                self.actualiser_liste()
            else:
                messagebox.showerror("Erreur", "Échec de l'inscription des étudiants.")
        else:
            messagebox.showwarning("Annulé", "Aucun fichier sélectionné.")

    def Contener(self):
        menu = tk.Frame(self, width=100, bg="#0A1F44")
        menu.place(x=0, y=0)

        title = tk.Label(menu, text="Gest Notes", fg="white", bg="#0A1F44", font=("Arial", 25, "bold"))
        title.place(relx=0.5, rely=0.05, anchor="center")

        ligne_verticale = tk.Frame(self, bg="black", width=2)
        ligne_verticale.place(x=100, y=0, relheight=1)

        liste = tk.Frame(self, bg="white")
        liste.place(x=101, y=0, relwidth=0.9, relheight=1)

        self.label_promotion = tk.Label(liste, text=f"Promotion : {self.TEXT_PROMOTION}", font=("Arial", 18, "bold"), bg="white")
        self.label_promotion.pack(pady=10)

        columns = ("Matricule", "Nom", "Postnom", "Sexe", "Lieu de naissance", "Date de naissance")
        self.tree = ttk.Treeview(liste, columns=columns, show="headings")
        for col in self.tree["columns"]:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=150)
        self.tree.pack(expand=True, fill="both", padx=10, pady=10)

        btn_insert_student = tk.Button(liste, text="Ajouter les étudiants", bg="orange", fg="white", font=self.subtitle_font, 
                                       command=self.fenetre_de_selection_de_fichier_xlsx)
        btn_insert_student.pack(pady=10)

        btn_back = tk.Button(self, text="Retour", font=self.subtitle_font, fg="white", bg="#2C2C2C", 
                             command=self.master.previous_screen)
        btn_back.pack(pady=10)

        self.update_promotion_info()

    def actualiser_liste(self):
        """Actualise la liste des étudiants affichée"""
        for item in self.tree.get_children():
            self.tree.delete(item)

        data = get_etudiant_by_promotion_per_semester(connect_to_db(), self.ID_PROMOTION, "Semestre 1")

        if data:
            for row in data:
                self.tree.insert("", "end", values=row)
        else:
            self.tree.insert("", "end", values=("Aucun étudiant", "", "", ""))








