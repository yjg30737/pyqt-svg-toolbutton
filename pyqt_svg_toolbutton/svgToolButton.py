from PyQt5.QtWidgets import QToolButton
from pyqt_svg_button import SvgButton


class SvgToolButton(QToolButton, SvgButton):
    def __init__(self):
        super().__init__()
        self.__initUi()