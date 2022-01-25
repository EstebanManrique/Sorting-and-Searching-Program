from PyQt5.QtWidgets import QMainWindow, QApplication, QComboBox, QRadioButton, QLabel, QPushButton
from PyQt5 import uic
import sys
import random

class numberSetSortingUi(QMainWindow):
    """Every piece ff behaviour in the Number Set Sorting screen is controlled here"""
    def __init__(self):
        super(numberSetSortingUi, self).__init__()

        #Loading UI html file to be manipulated using Python
        uic.loadUi("../GUI_Files/numberSetSorting.ui", self)

        #Algorithms are added to Combo Box for user to select from
        self.algorithms = self.findChild(QComboBox, "AlgorithmSelection")
        self.algorithms.addItems(["Quicksort", "Mergesort", "Timsort", "Heapsort", "Bubble Sort", "Insertion Sort", "Selection Sort",
            "Tree Sort", "Counting Sort"])

        #Amount of numbers to be sorted are added so use can choose
        self.numbers = self.findChild(QComboBox, "NumberSelection")
        self.numbers.addItems(["25", "50", "75", "100"])
        
        #Radio Buttons for duplicate numbers are referenced
        self.yesDuplicates = self.findChild(QRadioButton, "YesSelectionDuplicates")
        self.noDuplicates = self.findChild(QRadioButton, "NoSelectionDuplicates")

        #Button to execute the sorting algorithm is called
        self.executeButton = self.findChild(QPushButton, "ExecuteButton")
        self.executeButton.clicked.connect(self.executeSorting)

        #Label where images showing the algorithm working is referenced 
        self.imageDisplayer = self.findChild(QLabel, "GraphSpace")

        #UI is shown
        self.show()

    def executeSorting(self):
        algorithm = self.algorithms.currentText()
        print(self.algorithms.currentText())

        numbers = int(self.numbers.currentText())
        print(int(self.numbers.currentText()))

        if self.noDuplicates.isChecked():
            print("No duplicates")
            print(random.sample(range(120), numbers))
        else:
            print("Duplicates")
            random_numbers = []
            for x in range(numbers):
                random_numbers.append(random.randint(0,120))
            print(random_numbers)


app = QApplication(sys.argv)
UIWindow = numberSetSortingUi()
app.exec_()
