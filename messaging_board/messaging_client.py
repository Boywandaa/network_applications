import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QTextEdit, QGridLayout
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtNetwork import QTcpSocket, QHostAddress


class Client(QWidget):
    def __init__(self):
        super().__init__()
        #LAYOUT OF THE APPLICATION
        #basic window styles
        self.setWindowTitle("Messaging Board CLient")
        self.setWindowIcon(QIcon("UnimaLogo.png"))
        self.resize(400, 300)
        self.initUI()

        # Initializing network object and variables
        self.socket = QTcpSocket(self)
        self.socket.connected.connect(self.on_connected)
        self.socket.disconnected.connect(self.on_disconnected)
        self.socket.readyRead.connect(self.receive_data)
        self.socket.error.connect(self.on_error)

        self.client_id = None


    def initUI(self):

        #layout
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        #first row configurations from the layout
        self.first_row = QHBoxLayout()
        self.address_input = QLineEdit()
        self.address_input.setPlaceholderText("Enter address")
        self.port_input = QLineEdit()
        self.port_input.setPlaceholderText("Enter port")
        self.connect_button = QPushButton("Connect")
        self.connect_button.setStyleSheet("background-color: green; color: white;")
        self.first_row.addWidget(self.address_input)
        self.first_row.addWidget(self.port_input) 
        self.first_row.addWidget(self.connect_button)  

        #seconod row configurations from the layout
        self.second_row = QHBoxLayout()
        self.message_input = QLineEdit()
        self.message_input.setPlaceholderText("Type your message here")
        self.message_input.setEnabled(False)
        self.send_button = QPushButton("Send")
        self.send_button.setStyleSheet("background-color: green; color: white;")
        self.send_button.setEnabled(False)
        self.second_row.addWidget(self.message_input)
        self.second_row.addWidget(self.send_button)

        #last row 
        self.output = QTextEdit()
        self.output.setReadOnly(True)

        #add widgets to the layout
        self.layout.addLayout(self.first_row)
        self.layout.addLayout(self.second_row)
        self.layout.addWidget(self.output)  

        #Buttons actions
        self.connect_button.clicked.connect(self.connect_to_server)
        self.send_button.clicked.connect(self.send_message)
        self.message_input.returnPressed.connect(self.send_message)
        
        #END OF LAYOUT CONFIGURATIONS

    def connect_to_server(self):
        address = self.address_input.text()
        port = self.port_input.text()

        if not address or not port.isdigit():
            self.log("Invalid address or port!")
            return
        
        port = int(port)
        self.log(f"Connecting to {address}:{port}...")
        self.socket.connectToHost(QHostAddress(address), port)

    def on_connected(self):
        self.log("Connected to server!")
        self.message_input.setEnabled(True)
        self.send_button.setEnabled(True)

    def on_disconnected(self):
        self.log("Disconnected from server")
        self.connect_button.setText("Connect")
        self.connect_button.setStyleSheet("background-color: green; color: white;")
        self.connect_button.clicked.disconnect()
        self.connect_button.clicked.connect(self.connect_to_server)
        
        # Disable message input
        self.message_input.setEnabled(False)
        self.send_button.setEnabled(False)

    def disconnect_from_server(self):
        self.socket.disconnectFromHost()

    def on_error(self, socket_error):
        error_message = self.socket.errorString()
        self.log(f"Error: {error_message}")

    def log(self, message):
        self.output.append(message)

    def send_message(self):
        if not self.message_input.text():
            return
        
        message = self.message_input.text()
        self.socket.write(message.encode())
        self.message_input.clear()
        self.message_input.setFocus()
        

    def receive_data(self):
        data = self.socket.readAll().data().decode()
        self.log(data)



def main():
    app = QApplication(sys.argv)
    client = Client()
    client.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()