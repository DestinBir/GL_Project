import tkinter as tk
from login import Login
from promotion import Promotion
from liste_etudiant import ListeEtudiant

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.state("zoomed")
        self.title("GEST NOTES")
        self.configure(bg="white")

        # Ajout du logo UCB
        self.iconphoto(False, tk.PhotoImage(file="ucb.png"))

        # Variables de promotion
        self.promotion_name = "Aucune promotion sélectionnée"
        self.promotion_id = None

        # Initialisation des écrans
        self.login = Login(self)
        self.promotion = Promotion(self)
        self.liste_etudiant = ListeEtudiant(self)

        self.current_screen = None
        self.screen_history = []

        self.transition(self.login)

    def transition(self, screen):
        """Permet de naviguer entre les écrans"""
        if self.current_screen:
            self.screen_history.append(self.current_screen)
            self.current_screen.pack_forget()
        self.current_screen = screen
        self.current_screen.pack(expand=True, fill="both")

    def previous_screen(self):
        """Retour à l'écran précédent"""
        if self.screen_history:
            self.current_screen.pack_forget()
            self.current_screen = self.screen_history.pop()
            self.current_screen.pack(expand=True, fill="both")

Application().mainloop()
