"""MainPage.py: Setup for the homepage GUI for the main file """

__author__ = "BenX13"
__copyright__ = "Copyright 2019, For educational purposes"
__license__ = "MIT"
__version__ = "1.0"
__email__ = "ahmed.sif.benmessaoud.13@gmail.com"



import sys
import re
from main import translate
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.uic import loadUi


class MainPage(QDialog):
    def __init__(self):
        super(MainPage, self).__init__()
        loadUi('homepage.ui', self)

        self.pushButton_3.clicked.connect(self.retriveText1)
        self.pushButton.clicked.connect(self.retriveText2)

    def retriveText1(self):
        rna = self.plainTextEdit.toPlainText()
        translator = translate(rna)
        rna = translator.get_rna()
        percentage = round(translator.get_cgpercent(), 3)
        self.textEdit.setText(rna)
        self.textEdit_3.setText(str(percentage) + '%')
        self.textEdit_4.setText(str(100 - percentage) + '%')

    def retriveText2(self):
        protien = self.plainTextEdit.toPlainText()
        translator = translate(protien)
        protien = translator.get_protien()
        protien = "\n-".join(protien)
        self.textEdit_2.setText(protien)

app = QApplication(sys.argv)
widget = MainPage()
widget.show()
sys.exit(app.exec_())

