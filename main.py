import tkinter as tk


from login import Login
from promotion import Promotion
from liste_etudiant import ListeEtudiant



class Application(tk.Tk):
	# Création de la fenêtre principale
	def __init__(self):
		super().__init__()
		self.state("zoomed")
		self.title("GEST NOTES")
		self.configure(bg="white")

		
		self.login = Login(self)
		self.promotion = Promotion(self)
		self.liste_etudiant = ListeEtudiant(self)
		self.curent_screen = None
		self.transition(self.promotion)


	def transition(self,screen):
		if self.curent_screen:
			self.curent_screen.pack_forget()
		self.curent_screen=screen
		self.curent_screen.pack(expand=True, fill="both")
		


Application().mainloop()