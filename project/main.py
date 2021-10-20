import sys
import os


from wm_ui import Ui_Form

# Import modules
from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine

from PySide6 import QtWidgets as qtw
from PySide6 import QtCore as qtc

from qt_material import apply_stylesheet


class MainWindow(qtw.QWidget):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.ui = Ui_Form()
        self.ui.setupUi(self)


# from tkinter import *

# # Tk, Canvas, Button
# from tkinter import filedialog


# def find_img():
#     # Opens an explorer window to select an image file, then it returns the path of the selected image
#     # filename = filedialog.askopenfilename(
#         initialdir="/",
#         title="Select file",
#         filetypes=[("image files", "*.jpg *.png *.bmp *.jpeg")],
#     )
#     print(filename)


# window = Tk()
# window.title("Image Watermark Program")
# # window.minsize(width=800,height=500)
# window.config(padx=50, pady=50)


# canvas = Canvas(width=500, height=500, highlightthickness=1, bg="white")
# # img = PhotoImage(file="exercises\\passwords\\logo.png")
# # canvas.create_image(100, 100, image=img)
# # timer_text = canvas.create_text(100,130, text="00:00",fill="white",font=(FONT_NAME,35,"bold"))
# canvas.grid(row=1, column=1)

# button_sel_img = Button(text="Select image", command=find_img)

# button_sel_img.grid(row=0, column=1)

# window.mainloop()

if __name__ == "__main__":
    # app = QGuiApplication(sys.argv)
    # engine = QQmlApplicationEngine()
    # print(os.path.join(os.path.dirname(__file__), "qml", "main.qml"))
    # engine.load("project\\qml\\main.qml")  # Relative dir since i'm in a venv

    app = qtw.QApplication([])
    widget = MainWindow()
    apply_stylesheet(app, theme="dark_cyan.xml")
    widget.show()

    app.exec_()
    # if not engine.rootObjects():
    #     sys.exit(-1)
    # sys.exit(app.exec_())
    # print(os.path.dirname(__file__))
