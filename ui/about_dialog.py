import os
import sys
from PyQt6.QtWidgets import QDialog, QVBoxLayout, QTextBrowser

def get_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

class AboutDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("О программе")
        self.resize(600, 500)

        layout = QVBoxLayout(self)

        self.viewer = QTextBrowser()
        layout.addWidget(self.viewer)

        html_path = get_path("ui/html files/about.html")

        try:
            with open(html_path, "r", encoding="utf-8") as f:
                self.viewer.setHtml(f.read())
        except:
            self.viewer.setHtml("<h1>Ошибка загрузки файла about.html</h1>")