import formulas
from gui import *
from PyQt6.QtWidgets import *


class Logic(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.num_list = []
        self.button_enter.clicked.connect(lambda: self.enter())
        self.button_calc.clicked.connect(lambda: self.calc())
        self.list.itemSelectionChanged.connect(lambda: self.button_del.setEnabled(True))
        self.button_del.clicked.connect(lambda: self.del_entry())
        self.button_clear.clicked.connect(lambda: self.clear())

    def enter(self):
        """
        Saves numbers to be calculated
        """
        entry = self.line_entry.text()
        try:
            self.num_list.append(float(entry))
        except ValueError:
            self.line_entry.clear()
        else:
            self.list.addItem(entry)
        self.line_entry.clear()

    def calc(self):
        """
        calculates values with selected operand
        """
        if len(self.num_list) == 0:
            self.label.setText('0')
        elif self.radio_add.isChecked():
            self.label.setText(str(formulas.add(self.num_list)))
        elif self.radio_sub.isChecked():
            self.label.setText(str(formulas.subtract(self.num_list)))
        elif self.radio_mul.isChecked():
            self.label.setText(str(formulas.multiply(self.num_list)))
        elif self.radio_div.isChecked():
            try:
                self.label.setText(str(formulas.divide(self.num_list)))
            except ZeroDivisionError:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Icon.Warning)
                msg.setText("Cannot Divide by Zero")
                msg.exec()
        elif self.radio_choose.isChecked():
            self.label.setText(str(formulas.choose(self.num_list)))

    def del_entry(self):
        """
        Deletes selected number
        """
        tar = self.list.currentRow()
        self.num_list.remove(self.num_list[tar - 1])
        self.list.takeItem(tar)
        if len(self.num_list) == 0:
            self.button_del.setEnabled(False)

    def clear(self):
        """
        Resets Gui
        """
        self.line_entry.clear()
        self.list.setCurrentRow(1)
        for i in range(len(self.num_list)):
            self.del_entry()
        self.button_del.setEnabled(False)
        self.label.setText('0')
