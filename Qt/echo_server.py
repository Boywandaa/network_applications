import sys
from PyQt5.QtWidgets import ( QApplication, QMainWindow ,QWidget,
                              QGridLayout, QHBoxLayout ,QGridLayout,
                              QLabel, QPushButton )

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700, 300, 500, 500)
        self.initUI()
        self.button = QPushButton()

    def initUI(self):
        #creating a widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        #creating a label
        label1 = QLabel("1")
        label2 = QLabel("2")
        label3 = QLabel("3")
        label4 = QLabel("4")

        #stying the labels
        label1.setStyleSheet("background-color: blue;")
        label2.setStyleSheet("background-color: green;")
        label3.setStyleSheet("background-color: black;")
        label4.setStyleSheet("background-color: red;")

        #creating a layout
        grid = QGridLayout()

        #adding widgets to the layout
        grid.addWidget(label1)
        grid.addWidget(label2, 0 ,1)
        grid.addWidget(label3, 1, 0)
        grid.addWidget(label4, 1, 1)

        #adding the layout to the centralwidget
        central_widget.setLayout(grid)


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()