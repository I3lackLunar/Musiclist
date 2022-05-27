# Import of the libraries
import sys
import sqlite3

# Pick out specific function inside of a library
from PyQt6.QtWidgets import (QApplication, QHBoxLayout, QInputDialog, QMainWindow, QMessageBox, QPushButton,
                             QTableWidget, QTableWidgetItem, QToolTip, QVBoxLayout, QWidget)

# def/enum
DATABASE = 'Musiclist.db'
TITLE = 'Musiclist'
DATA_COL = ["Numeration", "Title", "Artist", "Genre", "Occasion", "Mood", "Dancestyle", "Topic", "Length"]

# sqlite3
# find or create the database
con = sqlite3.connect(DATABASE)
cc = con.cursor()

# TESTDATA
TABLEDATA = []
item_1 = [1, 'Musictitel Nr. 1', 'Artist Nr. 1', 'Genre Nr. 1', 'Occasion Nr. 1', 'Mood Nr. 1', 'Dancestyle Nr. 1',
          '1:00']
item_2 = [2, 'Musictitel Nr. 2', 'Artist Nr. 2', 'Genre Nr. 2', 'Occasion Nr. 2', 'Mood Nr. 2', 'Dancestyle Nr. 2',
          '1:00']
item_3 = [3, 'Musictitel Nr. 3', 'Artist Nr. 3', 'Genre Nr. 3', 'Occasion Nr. 3', 'Mood Nr. 3', 'Dancestyle Nr. 3',
          '1:00']
TABLEDATA.append(item_1)
TABLEDATA.append(item_2)
TABLEDATA.append(item_3)

# main application
class MainWindow(QWidget):
    # don't know what it does but it does something
    def __init__(self):                     #done
        super(MainWindow,self).__init__()
        self.mainUI()

    def db2table(self, DATABASE, TABLE):    #done
        # copy all data from db to table
        row = 0
        for r in DATABASE:
            col = 0
            for item in r:
                cell = QTableWidgetItem(str(item))
                TABLE.setItem(row, col, cell)
                col += 1
            row += 1


    def table2db(self, table, database):    #test
        print("test")
        #print(table[1])
        #type_buffer = []
        #tablerow = len(DATA_COL) - 1
        #row = 0
        #for r in tablerow:
        #    for col in r:
        #        type_buffer.append(table.item(row, col).text())
        #        if type_buffer[0] == " ":
        #            cc.execute("""INSERT INTO Musiclist VALUES ({},{},{},{},{},{},{},{}).format(type_buffer[0],type_buffer[1],
        #            type_buffer[2],type_buffer[3],type_buffer[4],type_buffer[5],type_buffer[6],type_buffer[7])""")
        #        else:
        #
        #    row += 1

    def test2db(self, table, database):
        #type_buffer=[]
        tablerow = len(DATA_COL)-1
        for r in range(tablerow):
            print(r)

    def test2table(self,database,table):
        tablerow=len(DATA_COL)-1
        column=0
        table.setRowCount(len(database))
        for group in database:
            #print(column)
            row=0
            for item in group:
                table.setItem(column, row, QTableWidgetItem(item))
                row=row+1
            column=column+1
# STILL NOT DONE


    # function to close the window
    def closeApp(self):
        # save all data from table to DB
        return self.close

    def mainUI(self):
        # setup
        self.setWindowTitle(TITLE)

        # table preset
        table_list = QTableWidget()
        table_list.setColumnCount(len(DATA_COL))
        #table_list.setRowCount(4)
        table_list.setHorizontalHeaderLabels(DATA_COL)

        # button preset
        test_db_btn = QPushButton('TEST', self)                             #TEST
        test_db_btn.clicked.connect(lambda: self.test2table(TABLEDATA,table_list))  #TEST

        load_db_btn = QPushButton('Load Database', self)
        load_db_btn.clicked.connect(lambda: self.db2table(DATABASE,table_list))

        safe_table_btn = QPushButton('Safe Table', self)
        #safe_table_btn.clicked.connect(lambda: self.table2db(table_list, DATABASE))
        safe_table_btn.clicked.connect(lambda: self.test2db(TABLEDATA, DATABASE))

        add_btn = QPushButton('Add Music',self)                     # needs to be programmed, opens a new window to add music to the list

        close_btn = QPushButton("Close Application",self)            # need to be programmed
        close_btn.clicked.connect(self.closeApp())

        delete_btn = QPushButton("Delete Music",self)

        create_pl_btn = QPushButton("Create Playlist",self)

        # layout
        self.menu_btn_Layout = QHBoxLayout()
        self.menu_btn_Layout.addWidget(test_db_btn)                          #TEST
        self.menu_btn_Layout.addWidget(load_db_btn)
        self.menu_btn_Layout.addWidget(safe_table_btn)
        self.menu_btn_Layout.addWidget(close_btn)

        self.utility_btn_Layout = QHBoxLayout()
        self.utility_btn_Layout.addWidget(add_btn)
        self.utility_btn_Layout.addWidget(delete_btn)
        self.utility_btn_Layout.addWidget(create_pl_btn)

        self.main_Layout = QVBoxLayout()
        self.main_Layout.addLayout(self.menu_btn_Layout)
        self.main_Layout.addLayout(self.utility_btn_Layout)
        self.main_Layout.addWidget(table_list)

        #self.setLayout(top_btn_Layout)
        self.setLayout(self.main_Layout)
        self.show()

app = QApplication(sys.argv)
exe = MainWindow()
exe.show()
sys.exit(app.exec())