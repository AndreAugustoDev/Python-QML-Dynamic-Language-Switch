import os
import sys

# IMPORT MODULES
from PySide6.QtCore import QObject, QTranslator, Signal, Slot
from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine


# Main Window Class
class MainWindow(QObject):
    def __init__(self):
        QObject.__init__(self)
        self.trans = QTranslator(self)
        engine.retranslate()

    @Slot(str)
    def switchLanguage(self, lang):
        if lang:
            self.trans.load('./locale/' + lang)
            app.installTranslator(self.trans)
            engine.retranslate()
        else:
            app.removeTranslator(self.trans)


# INSTACE CLASS
if __name__ == "__main__":
    app = QGuiApplication(sys.argv)
    engine = QQmlApplicationEngine()

    # Get Context
    main = MainWindow()
    engine.rootContext().setContextProperty("backend", main)

    # Load QML File
    engine.load(os.path.join(os.path.dirname(__file__), "main.qml"))

    # Check Exit App
    if not engine.rootObjects():
        sys.exit(-1)
    sys.exit(app.exec())
