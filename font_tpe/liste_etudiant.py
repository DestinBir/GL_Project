import tkinter as tk
from tkinter import ttk
from tkinter import filedialog


class ListeEtudiant(tk.Frame):
    def __init__(self, master,text_promotion="BAC1", **kwargs):
        super().__init__(**kwargs)
        self.master = master
        self.TEXT_PROMOTION=text_promotion #nom de la promotion qui s'affichera sur la page.
        self.Contener()

    def fenetre_de_selection_de_fichier_xlsx(self):
    	chemin_fichier = filedialog.askopenfilename(
    			title="selectionner fiche étudiant",
    			filetypes=(("fichier excel","xlsx"), ("tous les fichier","*.*")))
    	if chemin_fichier:
    		print(chemin_fichier)
        
    def Contener(self):
    	menu = tk.Frame(self, width=300, height=self.winfo_screenheight())
    	menu.place(x=0,y=0)

    	font_title= tk.font.Font(family="Arial", size=25, weight="bold")
    	title = tk.Label(menu, text="Gest Notes",fg="Green", font=font_title)
    	title.place(relx=0.5,rely=0.05, anchor="center")


    	font_semestre= tk.font.Font(family="Arial", size=18, weight="bold")
    	semestre=tk.Label(menu, text="Semestre", fg="green",font=font_semestre)
    	semestre.place(relx=0.01,rely=0.1)

    	font_sem= tk.font.Font(family="Arial", size=14, weight="bold")
    	sem1 = tk.Button(menu, text="Sem 1", relief="flat", font=font_sem)
    	sem1.place(relx=0.15, rely=0.15)

    	font_sem= tk.font.Font(family="Arial", size=14, weight="bold")
    	sem2 = tk.Button(menu, text="Sem 2", relief="flat", font=font_sem)
    	sem2.place(relx=0.15, rely=0.205)

    	font_guide = tk.font.Font(family="Arial", size=18, weight="bold")
    	guide = tk.Label(menu, text="Guide d'utilisation",fg="green", font=font_guide)
    	guide.place(relx=0.01, rely=0.26)

    	ligne_verticale = tk.Frame(self, bg="black",width=1, height=self.winfo_screenheight())
    	ligne_verticale.place(x=300,y=0)

    	liste = tk.Frame(self,width=self.winfo_screenwidth()-301, height=self.winfo_screenheight())
    	
    	promotion=tk.Label(liste, text=self.TEXT_PROMOTION, bg=liste.cget("bg"), font=tk.font.Font(family="Arial", size=18, weight="bold"))
    	promotion.place(relx=0.,rely=0.05)

    	listeDesEtudiants=tk.Label(liste, text="LISTE DES ETUDIANTS", bg=liste.cget("bg"), font=tk.font.Font(family="Arial", size=18, weight="bold"))
    	listeDesEtudiants.place(relx=0.25,rely=0.05)


    	label_recherche = tk.Label(liste, text="Recherche", bg=liste.cget("bg"), font=tk.font.Font(family="Arial", size=13))
    	label_recherche.place(relx=0.61, rely=0.055)
    	recherche=tk.Entry(liste, bg=liste.cget("bg"), font=tk.font.Font(family="Arial", size=18, weight="bold"))
    	recherche.place(relx=0.7,rely=0.05)


    	frame_header_tableau = tk.Frame(liste, width=liste.winfo_screenwidth())
    	font_header_tableau=tk.font.Font(family="Arial", size=18)
    	num=tk.Label(frame_header_tableau, text="Matricule", bg=liste.cget("bg"), font=font_header_tableau)
    	frame_header_tableau.grid_columnconfigure(0,minsize=(frame_header_tableau.winfo_screenwidth()-301)*0.15)
    	num.grid(row=0, column=0, sticky="e")
    	nomPostnom=tk.Label(frame_header_tableau, text="Nom-Postnom", bg=liste.cget("bg"), font=font_header_tableau)
    	frame_header_tableau.grid_columnconfigure(1,minsize=(frame_header_tableau.winfo_screenwidth()-301)*0.35)
    	nomPostnom.grid(row=0, column=1, sticky="n")
    	sexe=tk.Label(frame_header_tableau, text="Sexe", bg=liste.cget("bg"), font=font_header_tableau)
    	frame_header_tableau.grid_columnconfigure(2,minsize=(frame_header_tableau.winfo_screenwidth()-301)*0.1)
    	sexe.grid(row=0, column=2, sticky="n")
    	date_nais=tk.Label(frame_header_tableau, text="Date de naissance", bg=liste.cget("bg"), font=font_header_tableau)
    	frame_header_tableau.grid_columnconfigure(3,minsize=(frame_header_tableau.winfo_screenwidth()-301)/5)
    	date_nais.grid(row=0, column=3, sticky="n")
    	lieu_nais=tk.Label(frame_header_tableau, text="Lieu de naissance", bg=liste.cget("bg"), font=font_header_tableau)
    	frame_header_tableau.grid_columnconfigure(4,minsize=(frame_header_tableau.winfo_screenwidth()-301)/5)
    	lieu_nais.grid(row=0, column=4, sticky="n")

    	frame_header_tableau.place(relx=0, rely=0.1)

    	btn_insert_student=tk.Button(liste, text="Ajouter les étudiant", command=self.fenetre_de_selection_de_fichier_xlsx)
    	btn_insert_student.place(relx=0.92,rely=0.88, anchor="center")


    	liste.place(x=301,y=0)