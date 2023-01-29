import tkinter as tk
from tkinter import *

class ParentWindow(Frame):
    def __init__(self,master):
        Frame.__init__(self)
        # set title of GUI window
        self.master.title('File Transfer')

        # creates button to select files from source directly
        self.sourceDir_btn = Button(text='Select Source',width=20)
        # positions source button in GUI using Tkinter grid()
        self.sourceDir_btn.grid(row=0,column=0,padx=(20,10),pady=(30,0))

        # creates entry for source directory selection
        self.source_dir = Entry(width=75)
        # positions entry in GUI using grid()
        self.source_dir.grid(row=0,column=1,padx=(20,10),pady=(30,0))

        # creates button to select destination of files from destination directory
        self.destDir_btn = Button(text='Select Destination',width=20)
        # positions destination button in GUI using Tkinter grid()
        self.destDir_btn.grid(row=1,column=0,padx=(20,10),pady=(15,10))

        # creates entry button for destination directory selection
        self.destination_dir = Entry(width=75)
        # positions entry in GUI using grid()
        self.destination_dir.grid(row=1,column=1,padx=(20,10),pady=(15,10))


if __name__ == '__main__':
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
