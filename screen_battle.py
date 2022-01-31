import tkinter
from tkinter import *

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

        Label(self, text = "You", font = "24").grid(row = 0, column = 1)
        Label(self, text = "Computer", font = "24").grid(row = 0, column = 4)

        #User combatant
        imageSmall = tkinter.PhotoImage(file="images/" + self.player1.large_image)
        w = tkinter.Label (self,
                        image = imageSmall, 
                         )
        w.photo = imageSmall # saving the image as a property is required for "saving" the image. It's odd.
        w.grid(row = 1, column = 0, columnspan = 3, sticky = W)
        Label(self, text = f"{self.player1.hit_points}/{self.player1.hit_points} HP", font = "20").grid(row = 3, column = 1)

        #Computer Combatant
        imageSmall = tkinter.PhotoImage(file="images/" + self.player2.large_image)
        w = tkinter.Label (self,
                        image = imageSmall, 
                         )
        w.photo = imageSmall # saving the image as a property is required for "saving" the image. It's odd.
        w.grid(row = 1, column = 3, columnspan = 3, sticky = W) 
        Label(self, text = f"{self.player2.hit_points}/{self.player2.hit_points} HP", font = "20").grid(row = 3, column = 4)

        #attack button
        Button(self, text = "Attack!", command = self.attack_clicked).grid(row = 7, column = 2, columnspan =2)
        


        '''
        This method creates all of the (initial) widgets for the battle page.
        '''
        #
        # TO DO
        #
        
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
        #
        # TO DO
        #
                                            
    def exit_clicked(self):
        ''' This method is called when the Exit button is clicked. 
            It passes control back to the callback method. '''        
        self.callback_on_exit()
  
            
            
            
            