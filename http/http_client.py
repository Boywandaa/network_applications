# file: pyqt_http_client.py
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout
import socket

class HttpClientApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt5 HTTP Client")
        
        self.label = QLabel("Click to send request")
        self.button = QPushButton("Send HTTP GET")
        self.button.clicked.connect(self.send_request)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.button)
        self.setLayout(layout)

    def send_request(self):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect(('127.0.0.1', 8080))
            request = "GET / HTTP/1.1\r\nHost: localhost\r\nConnection: close\r\n\r\n"
            s.sendall(request.encode())
            response = b""
            while True:
                chunk = s.recv(4096)
                if not chunk:
                    break
                response += chunk
            s.close()
            body = response.split(b'\r\n\r\n', 1)[1]
            self.label.setText(body.decode())
        except Exception as e:
            self.label.setText(f"Error: {e}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = HttpClientApp()
    window.show()
    sys.exit(app.exec_())
