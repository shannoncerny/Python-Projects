import tkinter as tk
from tkinter import *
import webbrowser

class ParentWindow(Frame):
    def __init__(self,master):
        Frame.__init__(self,master)
        self.master.title('Web Page Generator')

        # creates label for user input field
        self.label= Label(text='Enter custom text or click the Default HTML page button')
        self.label.grid(row=0,column=0,padx=(10,10),pady=(10,10),columnspan=3)

        # creates default HTML button
        self.btn = Button(self.master, text='Default HTML Page',width=30,height=2,command=self.defaultHTML)
        self.btn.grid(row=2,column=2,padx=(10,10),pady=(10,10))

        # creates submit custom text button
        self.btn = Button(self.master, text='Submit Custom Text',width=30,height=2,command=self.customText)
        self.btn.grid(row=2,column=3,padx=(10,10),pady=(10,10))

        # creates user input field
        self.custom_text = Entry(width=100)
        self.custom_text.grid(row=1,column=0,padx=(10,10),pady=(10,10),columnspan=3)


    # creates function that creates an html file and opens it on a web browser tab
    def defaultHTML(self):
        htmlText = 'Stay tuned for our amazing summer sale!'
        htmlFile = open('index.html','w')
        htmlContent = '<html>\n<body>\n<h1>' + htmlText + '</h1>\n</body>\n</html>'
        htmlFile.write(htmlContent)
        htmlFile.close()
        webbrowser.open_new_tab('index.html')

    # creates function that adds user inputed text to html file on the web browser
    def customText(self):
        htmlText = self.custom_text.get()
        htmlFile = open('index.html','w')
        htmlContent = '<html>\n<body>\n<h1>' + htmlText + '</h1>\n</body>\n</html>'
        htmlFile.write(htmlContent) # displays htmlcontent and user inputted text
        htmlFile.close()
        webbrowser.open_new_tab('index.html') # opens the web browser tab with html file loaded
        

if __name__ == '__main__':
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
    
