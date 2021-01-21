import webbrowser
import tkinter
from tkinter import *



#the GUI that lets you change the website text
class ParentWindow(Frame):
    def __init__ (self, master):
        Frame.__init__ (self)

        self.master = master
        self.master.resizable(width=False, height=False)
       
        self.master.title('Submit new website text')
        self.master.config(bg='lightgray')

        self.varWebTxt = StringVar()

        self.lblWebTxt = Label(self.master,text='New website text: ', font=("Helvetica", 16), fg='black', bg='lightgrey' )
        self.lblWebTxt.grid(row=0, column=0, padx=(30,0), pady=(30,0))

        self.lblDisplay = Label(self.master,text='', font=("Helvetica", 16), fg='black', bg='white')
        self.lblDisplay.grid(row=3, column=1,padx=(30,0), pady=(30,0))

        self.txtWebTxt = Entry(self.master,text=self.varWebTxt, font=("Helvetica", 16), fg='black', bg='lightblue')
        self.txtWebTxt.grid(row=0, column=1,padx=(30,0), pady=(30,0))
        
        self.btnSubmit = Button(self.master, text="Submit", width=10, height=2, command=self.submit)
        self.btnSubmit.grid(row=2, column=1,padx=(0,0), pady=(30,0), sticky=NE)

        self.btnCancel = Button(self.master, text="Cancel", width=10, height=2, command=self.cancel)
        self.btnCancel.grid(row=2, column=1,padx=(0,90), pady=(30,0), sticky=NE)

    def submit(self):
        fn = self.varWebTxt.get()
        
        f = open("webpage.html", "w")
        f.write(str(fn))
        f.close()
        f = open("webpage.html", "r")
        webbrowser.open_new_tab("webpage.html")

    def cancel(self):
        self.master.destroy()




if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()
