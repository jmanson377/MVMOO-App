# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from QLed import QLed
import matplotlib
matplotlib.use("Qt5Agg")
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT as NavigationToolbar
from matplotlib import cm
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import os, sys, time, csv, io
import qdarkstyle
os.environ['QT_API'] = 'pyqt5'

from MVMOO import MVMOO
import pandas as pd
import numpy as np
import scipy.io

class ThreeDSurface_GraphWindow(FigureCanvasQTAgg): #Class for 3D window
    def __init__(self):
        self.fig =plt.figure(figsize=(7,7))
        self.fig.set_facecolor('#19232D')
        FigureCanvasQTAgg.__init__(self, self.fig) #creating FigureCanvas
        #self.axes = self.fig.gca(projection='3d')#generates 3D Axes object

    def DrawGraph(self, x, y, z=None, c=None, batch=1):#Fun for Graph plotting
        if z is None and c is None:
            self.axes = self.fig.gca()#projection='3d')
            self.axes.clear
            self.axes.scatter(x, y, color='#FF8C00') #plots the 3D surface plot
            self.axes.scatter(x[-batch:],y[-batch:], color='#FF00FF')
            #self.axes.view_init(azim=-90, elev=90)
            #self.axes.w_zaxis.line.set_lw(0.)
            #self.axes.set_zticks([])
            self.axes.set_facecolor('#19232D')
            self.axes.spines['bottom'].set_color('w')
            self.axes.spines['top'].set_color('w') 
            self.axes.spines['right'].set_color('w')
            self.axes.spines['left'].set_color('w')
            self.axes.yaxis.label.set_color('w')
            self.axes.xaxis.label.set_color('w')
            self.axes.tick_params(axis='x', colors='w')
            self.axes.tick_params(axis='y', colors='w')
            self.axes.set_xlabel(r'$f_1$')
            self.axes.set_ylabel(r'$f_2$')
            self.draw()
        elif c is None:
            self.axes = self.fig.gca(projection='3d')
            self.axes.clear()
            self.axes.scatter(x, y, z, color='#FF8C00') #plots the 3D surface plot
            self.axes.scatter(x[-batch:],y[-batch:], z[-batch:],color='#FF00FF')
            self.axes.set_facecolor('#19232D')
            color = (25./254., 35./255., 45./255., 1.0)
            self.axes.w_xaxis.set_pane_color(color)
            self.axes.w_yaxis.set_pane_color(color)
            self.axes.w_zaxis.set_pane_color(color)
            self.axes.spines['bottom'].set_color('w')
            self.axes.spines['top'].set_color('w') 
            self.axes.spines['right'].set_color('w')
            self.axes.spines['left'].set_color('w')
            self.axes.yaxis.label.set_color('w')
            self.axes.xaxis.label.set_color('w')
            self.axes.zaxis.label.set_color('w')
            self.axes.tick_params(axis='x', colors='w')
            self.axes.tick_params(axis='y', colors='w')
            self.axes.tick_params(axis='z', colors='w')
            self.axes.set_xlabel(r'$f_1$')
            self.axes.set_ylabel(r'$f_2$')
            self.axes.set_zlabel(r'$f_3$')
            self.draw()
        else:
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Critical)
            msg.setText("Plot Error")
            msg.setInformativeText('Cannot plot higher than 3D currently!')
            msg.setWindowTitle("Error")
            msg.exec_()

class Ui_MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(Ui_MainWindow, self).__init__()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(809, 594)
        MainWindow.setMinimumSize(QtCore.QSize(809, 594))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.nDim = QtWidgets.QSpinBox(self.centralwidget)
        self.nDim.setMinimum(1)
        self.nDim.setObjectName("nDim")
        self.gridLayout.addWidget(self.nDim, 0, 1, 1, 1)
        self.Mode_2 = QtWidgets.QComboBox(self.centralwidget)
        self.Mode_2.setObjectName("Mode_2")
        self.Mode_2.addItem("")
        self.Mode_2.addItem("")
        self.gridLayout.addWidget(self.Mode_2, 4, 1, 1, 1)
        self.resultsDirectory = QtWidgets.QLineEdit(self.centralwidget)
        self.resultsDirectory.setObjectName("resultsDirectory")
        self.gridLayout.addWidget(self.resultsDirectory, 6, 0, 1, 1)
        self.lObj = QtWidgets.QLabel(self.centralwidget)
        self.lObj.setObjectName("lObj")
        self.gridLayout.addWidget(self.lObj, 1, 0, 1, 1)
        self.nObj = QtWidgets.QSpinBox(self.centralwidget)
        self.nObj.setMinimum(1)
        self.nObj.setObjectName("nObj")
        self.gridLayout.addWidget(self.nObj, 1, 1, 1, 1)
        self.lQual = QtWidgets.QLabel(self.centralwidget)
        self.lQual.setObjectName("lQual")
        self.gridLayout.addWidget(self.lQual, 2, 0, 1, 1)
        self.lDim = QtWidgets.QLabel(self.centralwidget)
        self.lDim.setObjectName("lDim")
        self.gridLayout.addWidget(self.lDim, 0, 0, 1, 1)
        self.nBatch = QtWidgets.QSpinBox(self.centralwidget)
        self.nBatch.setMinimum(1)
        self.nBatch.setObjectName("nBatch")
        self.gridLayout.addWidget(self.nBatch, 3, 1, 1, 1)
        self.nQual = QtWidgets.QSpinBox(self.centralwidget)
        self.nQual.setObjectName("nQual")
        self.gridLayout.addWidget(self.nQual, 2, 1, 1, 1)
        self.lBatch = QtWidgets.QLabel(self.centralwidget)
        self.lBatch.setObjectName("lBatch")
        self.gridLayout.addWidget(self.lBatch, 3, 0, 1, 1)
        self.dataDir = QtWidgets.QPushButton(self.centralwidget)
        self.dataDir.setObjectName("dataDir")
        self.gridLayout.addWidget(self.dataDir, 5, 1, 1, 1)
        self.dataDirectory = QtWidgets.QLineEdit(self.centralwidget)
        self.dataDirectory.setObjectName("dataDirectory")
        self.gridLayout.addWidget(self.dataDirectory, 5, 0, 1, 1)
        self.lMode = QtWidgets.QLabel(self.centralwidget)
        self.lMode.setObjectName("lMode")
        self.gridLayout.addWidget(self.lMode, 4, 0, 1, 1)
        self.resDir = QtWidgets.QPushButton(self.centralwidget)
        self.resDir.setObjectName("resDir")
        self.gridLayout.addWidget(self.resDir, 6, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 2, 1)
        self.ledLayout = QtWidgets.QGridLayout()
        self.ledLayout.setObjectName("ledLayout")
        self.LED = QLed(onColour=QLed.Green, shape=QLed.Circle)
        self.LED.setObjectName("LED")
        self.ledLayout.addWidget(self.LED)
        self.gridLayout_2.addLayout(self.ledLayout, 1, 3, 1, 1)
        self.boundsTable = QtWidgets.QTableWidget(self.centralwidget)
        self.boundsTable.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.boundsTable.setRowCount(1)
        self.boundsTable.setColumnCount(2)
        self.boundsTable.setObjectName("tableWidget")
        item = QtWidgets.QTableWidgetItem()
        self.boundsTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.boundsTable.setHorizontalHeaderItem(1, item)
        self.gridLayout_2.addWidget(self.boundsTable, 0, 1, 2, 1)
        self.startButton = QtWidgets.QPushButton(self.centralwidget)
        self.startButton.setObjectName("startButton")
        self.gridLayout_2.addWidget(self.startButton, 0, 3, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 1, 2, 1, 1)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 0, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout_3.addWidget(self.label_3, 1, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.tResponse = QtWidgets.QTableWidget(self.centralwidget)
        self.tResponse.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tResponse.sizePolicy().hasHeightForWidth())
        self.tResponse.setSizePolicy(sizePolicy)
        self.tResponse.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tResponse.setRowCount(1)
        self.tResponse.setColumnCount(2)
        self.tResponse.setObjectName("tResponse")
        self.verticalLayout.addWidget(self.tResponse)
        self.gridLayout_3.addLayout(self.verticalLayout, 1, 1, 1, 1)
        self.submit = QtWidgets.QPushButton(self.centralwidget)
        self.submit.setEnabled(False)
        self.submit.setObjectName("submit")
        self.gridLayout_3.addWidget(self.submit, 2, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout_3.addWidget(self.label_4, 2, 0, 1, 1)
        self.tConditions = QtWidgets.QTableWidget(self.centralwidget)
        self.tConditions.setEnabled(False)
        self.tConditions.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tConditions.setRowCount(1)
        self.tConditions.setColumnCount(2)
        self.tConditions.setObjectName("tConditions")
        self.tConditions.horizontalHeader().setVisible(True)
        self.tConditions.verticalHeader().setVisible(True)
        self.tConditions.verticalHeader().setStretchLastSection(False)
        self.gridLayout_3.addWidget(self.tConditions, 0, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout_3, 3, 0, 2, 1)
        self.figLayout = QtWidgets.QGridLayout()
        self.figLayout.setObjectName("figLayout")
        self.figureWidget = ThreeDSurface_GraphWindow()#creating 3D Window
        self.figureWidget.setObjectName("figureWidget")
        self.figLayout.addWidget(self.figureWidget)
        self.gridLayout_2.addLayout(self.figLayout, 2, 1, 3, 3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 809, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Event connections
        self.nDim.valueChanged.connect(self.adjustTable)
        self.dataDir.clicked.connect(self.getDir)
        self.resDir.clicked.connect(self.setDir)
        self.nObj.valueChanged.connect(self.adjustObj)
        self.Mode_2.currentTextChanged.connect(self.adjustMode)
        self.startButton.clicked.connect(self.start)
        self.changed_items = []
        self.boundsTable.itemChanged.connect(self.log_change)
        self.tConditions.installEventFilter(self)
        self.submit.clicked.connect(self.submit_click)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Mode_2.setItemText(0, _translate("MainWindow", "Online"))
        self.Mode_2.setItemText(1, _translate("MainWindow", "Offline"))
        self.lObj.setText(_translate("MainWindow", "Number of Objectives"))
        self.lQual.setText(_translate("MainWindow", "Number of Qualitative Variables"))
        self.lDim.setText(_translate("MainWindow", "Dimension"))
        self.lBatch.setText(_translate("MainWindow", "Batch Size"))
        self.dataDir.setText(_translate("MainWindow", "Data Folder"))
        self.lMode.setText(_translate("MainWindow", "Mode"))
        self.resDir.setText(_translate("MainWindow", "Results Folder"))
        item = self.boundsTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Lower"))
        item = self.boundsTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Upper"))
        self.startButton.setText(_translate("MainWindow", "Start"))
        self.label.setText(_translate("MainWindow", "Watcher Active"))
        self.label_2.setText(_translate("MainWindow", "Conditions to Run"))
        self.label_3.setText(_translate("MainWindow", "Response"))
        self.submit.setText(_translate("MainWindow", "Submit"))
        self.label_4.setText(_translate("MainWindow", "Submit Data"))

    def eventFilter(self, source, event):
        if (event.type() == QtCore.QEvent.KeyPress and
            event.matches(QtGui.QKeySequence.Copy)):
            self.copySelection()
            return True
        return super(Ui_MainWindow, self).eventFilter(source, event)

    def copySelection(self):
        selection = self.tConditions.selectedIndexes()
        if selection:
            rows = sorted(index.row() for index in selection)
            columns = sorted(index.column() for index in selection)
            rowcount = rows[-1] - rows[0] + 1
            colcount = columns[-1] - columns[0] + 1
            table = [[''] * colcount for _ in range(rowcount)]
            for index in selection:
                row = index.row() - rows[0]
                column = index.column() - columns[0]
                table[row][column] = index.data()
            stream = io.StringIO()
            csv.writer(stream).writerows(table)
            QtWidgets.qApp.clipboard().setText(stream.getvalue())

    def log_change(self, item):
        try:
            float(item.text())
            self.changed_items.append(item)
        except ValueError:
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Critical)
            msg.setText("Input Error")
            msg.setInformativeText('Please enter valid numeric value for bounds!')
            msg.setWindowTitle("Error")
            msg.exec_()

    def adjustMode(self):
        if self.Mode_2.currentText() == 'Online':
            self.dataDir.setEnabled(True)
            self.dataDirectory.setEnabled(True)
            self.resDir.setEnabled(True)
            self.resultsDirectory.setEnabled(True)
            self.tConditions.setEnabled(False)
            self.tResponse.setEnabled(False)
            self.submit.setEnabled(False)
        else:
            self.dataDir.setEnabled(False)
            self.dataDirectory.setEnabled(False)
            self.resDir.setEnabled(False)
            self.resultsDirectory.setEnabled(False)
            self.tConditions.setEnabled(True)
            self.tResponse.setEnabled(True)
            self.submit.setEnabled(True)

    def adjustTable(self):
        self.boundsTable.setRowCount(self.nDim.value())
        self.tConditions.setColumnCount(self.nDim.value())

    def adjustObj(self):
        self.tResponse.setColumnCount(self.nObj.value())

    def tableValue(self,row,col):
        print(self.boundsTable.item(row,col).value())

    def getTableValues(self):
        values = np.zeros((2,self.nDim.value()))
        for item in self.changed_items:
            values[item.column(), item.row()] = float(item.text())
        return values          

    def getDir(self):
        path = QtWidgets.QFileDialog.getExistingDirectory(None, "Select Folder")
        self.dataDirectory.setText(path)

    def setDir(self):
        path = QtWidgets.QFileDialog.getExistingDirectory(None, "Select Folder")
        self.resultsDirectory.setText(path)

    def plotting(self,Y):
        if int(self.nObj.value()) == 2:
            self.figureWidget.DrawGraph(Y[:,0],Y[:,1],batch=int(self.nBatch.value()))
        elif int(self.nObj.value()) == 3:
            self.figureWidget.DrawGraph(Y[:,0],Y[:,1],Y[:,2],batch=int(self.nBatch.value()))
        else:
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Critical)
            msg.setText("Plot Error")
            msg.setInformativeText('Cannot plot higher than 3D currently!')
            msg.setWindowTitle("Error")
            msg.exec_()

    def getnextconditions(self, X, Y):
        if self.mode == 0:
            sign = 1
        else:
            sign = -1
        if int(self.nBatch.value()) < 2:
            xnext, _ = self.optimiser.multinextcondition(X, sign*Y)
            return xnext
        xnext = []
        Xtemp = X[:]
        Ytemp = sign*Y[:]
        for _ in range(int(self.nBatch.value())):
            xmax, _ = self.optimiser.multinextcondition(Xtemp, Ytemp)
            xnext.append(xmax)
            Ynew = []
            for j in range(int(self.nObj.value())):
                ymu, _ = self.optimiser.models[j].predict_y(xmax)
                Ynew.append(ymu)
            Ynew = np.array(Ynew).reshape(-1,int(self.nObj.value()))
            Xtemp = np.concatenate((Xtemp,xmax))
            Ytemp = np.concatenate((Ytemp,Ynew))
        return np.array(xnext).reshape(-1,np.shape(X)[1])

    def startErrorCheck(self):
        if (not os.path.isdir(self.dataDirectory.text()) or not os.path.isdir(self.resultsDirectory.text())) and self.Mode_2.currentText() == 'Online':
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Critical)
            msg.setText("Directory Error")
            msg.setInformativeText('Check valid format for data and results directories!')
            msg.setWindowTitle("Error")
            msg.exec_()
            return False
        elif np.shape(self.getTableValues()) != (2,int(self.nDim.value())) or np.size(self.changed_items) < 2 * int(self.nDim.value()):
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Critical)
            msg.setText("Bounds Error")
            msg.setInformativeText('Check bounds match the optimisation dimension')
            msg.setWindowTitle("Error")
            msg.exec_()
            return False
        elif int(self.nDim.value()) <= 0 or int(self.nObj.value()) <= 0 or int(self.nDim.value()) < 0 or int(self.nBatch.value()) <=0: 
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Critical)
            msg.setText("Input Error")
            msg.setInformativeText('Check numeric values for dimension, objectives, qualitative variabes or batch size!')
            msg.setWindowTitle("Error")
            msg.exec_()
            return False
        elif int(self.nDim.value()) > 9:
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText("Dimensionality Warning")
            msg.setInformativeText('Performance may be affected by high dimensional problems')
            msg.setWindowTitle("Warning")
            msg.exec_()
            return True
        else:
            return True

    def disableInputs(self):
        self.dataDir.setDisabled(True)
        self.resDir.setDisabled(True)
        self.boundsTable.setDisabled(True)
        self.dataDirectory.setDisabled(True)
        self.resultsDirectory.setDisabled(True)
        self.nDim.setDisabled(True)
        self.nObj.setDisabled(True)
        self.nQual.setDisabled(True)
        self.startButton.setDisabled(True)
        self.nBatch.setDisabled(True)
              
    def onChange(self):
        time.sleep(2)
        fname = self.dataDirectory.text() + "/data.mat"
        if os.path.isfile(fname):
            print("file has been created")
            values = scipy.io.loadmat(fname)
            os.remove(fname)
            X = values['data'][:,:self.nDim.value()]
            Y = values['data'][:,-self.nObj.value():]
            x = self.getnextconditions(X,Y)
            values = {'values': x}
            scipy.io.savemat(self.resultsDirectory.text() + '/next.mat',values)
            self.plotting(Y)
        else:
            print("file has been delete")

    def addTablevalues(self, values):
        self.tConditions.setRowCount(np.shape(values)[0])
        self.tConditions.setColumnCount(np.shape(values)[1])
        for i in range(np.shape(values)[0]):
            for j in range(np.shape(values)[1]):
                self.tConditions.setItem(i,j,QtWidgets.QTableWidgetItem(str(values[i,j])))

    def adjustResponse(self, rows):
        self.tResponse.setRowCount(rows)
        for i in range(rows):
            for j in range(self.nObj.value()):
                self.tResponse.setItem(i,j, QtWidgets.QTableWidgetItem())

    def getMode(self):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Question)
        msg.setText("Optimisation Mode")
        msg.setInformativeText('Is this a minimisation or maximisation problem?')
        msg.setWindowTitle("Mode Select")
        msg.addButton(QtWidgets.QPushButton('Minimisation'), QtWidgets.QMessageBox.YesRole)
        msg.addButton(QtWidgets.QPushButton('Maximisation'), QtWidgets.QMessageBox.NoRole)
        result = msg.exec_()

        if result == 0:
            return 'min'
        else:
            return 'max'
    
    def start(self):
        # Test file system watcher
        if self.startErrorCheck():
            if self.Mode_2.currentText == 'Online':
                self.watcher = QtCore.QFileSystemWatcher()
                path = self.dataDirectory.text()
                self.watcher.addPath(path)
                self.watcher.directoryChanged.connect(self.onChange)
                # Complete
                bounds = self.getTableValues()
                self.optimiser = MVMOO(input_dim=int(self.nDim.value()),num_qual=int(self.nQual.value()),num_obj=int(self.nObj.value()),bounds=bounds)
                self.LED.value = True
                self.disableInputs()
            else: # Offline mode
                bounds = self.getTableValues()
                bounds[-self.nQual.value():,:] = bounds[-self.nQual.value():,:].astype(np.int)
                self.optimiser = MVMOO(input_dim=int(self.nDim.value()),num_qual=int(self.nQual.value()),num_obj=int(self.nObj.value()),bounds=bounds)
                initial = self.optimiser.sample_design(samples=5, design='lhc')
                self.addTablevalues(initial)
                self.adjustResponse(np.shape(initial)[0])
                self.LED.value = True
                self.disableInputs()
                self.iteration = 0
            self.mode = self.getMode()

        # Add an option to continue from a previous run

        

    def submit_click(self):
        # Firstly check response size matches conditions
        conditions = np.zeros((self.tConditions.rowCount(),self.tConditions.columnCount()))
        for i in range(self.tConditions.rowCount()):
            for j in range(self.tConditions.columnCount()):
                conditions[i,j] = float(self.tConditions.item(i,j).text())
        
        response = np.zeros((self.tResponse.rowCount(),self.nObj.value()))
        for i in range(self.tResponse.rowCount()):
            for j in range(self.nObj.value()):
                response[i,j] = float(self.tResponse.item(i,j).text())
                
        if self.iteration == 0:
            self.X = conditions
            self.Y = response
        else:
            self.X = np.concatenate((self.X,conditions))
            self.Y = np.concatenate((self.Y, response))

        next_condition = self.getnextconditions(self.X, self.Y)
        
        self.addTablevalues(next_condition)
        self.adjustResponse(np.shape(next_condition)[0]) 

        self.plotting(self.Y)
        self.iteration += 1

        

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    app.setStyleSheet(qdarkstyle.load_stylesheet_from_environment())
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())