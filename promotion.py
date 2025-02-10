import tkinter as tk
from tkinter import font

from functions import connect_to_db, get_promotions

class Promotion(tk.Frame):
	def __init__(self, master, **kwargs):
		super().__init__(**kwargs)
		self.master = master
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

		# Création des trois boutons BAC
		# self.create_bac_block(main_frame, "BAC 1")
		# self.create_bac_block(main_frame, "BAC 2")
		# self.create_bac_block(main_frame, "BAC 3")
  
		promotions = get_promotions(connect_to_db())
		for prom in promotions:
			self.create_bac_block(main_frame, prom[1])

	# Fonction pour ouvrir une nouvelle fenêtre
	def open_new_window(self,bac_title):
		new_window = tk.Toplevel(self)
		new_window.title(bac_title)
		new_window.geometry("500x300")

		label = tk.Label(new_window, text=f"Bienvenue dans la section {bac_title} !", font=self.subtitle_font, fg="black")
		label.pack(expand=True)
		button=tk.Button(new_window, text="selectionner")

	# Fonction pour créer un bloc BAC sous forme de bouton
	def create_bac_block(self,parent, title):
		button = tk.Button(parent, text=title + "\n\nEn savoir plus\nListe des étudiants...",
		                   font=self.subtitle_font, fg=self.text_color, bg=self.bg_color, wraplength=250,
		                   width=25, height=18, relief="raised", bd=3,
		                   command=lambda: self.master.transition(self.master.liste_etudiant))
		button.pack(side="left", expand=True, padx=10, pady=20)

	
