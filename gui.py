from PyQt6.QtWidgets import QApplication, QWidget
import sys


app = QApplication(sys.argv)

# Crea and show Qt widget (window)
#NOTE windows not shown by default
window = QWidget()
window.show()

app.exec()
