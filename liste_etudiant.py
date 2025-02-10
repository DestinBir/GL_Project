import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import tkinter.font as tkFont
from functions import *  # Import your function file

class ListeEtudiant(tk.Frame):

    def __init__(self, master, text_promotion="BAC1", **kwargs):
        super().__init__(master, **kwargs)
        self.master = master
        self.TEXT_PROMOTION = self.master.promotion_name
        self.subtitle_font = tkFont.Font(family="Arial", size=14, weight="bold")
        self.configure(bg="#2C2C2C")  # Gris foncé
        self.Contener()

    def fenetre_de_selection_de_fichier_xlsx(self):
        chemin_fichier = filedialog.askopenfilename(
            title="Sélectionner fiche étudiant",
            filetypes=(("Fichier Excel", "*.xlsx"), ("Tous les fichiers", "*.*"))
        )
        if chemin_fichier:
            etat = inscrire_etudiant_depuis_excel(chemin_fichier, connect_to_db(), self.master.promotion_id, "2024-2025", "Semestre 1")
            if etat: 
                messagebox.showinfo("Success", "L'inscription des étudiants a été faite")
        else:
            messagebox.showerror("Erreur", "L'inscription n'a pas été faite.")

    def Contener(self):
        menu = tk.Frame(self, width=300, height=self.winfo_screenheight(), bg="#0A1F44")  # Bleu de nuit
        menu.place(x=0, y=0)

        font_title = tkFont.Font(family="Arial", size=25, weight="bold")
        title = tk.Label(menu, text="Gest Notes", fg="white", bg="#0A1F44", font=font_title)
        title.place(relx=0.5, rely=0.05, anchor="center")

        font_semestre = tkFont.Font(family="Arial", size=18, weight="bold")
        semestre = tk.Label(menu, text="Semestre", fg="orange", bg="#0A1F44", font=font_semestre)
        semestre.place(relx=0.05, rely=0.1)

        # Button for "Sem 1" and "Sem 2" (This can be dynamically set later based on your data)
        sem1 = tk.Button(menu, text="Sem 1", relief="flat", bg="white", fg="#0A1F44", font=font_semestre)
        sem1.place(relx=0.15, rely=0.15)

        sem2 = tk.Button(menu, text="Sem 2", relief="flat", bg="white", fg="#0A1F44", font=font_semestre)
        sem2.place(relx=0.15, rely=0.205)

        guide = tk.Label(menu, text="Guide d'utilisation", fg="orange", bg="#0A1F44", font=font_semestre)
        guide.place(relx=0.05, rely=0.3)

        ligne_verticale = tk.Frame(self, bg="black", width=2, height=self.winfo_screenheight())
        ligne_verticale.place(x=300, y=0)

        liste = tk.Frame(self, width=self.winfo_screenwidth() - 301, height=self.winfo_screenheight(), bg="white")
        liste.place(x=301, y=0)

        promotion = tk.Label(liste, text=self.TEXT_PROMOTION, bg="white", fg="#0A1F44", font=font_semestre)
        promotion.place(relx=0.05, rely=0.05)

        listeDesEtudiants = tk.Label(liste, text="LISTE DES ETUDIANTS", bg="white", fg="black", font=font_semestre)
        listeDesEtudiants.place(relx=0.25, rely=0.05)

        # Search field and button
        label_recherche = tk.Label(liste, text="Recherche", bg="white", font=tkFont.Font(family="Arial", size=13))
        label_recherche.place(relx=0.61, rely=0.055)
        recherche = tk.Entry(liste, font=tkFont.Font(family="Arial", size=12))
        recherche.place(relx=0.7, rely=0.05, width=200)

        btn_actualiser = tk.Button(liste, text="Actualiser", bg="orange", fg="white", font=self.subtitle_font, command=self.actualiser_liste)
        btn_actualiser.place(relx=0.9, rely=0.05)

        # Treeview for students
        frame_header_tableau = tk.Frame(liste, bg="white")
        frame_header_tableau.place(relx=0, rely=0.1, relwidth=1)

        columns = ("Matricule", "Nom", "Postnom", "Sexe", "Lieu de naissance", "Date de naissance")    
        self.tree = ttk.Treeview(liste, columns=columns, show="headings")

        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=150)

        # Data fetching function call
        data = get_etudiant_by_promotion_per_semester(connect_to_db(), self.master.promotion_id, "Semestre 1")

        if data:  # Check if there is data
            for row in data:
                self.tree.insert("", "end", values=row)
        else:
            self.tree.insert("", "end", values=("Aucun étudiant",) * len(columns))  # Empty data message

        self.tree.place(relx=0.05, rely=0.2, relwidth=0.9, relheight=0.6)

        btn_insert_student = tk.Button(liste, text="Ajouter les étudiants", bg="orange", fg="white", font=self.subtitle_font, 
                                       command=self.fenetre_de_selection_de_fichier_xlsx)
        btn_insert_student.place(relx=0.5, rely=0.88, anchor="center")

        return_button = tk.Button(self, text="Retour", font=self.subtitle_font, fg="white", bg="#2C2C2C", 
                                  command=self.master.previous_screen)
        return_button.place(relx=0.5, rely=0.91, anchor="center")

    def actualiser_liste(self):
        """Actualise la liste des étudiants affichée dans le tableau"""
        if hasattr(self, 'tree'):
            for item in self.tree.get_children():
                self.tree.delete(item)

            data = get_etudiant_by_promotion_per_semester(connect_to_db(), self.master.promotion_id, "Semestre 1")

            if data:  # Check if there is data
                for row in data:
                    self.tree.insert("", "end", values=row)
            else:
                self.tree.insert("", "end", values=("Aucun étudiant",) * len(self.tree["columns"]))
