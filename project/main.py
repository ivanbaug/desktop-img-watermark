from PIL import Image, ImageFont, ImageDraw
from PIL.ImageQt import ImageQt

# Import QTDesigner UI
from wm_ui import Ui_Form

# Import Pyside UI modules
from PySide6.QtGui import QPixmap

from PySide6 import QtWidgets as qtw
from PySide6 import QtCore as qtc


from datetime import datetime as dt

from pathlib import Path


class MainWindow(qtw.QWidget):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.usr_img = Image.new("RGB", (100, 100))
        self.watermark_img = self.usr_img.copy()
        # In case there is no folder selected yet, get app directory
        self.file_path = self.dummy_filepath()

        # Setup button actions
        self.ui.btnDirectory.clicked.connect(self.get_image)
        self.ui.btnPreview.clicked.connect(self.preview_image)
        self.ui.btnSave.clicked.connect(self.save_watermark)

    def get_image(self):
        # Update placeholder text
        self.set_placeholder_txt("Loading image...")
        # Select and display img
        self.file_path = qtw.QFileDialog.getOpenFileName(
            self,
            "Select your image file",
            dir="/",
            filter="Image files (*.jpg *.png *.bmp *.jpeg)",
        )[0]
        if self.file_path == "":
            self.set_placeholder_txt("Remember:")
            self.file_path = self.dummy_filepath()
            self.usr_img = Image.new("RGB", (100, 100))
            return

        self.usr_img = Image.open(self.file_path)
        self.display_img(self.usr_img)

    def display_img(self, PIL_Image: Image):
        label_size = self.ui.imagePlaceholder.size()
        pix = QPixmap.fromImage(ImageQt(PIL_Image))
        scaled_pix = pix.scaled(label_size, qtc.Qt.KeepAspectRatio)
        self.ui.imagePlaceholder.setPixmap(scaled_pix)

    def preview_image(self):
        # Make a copy of the current image
        self.watermark_img = self.usr_img.copy()

        # Watermark Settings
        fillcolor = "white"
        shadowcolor = "#152238"
        width, height = self.watermark_img.size
        # 10% of the width, at least 1
        pointsize = int(width * 0.1) + 1
        # Origin in x and y relative to the current image
        x, y = pointsize, height - pointsize * 2

        # Get the watermark text
        wm_text = self.ui.textWatermark.text()

        # Edit using PIL
        draw = ImageDraw.Draw(self.watermark_img)
        #  ImageFont.truetype("font type",font size)
        font = ImageFont.truetype("arial.ttf", pointsize)
        # thin border
        draw.text((x - 1, y), wm_text, font=font, fill=shadowcolor)
        draw.text((x + 1, y), wm_text, font=font, fill=shadowcolor)
        draw.text((x, y - 1), wm_text, font=font, fill=shadowcolor)
        draw.text((x, y + 1), wm_text, font=font, fill=shadowcolor)

        # thicker border
        draw.text((x - 1, y - 1), wm_text, font=font, fill=shadowcolor)
        draw.text((x + 1, y - 1), wm_text, font=font, fill=shadowcolor)
        draw.text((x - 1, y + 1), wm_text, font=font, fill=shadowcolor)
        draw.text((x + 1, y + 1), wm_text, font=font, fill=shadowcolor)

        # now draw the text over it
        draw.text((x, y), wm_text, font=font, fill=fillcolor)

        self.display_img(self.watermark_img)

    def save_watermark(self):
        # Create file name and path
        mfile = Path(self.file_path)
        saving_time = dt.now().strftime("%Y%m%d-%H%M%S")
        new_name = f"{mfile.stem}-{saving_time}{mfile.suffix}"
        new_path = Path(mfile.parent).joinpath(new_name)

        # Save img
        self.watermark_img.save(new_path)

        # Message user
        mb = qtw.QMessageBox()
        mb.setIcon(mb.Icon.Information)
        mb.setText(
            f"Your watermarked image was sucessfully saved in the following directory:\n\n {new_path}"
        )
        mb.setWindowTitle("Image saved!")
        mb.exec()

    def dummy_filepath(self):
        return f"{qtc.QDir.currentPath()}/test.jpg"

    def set_placeholder_txt(self, msg):
        self.ui.imagePlaceholder.setText(
            qtc.QCoreApplication.translate(
                "Form",
                f"<html><head/><body><h3>{msg}</h3><p>1. Click on 'select image'</p><p>2. Add the text for watermark</p><p>3. Preview watermark</p><p>4. Save the new image</p></body></html>",
                None,
            )
        )


if __name__ == "__main__":

    app = qtw.QApplication([])
    widget = MainWindow()
    widget.show()

    with open("project/material-blue.qss", "r") as f:
        _style = f.read()
        app.setStyleSheet(_style)

    app.exec()
    # if not engine.rootObjects():
    #     sys.exit(-1)
    # sys.exit(app.exec_())
    # print(os.path.dirname(__file__))
