import sys
import requests
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout

class HttpClient(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("HTTP Client GUI")
        self.label = QLabel("Click to GET from server")
        self.button = QPushButton("Send GET Request")
        self.button.clicked.connect(self.send_request)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.button)
        self.setLayout(layout)

    def send_request(self):
        try:
            res = requests.get("http://127.0.0.1:8080")
            self.label.setText(res.json().get("message", "No message"))
        except Exception as e:
            self.label.setText(f"Error: {e}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = HttpClient()
    window.show()
    sys.exit(app.exec_())
