# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addEditCoffeeForm.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class UiForm(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(511, 603)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(200, 10, 131, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(28, 110, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(180, 530, 141, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(80, 109, 391, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(28, 171, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(190, 170, 281, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(28, 231, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.lineEdit_3 = QtWidgets.QLineEdit(Form)
        self.lineEdit_3.setGeometry(QtCore.QRect(200, 230, 271, 31))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(Form)
        self.lineEdit_4.setGeometry(QtCore.QRect(220, 289, 251, 31))
        self.lineEdit_4.setText("")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(30, 290, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.lineEdit_5 = QtWidgets.QLineEdit(Form)
        self.lineEdit_5.setGeometry(QtCore.QRect(190, 349, 281, 31))
        self.lineEdit_5.setText("")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(30, 350, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(30, 411, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.lineEdit_6 = QtWidgets.QLineEdit(Form)
        self.lineEdit_6.setGeometry(QtCore.QRect(100, 410, 371, 31))
        self.lineEdit_6.setText("")
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_7 = QtWidgets.QLineEdit(Form)
        self.lineEdit_7.setGeometry(QtCore.QRect(190, 469, 281, 31))
        self.lineEdit_7.setText("")
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(30, 470, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Добавление"))
        self.label_2.setText(_translate("Form", "ID"))
        self.pushButton.setText(_translate("Form", "Ok"))
        self.label_3.setText(_translate("Form", "Название сорта"))
        self.label_4.setText(_translate("Form", "Степень обжарки"))
        self.label_5.setText(_translate("Form", "Молотый / в зёрнах"))
        self.label_6.setText(_translate("Form", "Описание вкуса"))
        self.label_7.setText(_translate("Form", "Цена"))
        self.label_8.setText(_translate("Form", "Объём упаковки"))