# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'final_project.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(650, 600)
        MainWindow.setStyleSheet("QWidget {\n"
"   background-color: beige;\n"
"}\n"
"\n"
"/* Nice Windows-XP-style password character. */\n"
"QLineEdit[echoMode=\"2\"] {\n"
"    lineedit-password-character: 9679;\n"
"}\n"
"\n"
"/* We provide a min-width and min-height for push buttons\n"
"   so that they look elegant regardless of the width of the text. */\n"
"QPushButton {\n"
"    background-color: palegoldenrod;\n"
"    border-width: 2px;\n"
"    border-color: darkkhaki;\n"
"    border-style: solid;\n"
"    border-radius: 5;\n"
"    padding: 3px;\n"
"    min-width: 9ex;\n"
"    min-height: 2.5ex;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"   background-color: khaki;\n"
"}\n"
"\n"
"/* Increase the padding, so the text is shifted when the button is\n"
"   pressed. */\n"
"QPushButton:pressed {\n"
"    padding-left: 5px;\n"
"    padding-top: 5px;\n"
"    background-color: #d0d67c;\n"
"}\n"
"\n"
"QLabel, QAbstractButton {\n"
"    font: bold;\n"
"}\n"
"\n"
"/* Mark mandatory fields with a brownish color. */\n"
".mandatory {\n"
"    color: brown;\n"
"}\n"
"\n"
"/* Bold text on status bar looks awful. */\n"
"QStatusBar QLabel {\n"
"   font: normal;\n"
"}\n"
"\n"
"QStatusBar::item {\n"
"    border-width: 1;\n"
"    border-color: darkkhaki;\n"
"    border-style: solid;\n"
"    border-radius: 2;\n"
"}\n"
"\n"
"QComboBox, QLineEdit, QSpinBox, QTextEdit, QListView {\n"
"    background-color: cornsilk;\n"
"    selection-color: #0a214c; \n"
"    selection-background-color: #C19A6B;\n"
"}\n"
"\n"
"QListView {\n"
"    show-decoration-selected: 1;\n"
"}\n"
"\n"
"QListView::item:hover {\n"
"    background-color: wheat;\n"
"}\n"
"\n"
"/* We reserve 1 pixel space in padding. When we get the focus,\n"
"   we kill the padding and enlarge the border. This makes the items\n"
"   glow. */\n"
"QLineEdit, QFrame {\n"
"    border-width: 2px;\n"
"    padding: 1px;\n"
"    border-style: solid;\n"
"    border-color: darkkhaki;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"/* As mentioned above, eliminate the padding and increase the border. */\n"
"QLineEdit:focus, QFrame:focus {\n"
"    border-width: 3px;\n"
"    padding: 0px;\n"
"}\n"
"\n"
"/* A QLabel is a QFrame ... */\n"
"QLabel {\n"
"    border: none;\n"
"    padding: 0;\n"
"    background: none;\n"
"}\n"
"\n"
"/* A QToolTip is a QLabel ... */\n"
"QToolTip {\n"
"    border: 2px solid darkkhaki;\n"
"    padding: 5px;\n"
"    border-radius: 3px;\n"
"    opacity: 200;\n"
"}\n"
"\n"
"/* Nice to have the background color change when hovered. */\n"
"QRadioButton:hover, QCheckBox:hover {\n"
"    background-color: wheat;\n"
"}\n"
"\n"
"/* Force the dialog\'s buttons to follow the Windows guidelines. */\n"
"QDialogButtonBox {\n"
"    button-layout: 0;\n"
"}\n"
"\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_mesafetara = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_mesafetara.setGeometry(QtCore.QRect(520, 500, 75, 23))
        self.pushButton_mesafetara.setObjectName("pushButton_mesafetara")
        self.pushButton_ldrdeger = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_ldrdeger.setGeometry(QtCore.QRect(530, 290, 75, 23))
        self.pushButton_ldrdeger.setObjectName("pushButton_ldrdeger")
        self.label_ldr_pic = QtWidgets.QLabel(self.centralwidget)
        self.label_ldr_pic.setGeometry(QtCore.QRect(520, 170, 111, 101))
        self.label_ldr_pic.setText("")
        self.label_ldr_pic.setPixmap(QtGui.QPixmap("image/ldr.png"))
        self.label_ldr_pic.setObjectName("label_ldr_pic")
        self.label_dc_pic = QtWidgets.QLabel(self.centralwidget)
        self.label_dc_pic.setGeometry(QtCore.QRect(14, 470, 91, 51))
        self.label_dc_pic.setText("")
        self.label_dc_pic.setPixmap(QtGui.QPixmap("image/dc_motor.png"))
        self.label_dc_pic.setObjectName("label_dc_pic")
        self.label_servo_pic = QtWidgets.QLabel(self.centralwidget)
        self.label_servo_pic.setGeometry(QtCore.QRect(20, 170, 101, 121))
        self.label_servo_pic.setText("")
        self.label_servo_pic.setPixmap(QtGui.QPixmap("image/servo.png"))
        self.label_servo_pic.setObjectName("label_servo_pic")
        self.label_mesafepic = QtWidgets.QLabel(self.centralwidget)
        self.label_mesafepic.setGeometry(QtCore.QRect(510, 420, 111, 61))
        self.label_mesafepic.setText("")
        self.label_mesafepic.setPixmap(QtGui.QPixmap("image/mesafe.png"))
        self.label_mesafepic.setObjectName("label_mesafepic")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(30, 31, 581, 102))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEdit_rgb = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_rgb.setMinimumSize(QtCore.QSize(0, 50))
        self.lineEdit_rgb.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_rgb.setObjectName("lineEdit_rgb")
        self.horizontalLayout.addWidget(self.lineEdit_rgb)
        self.label_rgb_pic = QtWidgets.QLabel(self.layoutWidget)
        self.label_rgb_pic.setText("")
        self.label_rgb_pic.setPixmap(QtGui.QPixmap("image/rgb.png"))
        self.label_rgb_pic.setObjectName("label_rgb_pic")
        self.horizontalLayout.addWidget(self.label_rgb_pic)
        self.rgb = QtWidgets.QPushButton(self.layoutWidget)
        self.rgb.setMinimumSize(QtCore.QSize(60, 18))
        self.rgb.setObjectName("rgb")
        self.horizontalLayout.addWidget(self.rgb)
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(130, 210, 65, 54))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_servorun = QtWidgets.QPushButton(self.layoutWidget1)
        self.pushButton_servorun.setObjectName("pushButton_servorun")
        self.verticalLayout.addWidget(self.pushButton_servorun)
        self.pushButton_servostop = QtWidgets.QPushButton(self.layoutWidget1)
        self.pushButton_servostop.setObjectName("pushButton_servostop")
        self.verticalLayout.addWidget(self.pushButton_servostop)
        self.layoutWidget2 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget2.setGeometry(QtCore.QRect(114, 470, 65, 63))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pushButton_dcrun = QtWidgets.QPushButton(self.layoutWidget2)
        self.pushButton_dcrun.setObjectName("pushButton_dcrun")
        self.verticalLayout_2.addWidget(self.pushButton_dcrun)
        self.pushButton_dcstop = QtWidgets.QPushButton(self.layoutWidget2)
        self.pushButton_dcstop.setObjectName("pushButton_dcstop")
        self.verticalLayout_2.addWidget(self.pushButton_dcstop)
        self.label_dc = QtWidgets.QLabel(self.centralwidget)
        self.label_dc.setGeometry(QtCore.QRect(40, 530, 61, 20))
        self.label_dc.setObjectName("label_dc")
        self.label_ldr = QtWidgets.QLabel(self.centralwidget)
        self.label_ldr.setGeometry(QtCore.QRect(560, 270, 31, 16))
        self.label_ldr.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_ldr.setObjectName("label_ldr")
        self.label_servo = QtWidgets.QLabel(self.centralwidget)
        self.label_servo.setGeometry(QtCore.QRect(30, 280, 91, 16))
        self.label_servo.setObjectName("label_servo")
        self.label_mesafe = QtWidgets.QLabel(self.centralwidget)
        self.label_mesafe.setGeometry(QtCore.QRect(510, 480, 101, 20))
        self.label_mesafe.setObjectName("label_mesafe")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(540, 320, 47, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(530, 530, 63, 31))
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_mesafetara.setText(_translate("MainWindow", "TARA"))
        self.pushButton_ldrdeger.setText(_translate("MainWindow", "DE??ER AL"))
        self.lineEdit_rgb.setText(_translate("MainWindow", "RedGreenBlue"))
        self.rgb.setText(_translate("MainWindow", "RGB"))
        self.pushButton_servorun.setText(_translate("MainWindow", "??ALI??TIR"))
        self.pushButton_servostop.setText(_translate("MainWindow", "DURDUR"))
        self.pushButton_dcrun.setText(_translate("MainWindow", "??ALI??TIR"))
        self.pushButton_dcstop.setText(_translate("MainWindow", "DURDUR"))
        self.label_dc.setText(_translate("MainWindow", "DC MOTOR"))
        self.label_ldr.setText(_translate("MainWindow", "LDR"))
        self.label_servo.setText(_translate("MainWindow", "SERVO MOTOR"))
        self.label_mesafe.setText(_translate("MainWindow", "MESAFE SENS??R??"))
        self.label.setText(_translate("MainWindow", "0"))
        self.label_2.setText(_translate("MainWindow", "0"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
