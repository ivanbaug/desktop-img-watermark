from PIL import Image
from PIL.ImageQt import ImageQt

# Import QTDesigner UI
from wm_ui import Ui_Form

# Import Pyside UI modules
from PySide6.QtGui import QImage, QPixmap
from PySide6.QtQml import QQmlApplicationEngine

from PySide6 import QtWidgets as qtw
from PySide6 import QtCore as qtc


class MainWindow(qtw.QWidget):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.usr_img = Image.new("RGB", (100, 100))

        # Setup button actions
        self.ui.btnDirectory.clicked.connect(self.get_image)
        self.ui.btnPreview.clicked.connect(self.get_image)
        self.ui.btnSave.clicked.connect(self.get_image)

    def get_image(self):

        self.ui.imagePlaceholder.setText(
            qtc.QCoreApplication.translate(
                "Form",
                u"<html><head/><body><h3>Loading Image ...</h3><p>1. Click on select image</p><p>2. Add the text for watermark</p><p>3. Preview watermark</p><p>4. Save the new image</p></body></html>",
                None,
            )
        )
        file_path = qtw.QFileDialog.getOpenFileName(
            self,
            "Select your image file",
            dir="/",
            filter="Image files (*.jpg *.png *.bmp *.jpeg)",
        )[0]

        self.display_img(Image.open(file_path))
        # label_size = self.ui.imagePlaceholder.size()
        # pix = QPixmap.fromImage(ImageQt())
        # scaled_pix = pix.scaled(label_size, qtc.Qt.KeepAspectRatio)
        # self.ui.imagePlaceholder.setPixmap(scaled_pix)

    def display_img(self, PIL_Image: Image):
        label_size = self.ui.imagePlaceholder.size()
        pix = QPixmap.fromImage(ImageQt(PIL_Image))
        scaled_pix = pix.scaled(label_size, qtc.Qt.KeepAspectRatio)
        self.ui.imagePlaceholder.setPixmap(scaled_pix)


# qImg = QtGui.QImage(
#     input_image.data, width, height, bytesPerLine, QtGui.QImage.Format_RGB888
# )
# def find_img():
#     # Opens an explorer window to select an image file, then it returns the path of the selected image
#     # filename = filedialog.askopenfilename(
#         initialdir="/",
#         title="Select file",
#         filetypes=[("image files", "*.jpg *.png *.bmp *.jpeg")],
#     )
#     print(filename)


# canvas = Canvas(width=500, height=500, highlightthickness=1, bg="white")
# # img = PhotoImage(file="exercises\\passwords\\logo.png")
# # canvas.create_image(100, 100, image=img)
# # timer_text = canvas.create_text(100,130, text="00:00",fill="white",font=(FONT_NAME,35,"bold"))
# canvas.grid(row=1, column=1)

# button_sel_img = Button(text="Select image", command=find_img)

# button_sel_img.grid(row=0, column=1)

# window.mainloop()

if __name__ == "__main__":

    app = qtw.QApplication([])
    widget = MainWindow()
    widget.show()

    with open("project/material-blue.qss", "r") as f:
        _style = f.read()
        app.setStyleSheet(_style)

    app.exec_()
    # if not engine.rootObjects():
    #     sys.exit(-1)
    # sys.exit(app.exec_())
    # print(os.path.dirname(__file__))
