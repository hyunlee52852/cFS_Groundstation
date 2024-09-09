import sys
from DS_Parser import Ui_Form
from PyQt6 import QtWidgets, uic
from PyQt6.QtGui import QFont, QResizeEvent, QFontMetrics
from PyQt6.QtCore import Qt
import csv

import ctypes

Dsparser_lib = ctypes.CDLL("./ds_parser_x86_64.so")
Dsparser_lib.parse_ds.restype = ctypes.c_char_p

app = QtWidgets.QApplication(sys.argv)

class DsParser(QtWidgets.QWidget, Ui_Form):
    
    def __init__(self, *args, obj=None, **kwargs):
        
        # Do not change, automatically generated by QT studio
        super(DsParser, self).__init__(*args, **kwargs)
        self.setupUi(self)
        
        self.pushButton_FileSelector.clicked.connect(self.select_file)
        self.pushButton_FileSelector.clicked.connect(self.parse_ds)
        
        self.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
        
    
    def select_file(self):
        self.file_path, _ = QtWidgets.QFileDialog.getOpenFileName(
            self, "Select File","",
            "DS Files (*.tlm);;All Files (*)",
            )
        if self.file_path:
            self.label_filename.setText(self.file_path)
        else:
            self.label_filename.setText("No file selected")
            
    def parse_ds(self):
        
        output_file_path = Dsparser_lib.parse_ds(self.file_path.encode('utf-8'))
        output_file_path = output_file_path.decode('utf-8')

        with open(output_file_path, newline='', encoding='utf-8') as csvfile:
                reader = csv.reader(csvfile)
                headers = next(reader)

                # Set the number of rows and columns based on the CSV content
                self.tableWidget.setColumnCount(len(headers))
                self.tableWidget.setHorizontalHeaderLabels(headers)

                # Populate the rows
                for row_data in reader:
                    row = self.tableWidget.rowCount()
                    self.tableWidget.insertRow(row)
                    for column, item in enumerate(row_data):
                        cell = QtWidgets.QTableWidgetItem(item)
                        self.tableWidget.setItem(row, column, cell)
        

window = DsParser()
window.show()
app.exec()