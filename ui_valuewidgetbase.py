# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_valuewidgetbase.ui'
#
# Created: Thu Jun 12 13:05:26 2014
#      by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_ValueWidgetBase(object):
    def setupUi(self, ValueWidgetBase):
        ValueWidgetBase.setObjectName(_fromUtf8("ValueWidgetBase"))
        ValueWidgetBase.resize(340, 392)
        self.verticalLayout = QtGui.QVBoxLayout(ValueWidgetBase)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.cbxEnable = QtGui.QCheckBox(ValueWidgetBase)
        self.cbxEnable.setObjectName(_fromUtf8("cbxEnable"))
        self.verticalLayout.addWidget(self.cbxEnable)
        self.tabWidget = QtGui.QTabWidget(ValueWidgetBase)
        self.tabWidget.setTabPosition(QtGui.QTabWidget.North)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tabWidgetPage1 = QtGui.QWidget()
        self.tabWidgetPage1.setObjectName(_fromUtf8("tabWidgetPage1"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.tabWidgetPage1)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.widget = QtGui.QWidget(self.tabWidgetPage1)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout_3.setMargin(0)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.cbxDigits = QtGui.QCheckBox(self.widget)
        self.cbxDigits.setObjectName(_fromUtf8("cbxDigits"))
        self.horizontalLayout_3.addWidget(self.cbxDigits)
        self.spinDigits = QtGui.QSpinBox(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinDigits.sizePolicy().hasHeightForWidth())
        self.spinDigits.setSizePolicy(sizePolicy)
        self.spinDigits.setMaximum(99)
        self.spinDigits.setProperty("value", 2)
        self.spinDigits.setObjectName(_fromUtf8("spinDigits"))
        self.horizontalLayout_3.addWidget(self.spinDigits)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.verticalLayout_2.addWidget(self.widget)
        self.tableWidget = QtGui.QTableWidget(self.tabWidgetPage1)
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.verticalLayout_2.addWidget(self.tableWidget)
        self.tabWidget.addTab(self.tabWidgetPage1, _fromUtf8(""))
        self.tabWidgetPage2 = QtGui.QWidget()
        self.tabWidgetPage2.setObjectName(_fromUtf8("tabWidgetPage2"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.tabWidgetPage2)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.graphControls = QtGui.QWidget(self.tabWidgetPage2)
        self.graphControls.setObjectName(_fromUtf8("graphControls"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.graphControls)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.cbxStats = QtGui.QCheckBox(self.graphControls)
        self.cbxStats.setObjectName(_fromUtf8("cbxStats"))
        self.horizontalLayout_2.addWidget(self.cbxStats)
        self.label = QtGui.QLabel(self.graphControls)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_2.addWidget(self.label)
        self.leYMin = QtGui.QLineEdit(self.graphControls)
        self.leYMin.setObjectName(_fromUtf8("leYMin"))
        self.horizontalLayout_2.addWidget(self.leYMin)
        self.label_2 = QtGui.QLabel(self.graphControls)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_2.addWidget(self.label_2)
        self.leYMax = QtGui.QLineEdit(self.graphControls)
        self.leYMax.setObjectName(_fromUtf8("leYMax"))
        self.horizontalLayout_2.addWidget(self.leYMax)
        self.plotSelector = QtGui.QComboBox(self.graphControls)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plotSelector.sizePolicy().hasHeightForWidth())
        self.plotSelector.setSizePolicy(sizePolicy)
        self.plotSelector.setObjectName(_fromUtf8("plotSelector"))
        self.horizontalLayout_2.addWidget(self.plotSelector)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout_3.addWidget(self.graphControls)
        self.stackedWidget = QtGui.QStackedWidget(self.tabWidgetPage2)
        self.stackedWidget.setObjectName(_fromUtf8("stackedWidget"))
        self.verticalLayout_3.addWidget(self.stackedWidget)
        self.tabWidget.addTab(self.tabWidgetPage2, _fromUtf8(""))
        self.tabWidgetPage3 = QtGui.QWidget()
        self.tabWidgetPage3.setObjectName(_fromUtf8("tabWidgetPage3"))
        self.gridLayout_3 = QtGui.QGridLayout(self.tabWidgetPage3)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.label_4 = QtGui.QLabel(self.tabWidgetPage3)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout_2.addWidget(self.label_4, 2, 0, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem2, 1, 2, 1, 1)
        self.label_3 = QtGui.QLabel(self.tabWidgetPage3)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_2.addWidget(self.label_3, 1, 0, 1, 1)
        self.cbxLayers = QtGui.QComboBox(self.tabWidgetPage3)
        self.cbxLayers.setObjectName(_fromUtf8("cbxLayers"))
        self.cbxLayers.addItem(_fromUtf8(""))
        self.cbxLayers.addItem(_fromUtf8(""))
        self.cbxLayers.addItem(_fromUtf8(""))
        self.cbxLayers.addItem(_fromUtf8(""))
        self.gridLayout_2.addWidget(self.cbxLayers, 1, 1, 1, 1)
        self.cbxBands = QtGui.QComboBox(self.tabWidgetPage3)
        self.cbxBands.setObjectName(_fromUtf8("cbxBands"))
        self.cbxBands.addItem(_fromUtf8(""))
        self.cbxBands.addItem(_fromUtf8(""))
        self.cbxBands.addItem(_fromUtf8(""))
        self.gridLayout_2.addWidget(self.cbxBands, 2, 1, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_2, 2, 0, 1, 1)
        self.line = QtGui.QFrame(self.tabWidgetPage3)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.gridLayout_3.addWidget(self.line, 1, 0, 1, 1)
        self.cbxClick = QtGui.QCheckBox(self.tabWidgetPage3)
        self.cbxClick.setObjectName(_fromUtf8("cbxClick"))
        self.gridLayout_3.addWidget(self.cbxClick, 0, 0, 1, 1)
        self.line_2 = QtGui.QFrame(self.tabWidgetPage3)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.gridLayout_3.addWidget(self.line_2, 3, 0, 1, 1)
        self.setActiveLayerLabel = QtGui.QLabel(self.tabWidgetPage3)
        self.setActiveLayerLabel.setObjectName(_fromUtf8("setActiveLayerLabel"))
        self.gridLayout_3.addWidget(self.setActiveLayerLabel, 4, 0, 1, 1)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.selectionStringLabel = QtGui.QLabel(self.tabWidgetPage3)
        self.selectionStringLabel.setObjectName(_fromUtf8("selectionStringLabel"))
        self.gridLayout.addWidget(self.selectionStringLabel, 0, 0, 1, 1)
        self.selectionStringLineEdit = QtGui.QLineEdit(self.tabWidgetPage3)
        self.selectionStringLineEdit.setEnabled(False)
        self.selectionStringLineEdit.setObjectName(_fromUtf8("selectionStringLineEdit"))
        self.gridLayout.addWidget(self.selectionStringLineEdit, 0, 1, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout, 5, 0, 1, 1)
        self.line_3 = QtGui.QFrame(self.tabWidgetPage3)
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.gridLayout_3.addWidget(self.line_3, 6, 0, 1, 1)
        self.label_5 = QtGui.QLabel(self.tabWidgetPage3)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout_3.addWidget(self.label_5, 7, 0, 1, 1)
        self.tableWidget2 = QtGui.QTableWidget(self.tabWidgetPage3)
        self.tableWidget2.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tableWidget2.setObjectName(_fromUtf8("tableWidget2"))
        self.tableWidget2.setColumnCount(4)
        self.tableWidget2.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidget2.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget2.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget2.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget2.setHorizontalHeaderItem(3, item)
        self.gridLayout_3.addWidget(self.tableWidget2, 8, 0, 1, 1)
        self.tabWidget.addTab(self.tabWidgetPage3, _fromUtf8(""))
        self.tabWidgetPage4 = QtGui.QWidget()
        self.tabWidgetPage4.setObjectName(_fromUtf8("tabWidgetPage4"))
        self.gridLayout_5 = QtGui.QGridLayout(self.tabWidgetPage4)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.priorityLabel = QtGui.QLabel(self.tabWidgetPage4)
        self.priorityLabel.setEnabled(False)
        self.priorityLabel.setObjectName(_fromUtf8("priorityLabel"))
        self.gridLayout_5.addWidget(self.priorityLabel, 1, 0, 1, 2)
        self.patternLabel = QtGui.QLabel(self.tabWidgetPage4)
        self.patternLabel.setEnabled(False)
        self.patternLabel.setObjectName(_fromUtf8("patternLabel"))
        self.gridLayout_5.addWidget(self.patternLabel, 3, 0, 1, 1)
        self.patternLineEdit = QtGui.QLineEdit(self.tabWidgetPage4)
        self.patternLineEdit.setEnabled(False)
        self.patternLineEdit.setObjectName(_fromUtf8("patternLineEdit"))
        self.gridLayout_5.addWidget(self.patternLineEdit, 3, 1, 1, 1)
        self.writeMetaDataCheckBox = QtGui.QCheckBox(self.tabWidgetPage4)
        self.writeMetaDataCheckBox.setEnabled(False)
        self.writeMetaDataCheckBox.setChecked(True)
        self.writeMetaDataCheckBox.setObjectName(_fromUtf8("writeMetaDataCheckBox"))
        self.gridLayout_5.addWidget(self.writeMetaDataCheckBox, 4, 0, 1, 2)
        self.enableMTAnalysesCheckBox = QtGui.QCheckBox(self.tabWidgetPage4)
        self.enableMTAnalysesCheckBox.setObjectName(_fromUtf8("enableMTAnalysesCheckBox"))
        self.gridLayout_5.addWidget(self.enableMTAnalysesCheckBox, 0, 0, 1, 2)
        self.extractionPriorityListWidget = QtGui.QListWidget(self.tabWidgetPage4)
        self.extractionPriorityListWidget.setEnabled(False)
        self.extractionPriorityListWidget.setDragDropMode(QtGui.QAbstractItemView.InternalMove)
        self.extractionPriorityListWidget.setDefaultDropAction(QtCore.Qt.MoveAction)
        self.extractionPriorityListWidget.setObjectName(_fromUtf8("extractionPriorityListWidget"))
        item = QtGui.QListWidgetItem()
        item.setCheckState(QtCore.Qt.Checked)
        self.extractionPriorityListWidget.addItem(item)
        item = QtGui.QListWidgetItem()
        item.setCheckState(QtCore.Qt.Checked)
        self.extractionPriorityListWidget.addItem(item)
        item = QtGui.QListWidgetItem()
        item.setCheckState(QtCore.Qt.Checked)
        self.extractionPriorityListWidget.addItem(item)
        item = QtGui.QListWidgetItem()
        item.setCheckState(QtCore.Qt.Checked)
        self.extractionPriorityListWidget.addItem(item)
        self.gridLayout_5.addWidget(self.extractionPriorityListWidget, 2, 0, 1, 2)
        self.tabWidget.addTab(self.tabWidgetPage4, _fromUtf8(""))
        self.verticalLayout.addWidget(self.tabWidget)
        self.labelStatus = QtGui.QLabel(ValueWidgetBase)
        self.labelStatus.setText(_fromUtf8(""))
        self.labelStatus.setObjectName(_fromUtf8("labelStatus"))
        self.verticalLayout.addWidget(self.labelStatus)

        self.retranslateUi(ValueWidgetBase)
        self.tabWidget.setCurrentIndex(2)
        self.stackedWidget.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(ValueWidgetBase)

    def retranslateUi(self, ValueWidgetBase):
        ValueWidgetBase.setWindowTitle(_translate("ValueWidgetBase", "Form", None))
        self.cbxEnable.setToolTip(_translate("ValueWidgetBase", "Can also be enabled using the \"Value Tool\" toolbar icon", None))
        self.cbxEnable.setText(_translate("ValueWidgetBase", "Enable", None))
        self.cbxDigits.setToolTip(_translate("ValueWidgetBase", "Specify how many digits to show in table", None))
        self.cbxDigits.setText(_translate("ValueWidgetBase", "Decimals", None))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("ValueWidgetBase", "Layer", None))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("ValueWidgetBase", "Value", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabWidgetPage1), _translate("ValueWidgetBase", "Table", None))
        self.cbxStats.setToolTip(_translate("ValueWidgetBase", "Compute min/max when layers are loaded", None))
        self.cbxStats.setText(_translate("ValueWidgetBase", "Stats", None))
        self.label.setText(_translate("ValueWidgetBase", "Y min", None))
        self.label_2.setText(_translate("ValueWidgetBase", "Y max", None))
        self.plotSelector.setToolTip(_translate("ValueWidgetBase", "Select plotting toolkit", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabWidgetPage2), _translate("ValueWidgetBase", "Graph", None))
        self.label_4.setText(_translate("ValueWidgetBase", "Show bands:", None))
        self.label_3.setText(_translate("ValueWidgetBase", "Show layers:", None))
        self.cbxLayers.setItemText(0, _translate("ValueWidgetBase", "Visible layers", None))
        self.cbxLayers.setItemText(1, _translate("ValueWidgetBase", "All layers", None))
        self.cbxLayers.setItemText(2, _translate("ValueWidgetBase", "Manual selection", None))
        self.cbxLayers.setItemText(3, _translate("ValueWidgetBase", "By selection string", None))
        self.cbxBands.setItemText(0, _translate("ValueWidgetBase", "All bands", None))
        self.cbxBands.setItemText(1, _translate("ValueWidgetBase", "Active bands", None))
        self.cbxBands.setItemText(2, _translate("ValueWidgetBase", "Selected bands", None))
        self.cbxClick.setToolTip(_translate("ValueWidgetBase", "Replaces active map tool. Use this to select a particular point or if plotting is slow (e.g. when using mpl Graph).", None))
        self.cbxClick.setText(_translate("ValueWidgetBase", "Plot values only when mouse is clicked", None))
        self.setActiveLayerLabel.setText(_translate("ValueWidgetBase", "Select active layer by selection string:", None))
        self.selectionStringLabel.setText(_translate("ValueWidgetBase", "Selection string:", None))
        self.selectionStringLineEdit.setText(_translate("ValueWidgetBase", "MYD09CMG.A2002186.005.*.hdf ", None))
        self.label_5.setText(_translate("ValueWidgetBase", "Select active layers and display options:", None))
        item = self.tableWidget2.horizontalHeaderItem(0)
        item.setToolTip(_translate("ValueWidgetBase", "Select layers", None))
        item = self.tableWidget2.horizontalHeaderItem(1)
        item.setText(_translate("ValueWidgetBase", "Layer", None))
        item = self.tableWidget2.horizontalHeaderItem(2)
        item.setText(_translate("ValueWidgetBase", "#", None))
        item.setToolTip(_translate("ValueWidgetBase", "Select bands", None))
        item = self.tableWidget2.horizontalHeaderItem(3)
        item.setText(_translate("ValueWidgetBase", "Bands", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabWidgetPage3), _translate("ValueWidgetBase", "Options", None))
        self.priorityLabel.setText(_translate("ValueWidgetBase", "Extract time from (highest priority on top):", None))
        self.patternLabel.setText(_translate("ValueWidgetBase", "Pattern:", None))
        self.patternLineEdit.setText(_translate("ValueWidgetBase", "MYD09CMG.A2002186.005.%Y%j%H%M%S.hdf ", None))
        self.writeMetaDataCheckBox.setText(_translate("ValueWidgetBase", "Write time to metadata (overwrite existing)", None))
        self.enableMTAnalysesCheckBox.setToolTip(_translate("ValueWidgetBase", "If you enable this Option your data will be reorder chronologically and points with no data will be omitted in the graph.", None))
        self.enableMTAnalysesCheckBox.setText(_translate("ValueWidgetBase", "Enable multi-temporal analysis", None))
        __sortingEnabled = self.extractionPriorityListWidget.isSortingEnabled()
        self.extractionPriorityListWidget.setSortingEnabled(False)
        item = self.extractionPriorityListWidget.item(0)
        item.setText(_translate("ValueWidgetBase", "GDALPamDataset", None))
        item = self.extractionPriorityListWidget.item(1)
        item.setText(_translate("ValueWidgetBase", "Filename", None))
        item = self.extractionPriorityListWidget.item(2)
        item.setText(_translate("ValueWidgetBase", "Exif", None))
        item = self.extractionPriorityListWidget.item(3)
        item.setText(_translate("ValueWidgetBase", "TIFF-Header", None))
        self.extractionPriorityListWidget.setSortingEnabled(__sortingEnabled)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabWidgetPage4), _translate("ValueWidgetBase", "Time", None))

