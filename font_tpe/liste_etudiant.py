import tkinter as tk
from tkinter import ttk, filedialog
import tkinter.font as tkFont

import datetime

class ListeEtudiant(tk.Frame):
    def __init__(self, master, text_promotion="BAC1", **kwargs):
        super().__init__(master, **kwargs)
        self.master = master
        self.TEXT_PROMOTION = text_promotion
        self.configure(bg="#2C2C2C")  # Gris foncé
        self.Contener()
    
    def fenetre_de_selection_de_fichier_xlsx(self):
        chemin_fichier = filedialog.askopenfilename(
            title="Sélectionner fiche étudiant",
            filetypes=(("Fichier Excel", "*.xlsx"), ("Tous les fichiers", "*.*"))
        )
        if chemin_fichier:
            print(chemin_fichier)
    
    def Contener(self):
        menu = tk.Frame(self, width=300, height=self.winfo_screenheight(), bg="#0A1F44")  # Bleu de nuit
        menu.place(x=0, y=0)
        
        font_title = tkFont.Font(family="Arial", size=25, weight="bold")
        title = tk.Label(menu, text="Gest Notes", fg="white", bg="#0A1F44", font=font_title)
        title.place(relx=0.5, rely=0.05, anchor="center")
        
        font_semestre = tkFont.Font(family="Arial", size=18, weight="bold")
        semestre = tk.Label(menu, text="Semestre", fg="orange", bg="#0A1F44", font=font_semestre)
        semestre.place(relx=0.05, rely=0.1)
        
        font_sem = tkFont.Font(family="Arial", size=14, weight="bold")
        sem1 = tk.Button(menu, text="Sem 1", relief="flat", bg="white", fg="#0A1F44", font=font_sem)
        sem1.place(relx=0.15, rely=0.15)
        
        sem2 = tk.Button(menu, text="Sem 2", relief="flat", bg="white", fg="#0A1F44", font=font_sem)
        sem2.place(relx=0.15, rely=0.205)
        
        font_guide = tkFont.Font(family="Arial", size=18, weight="bold")
        guide = tk.Label(menu, text="Guide d'utilisation", fg="orange", bg="#0A1F44", font=font_guide)
        guide.place(relx=0.05, rely=0.3)
        
        ligne_verticale = tk.Frame(self, bg="black", width=2, height=self.winfo_screenheight())
        ligne_verticale.place(x=300, y=0)
        
        liste = tk.Frame(self, width=self.winfo_screenwidth() - 301, height=self.winfo_screenheight(), bg="white")
        liste.place(x=301, y=0)
        
        columns = ("Matricule", "Nom", "Postnom", "Sexe", "Lieu de naissance", "Date de naissance")
        tree = ttk.Treeview(liste, columns=columns, show="headings")
        
        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, width=150)
        
        data = [
            ('UK-Ljfdkle01', 'Bahati', 'Jeoge', 'M', 'Bukavu', datetime.date(2012, 12, 12)),
            ('UK-Ljfdkle02', 'Bahati', 'Jeoge', 'M', 'Bukavu', datetime.date(2012, 12, 13)),
            ('UK-Ljfdkle03', 'Bahati', 'Jeoge', 'M', 'Bukavu', datetime.date(2012, 12, 14)),
            ('UK-Ljfdkle04', 'Bahati', 'Jeoge', 'M', 'Bukavu', datetime.date(2012, 12, 15)),
            ('UK-Ljfdkle05', 'Bahati', 'Jeoge', 'M', 'Bukavu', datetime.date(2012, 12, 16))
        ]
        
        for row in data:
            tree.insert("", "end", values=row)
        
        tree.place(relx=0.05, rely=0.2, relwidth=0.9, relheight=0.6)
        
        btn_insert_student = tk.Button(liste, text="Ajouter les étudiants", bg="orange", fg="white", font=font_sem, 
                                       command=self.fenetre_de_selection_de_fichier_xlsx)
        btn_insert_student.place(relx=0.5, rely=0.85, anchor="center")

"""if __name__ == "__main__":
    root = tk.Tk()
    root.title("Gestion des Étudiants")
    root.geometry(f"{root.winfo_screenwidth()}x{root.winfo_screenheight()}")
    app = ListeEtudiant(root)
    app.pack(fill="both", expand=True)
    root.mainloop()"""
