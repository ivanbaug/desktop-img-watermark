from tkinter import *

from tkinter import filedialog


def find_img():
    # Opens an explorer window to select an image file, then it returns the path of the selected image
    filename = filedialog.askopenfilename(
        initialdir="/",
        title="Select file",
        filetypes=[("image files", "*.jpg *.png *.bmp *.jpeg")],
    )
    print(filename)


window = Tk()
window.title("Password Manager")
# window.minsize(width=800,height=500)
window.config(padx=50, pady=50)


canvas = Canvas(width=200, height=200, highlightthickness=0)
# img = PhotoImage(file="exercises\\passwords\\logo.png")
# canvas.create_image(100, 100, image=img)
# timer_text = canvas.create_text(100,130, text="00:00",fill="white",font=(FONT_NAME,35,"bold"))
# canvas.grid(row=0, column=1)

button_sel_img = Button(text="Select image", command=find_img)

button_sel_img.grid(row=3, column=2, sticky="w")

window.mainloop()
