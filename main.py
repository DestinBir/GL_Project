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

        self.current_screen = None
        self.screen_history = []  # Stack to track previous screens

        self.promotion_name = None
        self.promotion_id = None

        self.transition(self.login)

    def transition(self, screen):
        if self.current_screen:
            self.screen_history.append(self.current_screen)  # Save current screen before switching
            self.current_screen.pack_forget()
        self.current_screen = screen
        self.current_screen.pack(expand=True, fill="both")

    def previous_screen(self):
        if self.screen_history:
            self.current_screen.pack_forget()
            self.current_screen = self.screen_history.pop()
            self.current_screen.pack(expand=True, fill="both")

Application().mainloop()
