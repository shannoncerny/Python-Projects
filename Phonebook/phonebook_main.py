# Python Ver: 3.11.1
#
# Author: Shannon Cerny
#
# Purpose: Phonebook Demo. Demonstrating OOP, Tkinter GUI module,
#          using Tkinter Parent and Child relationships
#
# Tested OS: This code was written and tested to work with Windows 11.

from tkinter import messagebox
import tkinter as tk

# import other modules to access
import phonebook_gui
import phonebook_func

# Frame is the tkinter frame class that our own class will inherit from
class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        # define master frame configuration
        self.master = master
        self.master.minsize(500,300) #height and width
        self.master.maxsize(500,300)
        # this centerwindow method will center the app on the user's screen
        phonebook_func.center_window(self,500,300)
        self.master.title('The Tkinter Phonebook Demo')
        self.master.configure(bg='#F0F0F0')
        # this protocol method is a tkinter built-in method to catch if
        # the user clicks the upper corner, 'X' on Windows OS
        self.master.protocol('WM_DELETE_WINDOW', lambda: phonebook_func.ask_quit(self))
        arg = self.master

        # load in the GUI widgets from a separate module,
        # keeping the code comparmentalized and clutter free
        phonebook_gui.load_gui(self)



        if __name__ == '__main__':
            root = tk.Tk()
            App = ParentWindow(root)
            root.mainloop()
