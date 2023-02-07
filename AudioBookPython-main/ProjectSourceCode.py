# Python audiobook project


from audio import *
from tkinter import *   # Importing the GUI named tkinter
from tkinter.filedialog import *
root = Tk()

def close_window():
    root.destroy()  # Destroying the main window


# Creating the tkinter window 

def main():
    root.configure(background='floral white')
    # set the title of GUI window
    root.title("Divya Barathi Audiobook")
    # set the configuration of GUI window
    # root.geometry("500x300")
    frame = Frame(root)
    frame.pack(fill=None, expand=False)
    Label(frame, text='Enter below Page Range Ex: 1-2', font=('Comic Sans MS', 10), background='floral white').pack()
    var = StringVar()
    entry = Entry(root, textvariable = var, font=('Comic Sans MS', 15))
    entry.pack()
    redbutton = Button(root, text="Browse and select the PDF file", font=('Comic Sans MS', 15), fg="blue", command=close_window)  # The window will get closed by the command
    redbutton.pack(side=TOP)

    photo = PhotoImage(file="milk-and-mocha-cute.gif")  # Creating a photoimage object to use image . JPEG wouldn't work here
    Button(root, image=photo).pack(side=TOP)  # Setting image in button
    root.mainloop()
    print(var.get(),"tets")
    pageRange = var.get()
    audio(pageRange, audiotab = Tk())
    
    



