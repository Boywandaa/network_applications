import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel, QHBoxLayout

from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl

class Browser(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("DevNet Web Browser")

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        # Search/URL Bar
        self.url_bar = QLineEdit()
        self.url_bar.setPlaceholderText("Enter page name (e.g., register)")
        self.url_bar.returnPressed.connect(self.load_page)

        self.browser = QWebEngineView()
        self.error_label = QLabel()
        self.google_button = QPushButton("Search on Google")
        self.google_button.clicked.connect(self.search_google)
        self.google_button.hide()

        top_bar = QHBoxLayout()
        top_bar.addWidget(QLabel("Search:"))
        top_bar.addWidget(self.url_bar)

        self.layout.addLayout(top_bar)
        self.layout.addWidget(self.browser)
        self.layout.addWidget(self.error_label)
        self.layout.addWidget(self.google_button)

        self.load_homepage()

    def load_homepage(self):
        self.browser.setUrl(QUrl("http://localhost:8085/"))

    def load_page(self):
        page = self.url_bar.text().strip()
        if not page:
            self.load_homepage()
        else:
            url = f"http://localhost:8085/{page}"
            self.browser.setUrl(QUrl(url))
            self.browser.loadFinished.connect(self.check_page_loaded)

    def check_page_loaded(self, ok):
        if not ok:
            self.error_label.setText("Page not found. Try searching it online.")
            self.google_button.show()
        else:
            self.error_label.setText("")
            self.google_button.hide()

    def search_google(self):
        query = self.url_bar.text()
        google_url = f"https://www.google.com/search?q={query}"
        self.browser.setUrl(QUrl(google_url))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    browser = Browser()
    browser.resize(900, 600)
    browser.show()
    sys.exit(app.exec_())
