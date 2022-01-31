import tkinter
from tkinter import *
import random

class Screen_Battle (tkinter.Frame):
    def __init__ (self, master, player1, player2, callback_on_exit):
        super().__init__(master)

        # Save references to the two player objects
        self.player1 = player1
        self.player2 = player2

        # Store the maximum number of hit points which are needed on the screen display.
        self.player1_max_hp = player1.hit_points
        self.player2_max_hp = player2.hit_points

        # Save the method reference to which we return control after this page Exits.
        self.callback_on_exit = callback_on_exit

        self.create_widgets()
        self.grid()
        
    def create_widgets (self):

        self.attack_messages = Label(self, text = "", font = "16")
        self.attack_messages.grid(row = 0, column = 4, columnspan = 2)
        self.winner_message = Label(self, text = "", fg = "red", font = "16")
        self.winner_message.grid(row = 2, column = 4)

        Label(self, text = "You", font = "24").grid(row = 3, column = 0)
        Label(self, text = "Computer", font = "24").grid(row = 3, column = 4)

        #User combatant
        imageSmall = tkinter.PhotoImage(file="images/" + self.player1.large_image)
        w = tkinter.Label (self, image = imageSmall)
        w.photo = imageSmall # saving the image as a property is required for "saving" the image. It's odd.
        w.grid(row = 4, column = 0, columnspan = 3, sticky = W)
        self.p1_fullhp = self.player1.hit_points
        self.player_hp = Label(self, text = f"{self.player1.hit_points}/{self.p1_fullhp} HP", font = "20")
        self.player_hp.grid(row = 5, column = 0)

        #Computer Combatant
        imageSmall = tkinter.PhotoImage(file="images/" + self.player2.large_image)
        w = tkinter.Label (self, image = imageSmall)
        w.photo = imageSmall # saving the image as a property is required for "saving" the image. It's odd.
        w.grid(row = 4, column = 4, columnspan = 3, sticky = W) 
        self.p2_fullhp = self.player2.hit_points
        self.computer_hp = Label(self, text = f"{self.player2.hit_points}/{self.p2_fullhp} HP", font = "20")
        self.computer_hp.grid(row = 5, column = 4)

        #attack button
        self.attack_button = Button(self, text = "Attack!", command = self.attack_clicked)
        self.attack_button.grid(row = 7, column = 2, columnspan =2)
        
        '''
        This method creates all of the (initial) widgets for the battle page.
        '''
        
    def attack_clicked(self):

        ''' This method is called when the user presses the "Attack" button.
            
            This method does the following:
            1) Calls the character.attack method for both the player and (if still alive) the computer.
            2) Updates the labels on the top right with the results of the attacks.
            3) Determines if there was a victor, and if so display that info 
            4) If there is a victor, remove the Attack button.  Create an Exit button to replace it.  

            To remove a widget, use the destroy() method. For example:
    
                self.button.destroy()
        '''

        if self.player1.hit_points > 0 and self.player2.hit_points > 0:

            self.attack_messages["text"] = self.player2.attack(self.player1)

            if self.player2.hit_points > 0:
                self.attack_messages["text"] += "\n" + self.player1.attack(self.player2)

            self.player_hp["text"] = f"{self.player1.hit_points}/{self.p1_fullhp} HP"
            self.computer_hp["text"] = f"{self.player2.hit_points}/{self.p2_fullhp} HP"

        if self.player2.hit_points <= 0:
            self.winner_message["text"] = f"{self.player1.name} is victorious!"
            self.attack_button.destroy()
            Button(self, text = "Exit!", command = self.exit_clicked, bg = "black", fg = "red", font = "24").grid(row = 7, column = 6)
        elif self.player1.hit_points <= 0:
            self.winner_message["text"] = f"{self.player2.name} is victorious!"
            self.attack_button.destroy()
            Button(self, text = "Exit!", command = self.exit_clicked, bg = "black", fg = "red", font = "24").grid(row = 7, column = 6)

    def exit_clicked(self):
        ''' This method is called when the Exit button is clicked. 
            It passes control back to the callback method. '''        
        self.callback_on_exit()
