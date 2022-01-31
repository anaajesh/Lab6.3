import tkinter
from tkinter import *
from characters import *

class Screen_CharacterSelection (tkinter.Frame, Character, CharacterRoster):

    def __init__ (self, master, roster, callback_on_selected):
        super().__init__(master)
       # Save the CharacterRoster  
        self.roster = roster
        # Save the method reference to which we return control after the player hits "Character Selected"
        self.callback_on_selected = callback_on_selected

        self.grid()
        self.create_widgets()
        
    def create_widgets (self):

        self.character_index = tkinter.StringVar()
        self.character_index.set(None)
        
        #title
        Label(self, text = "Hit Points").grid(row = 0, column = 2)
        Label(self, text = "Dexterity").grid(row = 0, column = 3)
        Label(self, text = "Strength").grid(row = 0, column = 4)

        #character stuff
        row_index = 1
        value_index = 0
        for character in self.roster.character_list:
            Radiobutton(self, text = character.name, variable = self.character_index, value = value_index
                       ).grid(row = row_index, column = 0, sticky = W)
            imageSmall = PhotoImage(file="images/" + character.small_image)
            w = Label (self,
                     image = imageSmall)
            w.photo = imageSmall # saving the image as a property is required for "saving" the image. It's odd.
            w.grid (row = row_index, column = 1, sticky = W)
            
            Label(self, text = f"{character.hit_points}").grid(row = row_index, column = 2)
            Label(self, text = f"{character.dexterity}").grid(row = row_index, column = 3)
            Label(self, text = f"{character.strength}").grid(row = row_index, column = 4)
            
            row_index += 1
            value_index += 1
            
        Button(self, text = "Select Character!!!", bg = "black", fg = "red", font=("Helvetica", 16), command = self.selected_clicked).grid(row = row_index, column = 6, sticky = W)
        '''
        This method creates all of the widgets character selector page.
        The information about each character should be derived from self.roster, 
        which is a CharacterRoster loaded from battle_characters.txt. 
        The layout should NOT be hard-coded: if you re-order, alter, or remove entries 
        in battle_characters.txt, the layout should automatically reflect those changes. 
        
        ########
        
        The radio buttons on this page should all use the variable "self.character_index_index".  
        The values of the radio buttons must be a number equally the position of the character in the list. 
        For example, if the characters listed are Troll, Elf, Human, and Dwarf.  self.character_index would equal 0 
        for the Troll, 1 for the Elf, and so forth.  
        
        The variable self.character_index has been instantiated for your convenience below.
        
        '''
       
 
    def selected_clicked(self):
        ''' This method is to be called when the "Character Selected!" button is clicked. 
            Notice that it passes self.character_index back to the callback method. '''         
        self.callback_on_selected(self.character_index.get())
