from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        self.x = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        Dialog.setObjectName("Dialog")
        Dialog.resize(500, 550)
        Dialog.setMinimumSize(QtCore.QSize(500, 550))
        Dialog.setMaximumSize(QtCore.QSize(500, 550))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light")
        font.setPointSize(14)
        Dialog.setFont(font)
        self.textEdit_input = QtWidgets.QTextEdit(Dialog)
        self.textEdit_input.setGeometry(QtCore.QRect(40, 20, 420, 160))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light")
        font.setPointSize(14)
        self.textEdit_input.setFont(font)
        self.textEdit_input.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.textEdit_input.setInputMethodHints(QtCore.Qt.ImhNone)
        self.textEdit_input.setAutoFormatting(QtWidgets.QTextEdit.AutoNone)
        self.textEdit_input.setTabChangesFocus(False)
        self.textEdit_input.setReadOnly(False)
        self.textEdit_input.setOverwriteMode(False)
        self.textEdit_input.setAcceptRichText(True)
        self.textEdit_input.setObjectName("textEdit_input")
        self.textEdit_input.setPlaceholderText("Введите текст (A-z)")
        self.textOutput = QtWidgets.QTextBrowser(Dialog)
        self.textOutput.setGeometry(QtCore.QRect(40, 200, 420, 160))
        self.textOutput.setPlaceholderText("Зашифрованный (расшифрованный) текст")
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light")
        font.setPointSize(14)
        self.textOutput.setFont(font)
        self.textOutput.setObjectName("textOutput")
        self.pushButton_cipher = QtWidgets.QPushButton(Dialog)
        self.pushButton_cipher.setGeometry(QtCore.QRect(40, 430, 200, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light")
        font.setPointSize(14)
        self.pushButton_cipher.setFont(font)
        self.pushButton_cipher.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_cipher.setStyleSheet("background-color: rgb(170, 170, 255);")
        self.pushButton_cipher.setObjectName("pushButton_cipher")
        self.pushButton_decoding = QtWidgets.QPushButton(Dialog)
        self.pushButton_decoding.setGeometry(QtCore.QRect(40, 480, 200, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light")
        font.setPointSize(14)
        self.pushButton_decoding.setFont(font)
        self.pushButton_decoding.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_decoding.setStyleSheet("background-color: rgb(170, 170, 255);\n"
"")
        self.pushButton_decoding.setObjectName("pushButton_decoding")
        self.textEdit_keyword = QtWidgets.QTextEdit(Dialog)
        self.textEdit_keyword.setGeometry(QtCore.QRect(280, 470, 180, 50))
        self.textEdit_keyword.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.textEdit_keyword.setStyleSheet("")
        self.textEdit_keyword.setObjectName("textEdit_keyword")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(280, 440, 180, 20))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_Error = QtWidgets.QLabel(Dialog)
        self.label_Error.setGeometry(QtCore.QRect(40, 380, 420, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_Error.setFont(font)
        self.label_Error.setStyleSheet("color: rgb(255, 71, 74)")
        self.label_Error.setText("")
        self.label_Error.setObjectName("label_Error")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Nicolencoder"))
        self.textEdit_input.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Bahnschrift Light\'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\';\"><br /></p></body></html>"))
        self.textOutput.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Bahnschrift Light\'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\'; font-size:8.25pt;\"><br /></p></body></html>"))
        self.pushButton_cipher.setText(_translate("Dialog", "Зашифровать"))
        self.pushButton_decoding.setText(_translate("Dialog", "Расшифровать"))
        self.label.setText(_translate("Dialog", "KeyWord:"))

        self.pushButton_cipher.clicked.connect(self.cipher)
        self.pushButton_decoding.clicked.connect(self.decoding)

    def cipher(self):
        try:
            if self.textEdit_keyword.toPlainText() != '':
                a = self.textEdit_input.toPlainText().upper()
                b = self.textEdit_keyword.toPlainText().upper()
                result = ''
                i = 0
                b = ''.join(b.split(' '))
                if len(a) > len(b):
                    z = len(a) - len(b)
                    while i < z:
                        b = b + b[i]
                        i += 1
                i = 0

                while i < len(''.join((a).split(' '))):
                    a1 = self.x.index((''.join(a.split(' ')))[i])
                    b1 = self.x.index(b[i])
                    k = a1 + b1
                    if k > len(self.x) - 1:
                        k = k - len(self.x)
                    result = result + self.x[k]
                    i += 1

                result = list(result)
                a = list(a)
                i = 0

                for q in a:
                    if q == ' ':
                        result.insert(a.index(q) + i, ' ')
                        a.pop(a.index(q))
                        i += 1
                self.label_Error.setText('')
                self.textOutput.setText(''.join(result))
            else:
                self.label_Error.setText("Введите KeyWord")
        except:
            self.label_Error.setText('Используйте символы (A-z)')

    def decoding(self):
        try:
            if self.textEdit_keyword.toPlainText() != '':
                a = self.textEdit_keyword.toPlainText().upper()
                b = self.textEdit_input.toPlainText().upper()
                result = ''
                i = 0
                a = ''.join(a.split(' '))
                if len(b) > len(a):
                    z = len(b) - len(a)
                    while i < z:
                        a = a + a[i]
                        i += 1
                i = 0

                while (i < len(''.join((b).split(' ')))):
                    a1 = self.x.index(a[i])
                    b1 = self.x.index(''.join(b.split(' '))[i])
                    k = b1 - a1
                    if k > len(self.x) - 1:
                        k = k - len(self.x)
                    result = result + self.x[k]
                    i += 1

                result = list(result)
                b = list(b)
                i = 0

                for q in b:
                    if q == ' ':
                        result.insert(b.index(q) + i, ' ')
                        b.pop(b.index(q))
                        i += 1
                self.label_Error.setText('')
                self.textOutput.setText(''.join(result).capitalize())
            else:
                self.label_Error.setText("Введите KeyWord")
        except:
            self.label_Error.setText('Используйте символы (A-z)')


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
