import pyttsx3
import PyPDF2
from tkinter import *   # Importing the GUI named tkinter
from tkinter.filedialog import *
from page_range import *
engine = pyttsx3.init()  # Object creation
audiotabclose = ''

def close_window_a():
    engine.stop()
    audiotabclose.destroy()


def audio(pageRange, audiotab):
    # Create a window
    audiotabclose = audiotab

    # Set Title as Image Loader
    audiotab.title("AudioBook")

    # Set the resolution of window
    audiotab.geometry("1000x600")
    audiotab.configure(bg = "#FFFFFF")
    canvas = Canvas(
        audiotab,
        bg = "#FFFFFF",
        height = 600,
        width = 1000,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge")
    canvas.place(x = 0, y = 0)

    background_img = PhotoImage(file = f"background 2.png")
    background = canvas.create_image(
        534.5, 310.5,
        image=background_img)

    img0 = PhotoImage(file = f"stop 2.png")
    b0 = Button(
        image = img0,
        borderwidth = 0,
        highlightthickness = 0,
        command = close_window_a,
        relief = "flat")

    b0.place(
        x = 386, y = 326,
        width = 249,
        height = 78)

    # Allow Window to be resizable
    
    frame = Frame(audiotab)
    frame.pack()
    
    

    # photo = PhotoImage(file="lisening.gif")  # Creating a photoimage object to use image . JPEG wouldn't work here
    # background_label = Label(audiotab, image=photo, text='Stop Audio')
    # background_label.place(x=0, y=35, relwidth=1, relheight=1)

    rate = engine.getProperty('rate')
    print (rate)  # Printing the current voice rate
    engine.setProperty('rate', 185)   # Setting up the new voice rate
    volume = engine.getProperty('volume')
    print (volume)  # Printing the current volume level
    engine.setProperty('volume',1.0)  # Setting up the volume level between 0 and 1
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    
    book=askopenfilename()
    pdfreader=PyPDF2.PdfFileReader(book)
    pages=pdfreader.numPages
    try:
        a , b = get_text(pageRange)
        for num in range(a, b):
            page=pdfreader.getPage(num)
            text=page.extractText()
            player=pyttsx3.init()
            player.say(text)
            player.runAndWait()
    except:
        for num in range(0,pages):
            page=pdfreader.getPage(num)
            text=page.extractText()
            player=pyttsx3.init()
            player.say(text)
            player.runAndWait()
    finally:
        engine.save_to_file(text, 'Audiobook created by Dolly.mp3')   # Saving the voice to a file 
        engine.runAndWait()
        print("Your audiobook file has been generated as an mp3 file. Check the project file directory for getting the file.")
    audiotab.mainloop()



    