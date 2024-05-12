#!/usr/bin/env python3

import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QHBoxLayout, QVBoxLayout
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QAction, QColor
import PyQt6.QtGui


app = QApplication(sys.argv)
app.setQuitOnLastWindowClosed(True)

BasePath = '/Applications/Walnut.app/Contents/Resources/'
# BasePath = ''  # test

class window_alarm(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint | Qt.WindowType.WindowStaysOnTopHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground, True)

        self.screen_width = app.primaryScreen().geometry().width()
        self.screen_height = app.primaryScreen().geometry().height()
        self.setFixedSize(self.screen_width, self.screen_height)

        self.l1 = QLabel(self)
        png = PyQt6.QtGui.QPixmap(BasePath + 'walnut.png')  # 调用QtGui.QPixmap方法，打开一个图片，存放在变量png中
        self.l1.setPixmap(png)  # 在l1里面，调用setPixmap命令，建立一个图像存放框，并将之前的图像png存放在这个框框里。
        self.l1.setMaximumWidth(200)
        self.l1.setMaximumHeight(200)
        self.l1.setScaledContents(True)

        self.lbl0 = QLabel('Walnut', self)
        font = PyQt6.QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setPointSize(35)
        self.lbl0.setFont(font)

        self.lbl1 = QLabel('Earthquake is happening!!!', self)
        font = PyQt6.QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setPointSize(30)
        self.lbl1.setFont(font)

        self.btn_1 = QPushButton("Take cover immediately!", self)
        self.btn_1.clicked.connect(self.theme_input)
        self.btn_1.setFixedSize(250, 20)

        qw0 = QWidget()
        vbox0 = QHBoxLayout()
        vbox0.setContentsMargins(0, 0, 0, 0)
        vbox0.addStretch()
        vbox0.addWidget(self.l1)
        vbox0.addStretch()
        qw0.setLayout(vbox0)

        qw6 = QWidget()
        vbox6 = QHBoxLayout()
        vbox6.setContentsMargins(0, 0, 0, 0)
        vbox6.addStretch()
        vbox6.addWidget(self.lbl0)
        vbox6.addStretch()
        qw6.setLayout(vbox6)

        qw1 = QWidget()
        vbox1 = QHBoxLayout()
        vbox1.setContentsMargins(0, 0, 0, 0)
        vbox1.addStretch()
        vbox1.addWidget(self.lbl1)
        vbox1.addStretch()
        qw1.setLayout(vbox1)

        qw3 = QWidget()
        vbox3 = QHBoxLayout()
        vbox3.setContentsMargins(0, 0, 0, 0)
        vbox3.addStretch()
        vbox3.addWidget(self.btn_1)
        vbox3.addStretch()
        qw3.setLayout(vbox3)

        qw4 = QWidget()
        qw4.setFixedHeight(30)

        qw7 = QWidget()
        qw7.setFixedHeight(30)

        qwx = QWidget()
        vboxx = QVBoxLayout()
        vboxx.setContentsMargins(0, 0, 0, 0)
        vboxx.addStretch()
        vboxx.addWidget(qw0)
        vboxx.addWidget(qw4)
        vboxx.addWidget(qw6)
        vboxx.addWidget(qw1)
        vboxx.addWidget(qw7)
        vboxx.addWidget(qw3)
        vboxx.addStretch()
        qwx.setLayout(vboxx)
        qwx.setObjectName('Main')

        vboxn = QHBoxLayout()
        vboxn.setContentsMargins(0, 0, 0, 0)
        vboxn.addWidget(qwx)
        self.setLayout(vboxn)

        self.show()

    def theme_input(self):
        self.close()
        sys.exit(0)


style_sheet_theme = '''
	QTabWidget::pane {
		border: 1px solid #ECECEC;
		background: #ECECEC;
		border-radius: 9px;
}
	QTableWidget{
		border: 1px solid grey;  
		border-radius:4px;
		background-clip: border;
		background-color: #FFFFFF;
		color: #000000;
		font: 14pt Helvetica;
}
	QWidget#Main {
		background: rgba(255, 255, 255, 0.7);
}
	QPushButton{
		border: 1px outset grey;
		background-color: #FFFFFF;
		border-radius: 4px;
		padding: 1px;
		color: #000000
}
	QPushButton:pressed{
		border: 1px outset grey;
		background-color: #0085FF;
		border-radius: 4px;
		padding: 1px;
		color: #FFFFFF
}
	QPlainTextEdit{
		border: 1px solid grey;  
		border-radius:4px;
		padding: 1px 5px 1px 3px; 
		background-clip: border;
		background-color: #F3F2EE;
		color: #000000;
		font: 14pt Times New Roman;
}
	QPlainTextEdit#edit{
		border: 1px solid grey;  
		border-radius:4px;
		padding: 1px 5px 1px 3px; 
		background-clip: border;
		background-color: #FFFFFF;
		color: rgb(113, 113, 113);
		font: 14pt Helvetica;
}
	QTableWidget#small{
		border: 1px solid grey;  
		border-radius:4px;
		background-clip: border;
		background-color: #F3F2EE;
		color: #000000;
		font: 14pt Times New Roman;
}
	QLineEdit{
		border-radius:4px;
		border: 1px solid gray;
		background-color: #FFFFFF;
}
	QTextEdit{
		border: 1px solid grey;  
		border-radius:4px;
		padding: 1px 5px 1px 3px; 
		background-clip: border;
		background-color: #F3F2EE;
		color: #000000;
		font: 14pt Times New Roman;
}
	QListWidget{
		border: 1px solid grey;  
		border-radius:4px;
		padding: 1px 5px 1px 3px; 
		background-clip: border;
		background-color: #F3F2EE;
		color: #000000;
		font: 14pt Times New Roman;
}
'''

if __name__ == '__main__':
    wtheme = window_alarm()
    wtheme.setAutoFillBackground(True)
    p = wtheme.palette()
    p.setColor(wtheme.backgroundRole(), QColor('#FFFFFF'))
    wtheme.setPalette(p)
    app.setStyleSheet(style_sheet_theme)
    app.exec()
