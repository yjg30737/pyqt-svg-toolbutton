from PyQt5.QtWidgets import QToolButton, QWidget
from pyqt_svg_abstractbutton import SvgAbstractButton


class SvgToolButton(QToolButton, SvgAbstractButton):
    def __init__(self, base_widget: QWidget = None, *args, **kwargs):
        super().__init__(base_widget, *args, **kwargs)