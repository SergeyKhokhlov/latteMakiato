import sqlite3
import sys
from PyQt5.QtWidgets import QApplication, QWidget
from addEditCoffeeForm import UiForm
from main import Ui_Form
import os
from PyQt5.QtWidgets import QWidget, QApplication, QTableWidgetItem

count = 0


class Example(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.fullname = os.path.join('data', 'coffee.sqlite')
        self.program_operation()
        self.pushButton.clicked.connect(self.add)
        self.pushButton_2.clicked.connect(self.change)

    def add(self):
        self.close()
        self.add = Add()
        self.add.show()

    def change(self):
        rows = list(set([i.row() for i in self.tableWidget.selectedItems()]))
        if len(rows) == 1:
            id = [self.tableWidget.item(i, 0).text() for i in rows]
            self.close()
            self.change = Change(rows, id)
            self.change.show()

    def program_operation(self):
        global count
        con = sqlite3.connect(self.fullname)
        cur = con.cursor()
        res = cur.execute("""SELECT * FROM coffe""")
        count = 0
        for i in res:
            count += 1
        res = cur.execute("""SELECT * FROM coffe""")
        self.tableWidget.setRowCount(count)
        for i, elem in enumerate(res):
            for j, val in enumerate(elem):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(val)))
        con.close()


class Add(QWidget, UiForm):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.fullname = os.path.join('data', 'coffee.sqlite')
        self.pushButton.clicked.connect(self.check)

    def check(self):
        try:
            if self.lineEdit.text() != '' and self.lineEdit_2.text() != '' and \
                    self.lineEdit_3.text() != '' and self.lineEdit_4.text() != '' and \
                    self.lineEdit_5.text() != '' and self.lineEdit_6.text() != '' and \
                    self.lineEdit_7.text() != '':
                self.program_operation()
        except sqlite3.IntegrityError:
            pass

    def program_operation(self):
        con = sqlite3.connect(self.fullname)
        cur = con.cursor()
        cur.execute("""INSERT INTO coffe(ID, name, degree, groundInGrains, taste,
         price, volume) VALUES(?, ?, ?, ?, ?, ?, ?)""", (self.lineEdit.text(),
                                                         self.lineEdit_2.text(),
                                                         self.lineEdit_3.text(),
                                                         self.lineEdit_4.text(),
                                                         self.lineEdit_5.text(),
                                                         self.lineEdit_6.text(),
                                                         self.lineEdit_7.text()))
        con.commit()
        con.close()
        self.close()
        self.mainWindow = Example()
        self.mainWindow.show()


class Change(QWidget, UiForm):
    def __init__(self, row, id):
        super().__init__()
        self.fullname = os.path.join('data', 'coffee.sqlite')
        self.setupUi(self)
        self.row = row
        self.id = int(id[0])
        self.label.setText('Изменить')
        self.pushButton.clicked.connect(self.check)

    def check(self):
        try:
            if self.lineEdit.text() != '' or self.lineEdit_2.text() != '' or \
                    self.lineEdit_3.text() != '' or self.lineEdit_4.text() != '' or \
                    self.lineEdit_5.text() != '' or self.lineEdit_6.text() != '' or \
                    self.lineEdit_7.text() != '':
                self.program_operation()
        except sqlite3.IntegrityError:
            pass

    def program_operation(self):
        self.con = sqlite3.connect(self.fullname)
        self.cur = self.con.cursor()
        res = self.cur.execute("""SELECT * FROM coffe""")
        full_res = res
        counter = 0
        for i in full_res:
            if counter == self.row[0]:
                self.changeSQLite()
                break
            counter += 1
        self.con.close()

    def changeSQLite(self):
        self.con.close()
        con = sqlite3.connect(self.fullname)
        cur = con.cursor()
        a = self.lineEdit.text()
        if self.lineEdit.text() != '':
            cur.execute("""UPDATE coffe SET ID = ? WHERE ID = ?""", (a, self.id))
            self.id = str(self.lineEdit.text())
        if self.lineEdit_2.text() != '':
            cur.execute("""UPDATE coffe SET name = ? WHERE ID = ?""", (
                self.lineEdit_2.text(),
                self.id))
        if self.lineEdit_3.text() != '':
            cur.execute("""UPDATE coffe SET degree = ? WHERE ID = ?""", (
                self.lineEdit_3.text(),
                self.id))
        if self.lineEdit_4.text() != '':
            cur.execute("""UPDATE coffe SET groundInGrains = ? WHERE ID = ?""", (
                self.lineEdit_4.text(),
                self.id))
        if self.lineEdit_5.text() != '':
            cur.execute("""UPDATE coffe SET taste = ? WHERE ID = ?""", (
                str(self.lineEdit_6.text()),
                self.id))
        if self.lineEdit_6.text() != '':
            cur.execute("""UPDATE coffe SET price = ? WHERE ID = ?""", (
                self.lineEdit_6.text(),
                self.id))
        if self.lineEdit_7.text() != '':
            cur.execute("""UPDATE coffe SET volume = ? WHERE ID = ?""", (
                self.lineEdit_7.text(),
                self.id))
        con.commit()
        con.close()
        self.close()
        self.mWindow = Example()
        self.mWindow.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
