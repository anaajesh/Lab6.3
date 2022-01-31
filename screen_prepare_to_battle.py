import tkinter
from tkinter import *
from characters import *

class Screen_PrepareToBattle (tkinter.Frame, Character, CharacterRoster):
    def __init__ (self, master, player1, player2, callback_on_commence_battle):
        super().__init__(master)

        # Save player character object references
        self.player1 = player1
        self.player2 = player2
        
        # Save the method reference to which we return control after the player hits "Next"
        self.callback_on_commence_battle = callback_on_commence_battle
        
        self.create_widgets()
        self.grid()
            
    def create_widgets (self):

        #title
        Label(self, text = "You", font = "24").grid(row = 0, column = 1)
        Label(self, text = "Computer", font = "24").grid(row = 0, column = 4)

        #User combatant
        imageSmall = tkinter.PhotoImage(file="images/" + self.player1.large_image)
        w = tkinter.Label (self, image = imageSmall)
        w.photo = imageSmall # saving the image as a property is required for "saving" the image. It's odd.
        w.grid(row = 1, column = 0, columnspan = 3, sticky = W)
        
        Label(self, text = f"HP: {self.player1.hit_points}", font = "20").grid(row = 3, column = 1)
        Label(self, text = f"Dexterity: {self.player1.dexterity}", font = "20").grid(row = 4, column = 1)
        Label(self, text = f"Strength: {self.player1.strength}", font = "20").grid(row = 5, column = 1)

        #Computer combatant
        imageSmall = tkinter.PhotoImage(file="images/" + self.player2.large_image)
        w = tkinter.Label (self, image = imageSmall)
        w.photo = imageSmall # saving the image as a property is required for "saving" the image. It's odd.
        w.grid(row = 1, column = 3, columnspan = 3, sticky = W)
        
        Label(self, text = f"HP: {self.player2.hit_points}", font = "20").grid(row = 3, column = 4)
        Label(self, text = f"Dexterity: {self.player2.dexterity}", font = "20").grid(row = 4, column = 4)
        Label(self, text = f"Strength: {self.player2.strength}", font = "20").grid(row = 5, column = 4)

        #Next Page Button
        Label(self, text = "").grid(row = 6, column = 0)
        Button(self, text = "Commence Battle", command = self.commence_battle_clicked).grid(row = 7, column = 2, columnspan =2)

        '''
        This method creates all of the widgets the prepare to battle page.
        '''
 
    def commence_battle_clicked(self):
        ''' This method is called when the Battle button is clicked. 
            It passes control back to the callback method. '''         
        self.callback_on_commence_battle()
            