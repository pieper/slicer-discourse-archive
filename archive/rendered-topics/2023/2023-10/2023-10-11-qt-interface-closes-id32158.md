---
topic_id: 32158
title: "Qt Interface Closes"
date: 2023-10-11
url: https://discourse.slicer.org/t/32158
---

# Qt interface closes

**Topic ID**: 32158
**Date**: 2023-10-11
**URL**: https://discourse.slicer.org/t/qt-interface-closes/32158

---

## Post #1 by @bserrano (2023-10-11 14:48 UTC)

<p>Hi all,</p>
<p>I am implementing a very simple interface in Qt. The ui code is in a file called “myUI.py” and I want to call it from my “script.py” (call to <code>run_gui</code>). It generates the window but closes it inmediately. How can I fix that?</p>
<p>Running the code <code>run_gui</code> from terminal works.</p>
<p>The UI looks like:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/d/6d0bbeb1b2b7047ffcec13a0d25f61912b33cf14.png" alt="imagen" data-base62-sha1="fyFcS312x0qFbqCY9UCKC8bhwwI" width="683" height="210"></p>
<p>The code of <code>myUI.py</code> is:</p>
<pre><code class="lang-auto">import sys
from qt import QApplication, QMainWindow, QTextBrowser, QLabel, QPushButton, QWidget, QCheckBox, \
    QVBoxLayout, QLineEdit, QApplication
from . import script

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(714, 294)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setGeometry(530, 180, 141, 51)
        font = self.pushButton.font
        font.setPointSize(13)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(script.readUserInputFromGUI)
        self.pushButton.toggle()
        
        self.checkBox = QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(30, 180, 391, 51)
        font = self.checkBox.font
        font.setPointSize(13)
        self.checkBox.setFont(font)
        self.checkBox.setObjectName("checkBox")
        self.checkBox.setChecked(True)
        
        self.widget = QWidget(self.centralwidget)
        self.widget.setGeometry(30, 45, 641, 121)
        self.widget.setObjectName("widget")
        
        self.gridLayout = QVBoxLayout(self.widget)
        
        self.label = QLabel(self.widget)
        font = self.label.font
        font.setPointSize(13)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label)
        
        self.lineEdit = QLineEdit(self.widget)
        font = self.lineEdit.font
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setFixedWidth(650)
        self.lineEdit.setFixedHeight(20)
        self.gridLayout.addWidget(self.lineEdit)
        
        self.label_2 = QLabel(self.widget)
        font = self.label_2.font
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2)
        
        self.lineEdit_2 = QLineEdit(self.widget)
        font = self.lineEdit_2.font
        font.setPointSize(12)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setFixedWidth(650)
        self.lineEdit_2.setFixedHeight(20)
        self.gridLayout.addWidget(self.lineEdit_2)
        
        self.label_3 = QLabel(self.widget)
        font = self.label_3.font
        font.setPointSize(13)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3)
        
        self.lineEdit_3 = QLineEdit(self.widget)
        font = self.lineEdit_3.font
        font.setPointSize(12)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_3.setFixedWidth(200)
        self.lineEdit_3.setFixedHeight(20)
        self.gridLayout.addWidget(self.lineEdit_3)
        
        MainWindow.setCentralWidget(self.centralwidget)
        
        self.retranslateUi(MainWindow)
        
        
    def retranslateUi(self, MainWindow):
        _translate = QApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Continue"))
        self.checkBox.setText(_translate("MainWindow", "Select if you want to reslice the volume"))
        self.label.setText(_translate("MainWindow", "Path to patients folder"))
        self.label_2.setText(_translate("MainWindow", "Path to save results"))
        self.label_3.setText(_translate("MainWindow", "Patient ID"))

def run_gui():
    #app = QApplication
    form = QMainWindow()
    window = Ui_MainWindow()
    window.setupUi(form)
    form.show()
    # sys.exit(app.exec_())

</code></pre>
<p>I tried to use QApplication but I had the same problem.</p>
<p>Thanks,</p>

---

## Post #2 by @pieper (2023-10-11 16:50 UTC)

<aside class="quote no-group" data-username="bserrano" data-post="1" data-topic="32158">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/bserrano/48/17034_2.png" class="avatar"> bserrano:</div>
<blockquote>
<p>I want to call it from my “script.py” (call to <code>run_gui</code>).</p>
</blockquote>
</aside>
<p>How are you running your script?</p>

---

## Post #3 by @bserrano (2023-10-13 12:39 UTC)

<p>The code is part of a module I’m working on. The idea is to do  <code>import moduleName</code> on python console and then I want the interface to open.</p>
<p>Module stucture is:<br>
init.py —calls—&gt; script.py —calls—&gt; ui.py to open ui</p>

---

## Post #4 by @pieper (2023-10-13 13:36 UTC)

<p>Probably your UI variables are going out of scope so they are deleted automatically.</p>
<p>Try first with a simple script that just shows a button and try different ways to launch the script and store your variables.</p>

---

## Post #5 by @bserrano (2023-10-18 11:21 UTC)

<p>Defining the mainWindow variable as “global” works.</p>
<p>Thanks</p>

---
