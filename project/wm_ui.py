# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'watermarks.ui'
##
## Created by: Qt User Interface Compiler version 6.2.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (
    QCoreApplication,
    QDate,
    QDateTime,
    QLocale,
    QMetaObject,
    QObject,
    QPoint,
    QRect,
    QSize,
    QTime,
    QUrl,
    Qt,
)
from PySide6.QtGui import (
    QBrush,
    QColor,
    QConicalGradient,
    QCursor,
    QFont,
    QFontDatabase,
    QGradient,
    QIcon,
    QImage,
    QKeySequence,
    QLinearGradient,
    QPainter,
    QPalette,
    QPixmap,
    QRadialGradient,
    QTransform,
)
from PySide6.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QLabel,
    QLayout,
    QLineEdit,
    QPushButton,
    QSizePolicy,
    QVBoxLayout,
    QWidget,
)


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(420, 594)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        self.verticalLayoutWidget = QWidget(Form)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(0, 0, 420, 594))

        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.btnDirectory = QPushButton(self.verticalLayoutWidget)
        self.btnDirectory.setObjectName(u"btnDirectory")

        self.verticalLayout.addWidget(self.btnDirectory)

        self.imagePlaceholder = QLabel(self.verticalLayoutWidget)
        self.imagePlaceholder.setObjectName(u"imagePlaceholder")
        self.imagePlaceholder.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.imagePlaceholder)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetMinimumSize)
        self.labelWatermarkText = QLabel(self.verticalLayoutWidget)
        self.labelWatermarkText.setObjectName(u"labelWatermarkText")

        self.horizontalLayout.addWidget(self.labelWatermarkText)

        self.textWatermark = QLineEdit(self.verticalLayoutWidget)
        self.textWatermark.setObjectName(u"textWatermark")

        self.horizontalLayout.addWidget(self.textWatermark)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.btnPreview = QPushButton(self.verticalLayoutWidget)
        self.btnPreview.setObjectName(u"btnPreview")

        self.verticalLayout.addWidget(self.btnPreview)

        self.btnSave = QPushButton(self.verticalLayoutWidget)
        self.btnSave.setObjectName(u"btnSave")

        self.verticalLayout.addWidget(self.btnSave)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)

    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(
            QCoreApplication.translate("Form", u"Watermark My Image", None)
        )
        self.btnDirectory.setText(
            QCoreApplication.translate("Form", u"Select image file", None)
        )
        self.imagePlaceholder.setText(
            QCoreApplication.translate(
                "Form",
                u"<html><head/><body><p>1. Click on 'select image'</p><p>2. Add the text for watermark</p><p>3. Preview watermark</p><p>4. Save the new image</p></body></html>",
                None,
            )
        )
        self.labelWatermarkText.setText(
            QCoreApplication.translate("Form", u"Your watermark:", None)
        )
        self.btnPreview.setText(
            QCoreApplication.translate("Form", u"Preview watermark", None)
        )
        self.btnSave.setText(
            QCoreApplication.translate("Form", u"Save watermarked image", None)
        )

    # retranslateUi
