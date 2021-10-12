from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *
import sys
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('http://google.com'))
        self.setCentralWidget(self.browser)
        self.showMaximized()
        
        navbar = QToolBar()
        self.addToolBar(navbar)

        back_btn = QAction('Back',self)
        back_btn.triggered.connect(self.browser.back)
        navbar.addAction(back_btn)

        forward_btn = QAction('Forward',self)
        forward_btn.triggered.connect(self.browser.forward)
        navbar.addAction(forward_btn)

        reload_btn = QAction('Reload',self)
        reload_btn.triggered.connect(self.browser.reload)
        navbar.addAction(reload_btn)

        home_btn = QAction('Home',self)
        home_btn.triggered.connect(lambda: self.navigate_home('http://google.com'))
        navbar.addAction(home_btn)

        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate)
        navbar.addWidget(self.url_bar)
        self.browser.urlChanged.connect(self.update_url)

        search_btn = QAction('Search',self)
        search_btn.triggered.connect(self.navigate)
        navbar.addAction(search_btn)

        # go_btn = QPushButton("Search")
        # navbar.addAction(go_btn)

        # self.go_btn.clicked.connect(lambda: self.navigate_home(self.url_bar.toPlainText()) )

    def update_url(self,url):
        self.url_bar.setText(url.toString())

    def navigate_home(self,url):
        if not url.startswith("http"):
            url = "https://www.google.com/search?q=" + url;
        self.browser.setUrl(QUrl(url))
    
    def navigate(self):
        url = self.url_bar.text()
        if not url.startswith("http"):
            url = "https://www.google.com/search?q=" + url;
        else:
            if not url.endswith(".com"):
                url = url +".com";
        self.browser.setUrl(QUrl(url))

        
app = QApplication([])
QApplication.setApplicationDisplayName("My Browser")
window = MainWindow()
app.exec()
print("helo")