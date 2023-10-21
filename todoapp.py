from PyQt5 import QtWidgets, uic
from PyQt5.QtGui import QStandardItemModel, QStandardItem
import sys
import pickle
from datetime import datetime


class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__() # Call the inherited classes __init__ method
        uic.loadUi('todoapp.ui', self) # Load the .ui file
        self.show() # Show the GUI

        self.today = str(datetime.now())
        self.add_task.clicked.connect(self.addtask)
        self.remove_task.clicked.connect(self.removetask)
        self.actionOpen.triggered.connect(self.openfile)
        self.actionSave.triggered.connect(self.savefile)

    def addtask(self):
        
        todo, confirmed = QtWidgets.QInputDialog.getText(self, "Add Todo", "New Todo: ")
        if confirmed and not todo.isspace():
            item = QtWidgets.QListWidgetItem()
            item.setText(todo + "  |  " + self.today)
            self.tasks_list.addItem(item)

        print("Add")
        pass

    def removetask(self):
        selected = self.tasks_list.currentItem()
        print(selected.text())
        self.tasks_list.takeItem(self.tasks_list.row(selected))
        
        print("Remove")
        pass

    def openfile(self):
        options = QtWidgets.QFileDialog()
        options = options.options()
        filename, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Open File", "", "Todo Files (*.todo)", options=options)
        if filename != "":
            with open(filename, "rb") as f:
                current_items = pickle.load(f)
                for item in current_items:
                    self.tasks_list.addItem(item)
        print("Open")
        pass
    def savefile(self):

        current_items = []
        for x in range(self.tasks_list.count()):
            current_items.append(self.tasks_list.item(x).text())

        options = QtWidgets.QFileDialog()
        options = options.options()

        filename, _ = QtWidgets.QFileDialog.getSaveFileName(self, "Save File", "", "Todo Files (*.todo)", options=options)
        if filename != "":
            with open(filename, "wb") as f:
                pickle.dump(current_items, f)
        print(current_items)   
        print("Save")
        pass

app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()