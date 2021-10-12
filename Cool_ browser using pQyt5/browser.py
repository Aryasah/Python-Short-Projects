from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *


stack = ["http://google.com"]
class MyWebBrowser():

    def __init__(self):
        self.window = QWidget()
        self.window.setWindowTitle("My Web Browser")

        self.layout = QVBoxLayout()
        self.horizontal = QHBoxLayout()

        self.url_bar = QTextEdit()
        self.url_bar.setMaximumHeight(30)

        self.go_btn = QPushButton("Search")
        self.go_btn.setMinimumHeight(30)

        self.back_btn = QPushButton("Back")
        self.back_btn.setMinimumHeight(30)

        self.forward_btn = QPushButton("Next")
        self.forward_btn.setMinimumHeight(30)

        self.reset_btn = QPushButton("Reset")
        self.reset_btn.setMinimumHeight(30)
        
        
        self.horizontal.addWidget(self.url_bar)
        self.horizontal.addWidget(self.go_btn)
        self.horizontal.addWidget(self.back_btn)
        self.horizontal.addWidget(self.forward_btn)
        self.horizontal.addWidget(self.reset_btn)


        self.browser = QWebEngineView()
        self.go_btn.clicked.connect(lambda: self.navigate(self.url_bar.toPlainText()) )
        self.back_btn.clicked.connect(lambda: self.back())
        self.forward_btn.clicked.connect(self.browser.forward)
        self.reset_btn.clicked.connect(lambda: self.reset())
        self.layout.addLayout(self.horizontal)
        self.layout.addWidget(self.browser)

        self.browser.setUrl(QUrl("http://google.com"))
        self.window.setLayout(self.layout)
        self.window.show()

    def navigate(self,url):
        if not url.startswith("http"):
            url = "https://www.bing.com/search?q=" + url;
            self.url_bar.setText(url)
        stack.append(url)
        self.browser.setUrl(QUrl(url))
        
    def reset(self):
        self.url_bar.setText("")
        self.browser.setUrl(QUrl("http://google.com"))
    def back(self):
        history = stack.pop()
        self.url_bar.setText(history)
        self.browser.setUrl(QUrl(history))

        

app = QApplication([])
window = MyWebBrowser()
app.exec_()
print("Hello")

