from audio import *
from tkinter import *
from tkinter import filedialog
window = Tk()

def close_window():
    window.destroy()


def main():
    window.title("AudioBook")
    window.geometry("1000x600")
    window.configure(bg = "#FFFFFF")
    canvas = Canvas(
        window,
        bg = "#FFFFFF",
        height = 600,
        width = 1000,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge")
    canvas.place(x = 0, y = 0)

    background_img = PhotoImage(file = f"background.png")
    background = canvas.create_image(
        516.5, 331.5,
        image=background_img)

    img0 = PhotoImage(file = f"img0.png")
    b0 = Button(window,
        image = img0,
        borderwidth = 0,
        highlightthickness = 0,
        command =close_window,
        relief = "flat")

    b0.place(
        x = 689, y = 316,
        width = 193,
        height = 46)


    entry0_img = PhotoImage(file = f"img_textBox0.png")
    entry0_bg = canvas.create_image(
        775.5, 270.0,
        image = entry0_img)
    var=StringVar()
    entry0 = Entry(window,
        bd = 0,
        bg = "#e2d9d9",
        highlightthickness = 0,
        textvariable = var, font=('Comic Sans MS', 15))
    entry0.pack()

    entry0.place(
        x = 620, y = 243,
        width = 311,
        height = 52)

    window.resizable(False, False)
    window.mainloop()
    print(var.get(),'tets')
    pageRange=var.get()
    audio(pageRange, audiotab = Tk())

if __name__ == '__main__':
    main()
