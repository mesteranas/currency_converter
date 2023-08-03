import sys
from custome_errors import *
sys.excepthook = my_excepthook
import google_currency
from webbrowser import open as openLink
import language
import app
import PyQt6.QtWidgets as qt
import PyQt6.QtGui as qt1
from PyQt6.QtCore import Qt
language.init_translation()
class main (qt.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle(app.name + _("version : ") + str(app.version))
        self.lang={}
        for code, name in google_currency.CODES.items():
            self.lang[name]=code
        self.text=qt.QDoubleSpinBox()
        self.text.setAccessibleName(_("value"))
        self.text.setRange(1.0,1000000000.0)
        self.From=qt.QComboBox()
        self.From.setAccessibleName(_("from"))
        self.From.addItems(self.lang.keys())
        self.to=qt.QComboBox()
        self.to.setAccessibleName(_("to"))
        self.to.addItems(self.lang.keys())
        self.translate=qt.QPushButton(_("convert"))
        self.translate.setDefault(True)
        self.translate.clicked.connect(self.ftranslate)
        self.re=qt.QTextEdit()
        self.re.setReadOnly(True)
        self.re.setAccessibleName(_("result"))
        layout=qt.QVBoxLayout()
        layout.addWidget(self.text)
        layout.addWidget(self.From)
        layout.addWidget(self.to)
        layout.addWidget(self.translate)
        layout.addWidget(self.re)
        w=qt.QWidget()
        w.setLayout(layout)
        self.setCentralWidget(w)
        mb=self.menuBar()
        help=mb.addMenu(_("help"))
        cus=help.addMenu(_("contact us"))
        telegram=qt1.QAction("telegram",self)
        cus.addAction(telegram)
        telegram.triggered.connect(lambda:openLink("https://t.me/mesteranasm"))
        telegramc=qt1.QAction(_("telegram channel"),self)
        cus.addAction(telegramc)
        telegramc.triggered.connect(lambda:openLink("https://t.me/tprogrammers"))
        donate=qt1.QAction(_("donate"),self)
        help.addAction(donate)
        donate.triggered.connect(lambda:openLink("https://www.paypal.me/AMohammed231"))
        about=qt1.QAction(_("about"),self)
        help.addAction(about)
        about.triggered.connect(lambda:qt.QMessageBox.information(self,_("about"),_("{} version: {} description: {} developer: {}").format(app.name,str(app.version),app.description,app.creater)))
        self.setMenuBar(mb)
    def ftranslate(self):
        try:
            a=google_currency.convert(self.lang[self.From.currentText()],self.lang[self.to.currentText()],self.text.value())
        except:
            a=_("error while converting")
        self.re.setText(a)
        self.re.setFocus()

App=qt.QApplication([])
w=main()
w.show()
App.exec()