# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_valuewidgetbase.ui'
#
# Created: Tue Dec 16 16:45:57 2014
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
        ValueWidgetBase.resize(320, 411)
        self.gridLayout = QtGui.QGridLayout(ValueWidgetBase)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.toggleValueTool = QtGui.QCheckBox(ValueWidgetBase)
        self.toggleValueTool.setObjectName(_fromUtf8("toggleValueTool"))
        self.gridLayout.addWidget(self.toggleValueTool, 0, 0, 1, 1)
        self.toggleFilter = QtGui.QCheckBox(ValueWidgetBase)
        self.toggleFilter.setEnabled(False)
        self.toggleFilter.setObjectName(_fromUtf8("toggleFilter"))
        self.gridLayout.addWidget(self.toggleFilter, 0, 2, 1, 1)
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
        self.exportPushButton = QtGui.QPushButton(self.widget)
        self.exportPushButton.setObjectName(_fromUtf8("exportPushButton"))
        self.horizontalLayout_3.addWidget(self.exportPushButton)
        self.verticalLayout_2.addWidget(self.widget)
        self.valueTable = QtGui.QTableWidget(self.tabWidgetPage1)
        self.valueTable.setObjectName(_fromUtf8("valueTable"))
        self.valueTable.setColumnCount(3)
        self.valueTable.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.valueTable.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.valueTable.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.valueTable.setHorizontalHeaderItem(2, item)
        self.verticalLayout_2.addWidget(self.valueTable)
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
        self.enableStatistics = QtGui.QCheckBox(self.graphControls)
        self.enableStatistics.setObjectName(_fromUtf8("enableStatistics"))
        self.horizontalLayout_2.addWidget(self.enableStatistics)
        self.yAutoCheckBox = QtGui.QCheckBox(self.graphControls)
        self.yAutoCheckBox.setEnabled(True)
        self.yAutoCheckBox.setChecked(True)
        self.yAutoCheckBox.setObjectName(_fromUtf8("yAutoCheckBox"))
        self.horizontalLayout_2.addWidget(self.yAutoCheckBox)
        self.minYLabel = QtGui.QLabel(self.graphControls)
        self.minYLabel.setEnabled(True)
        self.minYLabel.setObjectName(_fromUtf8("minYLabel"))
        self.horizontalLayout_2.addWidget(self.minYLabel)
        self.leYMin = QtGui.QLineEdit(self.graphControls)
        self.leYMin.setEnabled(False)
        self.leYMin.setObjectName(_fromUtf8("leYMin"))
        self.horizontalLayout_2.addWidget(self.leYMin)
        self.maxYLabel = QtGui.QLabel(self.graphControls)
        self.maxYLabel.setEnabled(True)
        self.maxYLabel.setObjectName(_fromUtf8("maxYLabel"))
        self.horizontalLayout_2.addWidget(self.maxYLabel)
        self.leYMax = QtGui.QLineEdit(self.graphControls)
        self.leYMax.setEnabled(False)
        self.leYMax.setObjectName(_fromUtf8("leYMax"))
        self.horizontalLayout_2.addWidget(self.leYMax)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout_3.addWidget(self.graphControls)
        self.plotLibSelector = QtGui.QComboBox(self.tabWidgetPage2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plotLibSelector.sizePolicy().hasHeightForWidth())
        self.plotLibSelector.setSizePolicy(sizePolicy)
        self.plotLibSelector.setObjectName(_fromUtf8("plotLibSelector"))
        self.verticalLayout_3.addWidget(self.plotLibSelector)
        self.stackedWidget = QtGui.QStackedWidget(self.tabWidgetPage2)
        self.stackedWidget.setEnabled(True)
        self.stackedWidget.setObjectName(_fromUtf8("stackedWidget"))
        self.verticalLayout_3.addWidget(self.stackedWidget)
        self.tabWidget.addTab(self.tabWidgetPage2, _fromUtf8(""))
        self.tabWidgetPage3 = QtGui.QWidget()
        self.tabWidgetPage3.setObjectName(_fromUtf8("tabWidgetPage3"))
        self.gridLayout_3 = QtGui.QGridLayout(self.tabWidgetPage3)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.selectLayerGrid = QtGui.QGridLayout()
        self.selectLayerGrid.setObjectName(_fromUtf8("selectLayerGrid"))
        self.bandSelectionLabel = QtGui.QLabel(self.tabWidgetPage3)
        self.bandSelectionLabel.setObjectName(_fromUtf8("bandSelectionLabel"))
        self.selectLayerGrid.addWidget(self.bandSelectionLabel, 2, 0, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.selectLayerGrid.addItem(spacerItem2, 1, 2, 1, 1)
        self.layerSelectionLabel = QtGui.QLabel(self.tabWidgetPage3)
        self.layerSelectionLabel.setObjectName(_fromUtf8("layerSelectionLabel"))
        self.selectLayerGrid.addWidget(self.layerSelectionLabel, 1, 0, 1, 1)
        self.layerSelection = QtGui.QComboBox(self.tabWidgetPage3)
        self.layerSelection.setObjectName(_fromUtf8("layerSelection"))
        self.layerSelection.addItem(_fromUtf8(""))
        self.layerSelection.addItem(_fromUtf8(""))
        self.layerSelection.addItem(_fromUtf8(""))
        self.layerSelection.addItem(_fromUtf8(""))
        self.selectLayerGrid.addWidget(self.layerSelection, 1, 1, 1, 1)
        self.bandSelection = QtGui.QComboBox(self.tabWidgetPage3)
        self.bandSelection.setObjectName(_fromUtf8("bandSelection"))
        self.bandSelection.addItem(_fromUtf8(""))
        self.bandSelection.addItem(_fromUtf8(""))
        self.bandSelection.addItem(_fromUtf8(""))
        self.selectLayerGrid.addWidget(self.bandSelection, 2, 1, 1, 1)
        self.gridLayout_3.addLayout(self.selectLayerGrid, 2, 0, 1, 1)
        self.line = QtGui.QFrame(self.tabWidgetPage3)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.gridLayout_3.addWidget(self.line, 1, 0, 1, 1)
        self.plotOnMove = QtGui.QCheckBox(self.tabWidgetPage3)
        self.plotOnMove.setObjectName(_fromUtf8("plotOnMove"))
        self.gridLayout_3.addWidget(self.plotOnMove, 0, 0, 1, 1)
        self.line_2 = QtGui.QFrame(self.tabWidgetPage3)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.gridLayout_3.addWidget(self.line_2, 3, 0, 1, 1)
        self.setActiveLayerLabel = QtGui.QLabel(self.tabWidgetPage3)
        self.setActiveLayerLabel.setObjectName(_fromUtf8("setActiveLayerLabel"))
        self.gridLayout_3.addWidget(self.setActiveLayerLabel, 4, 0, 1, 1)
        self.selectStringGrid = QtGui.QGridLayout()
        self.selectStringGrid.setObjectName(_fromUtf8("selectStringGrid"))
        self.selectionStringLabel = QtGui.QLabel(self.tabWidgetPage3)
        self.selectionStringLabel.setObjectName(_fromUtf8("selectionStringLabel"))
        self.selectStringGrid.addWidget(self.selectionStringLabel, 0, 0, 1, 1)
        self.selectionStringLineEdit = QtGui.QLineEdit(self.tabWidgetPage3)
        self.selectionStringLineEdit.setEnabled(False)
        self.selectionStringLineEdit.setObjectName(_fromUtf8("selectionStringLineEdit"))
        self.selectStringGrid.addWidget(self.selectionStringLineEdit, 0, 1, 1, 1)
        self.gridLayout_3.addLayout(self.selectStringGrid, 5, 0, 1, 1)
        self.line_3 = QtGui.QFrame(self.tabWidgetPage3)
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.gridLayout_3.addWidget(self.line_3, 6, 0, 1, 1)
        self.label_5 = QtGui.QLabel(self.tabWidgetPage3)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout_3.addWidget(self.label_5, 7, 0, 1, 1)
        self.selectionTable = QtGui.QTableWidget(self.tabWidgetPage3)
        self.selectionTable.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.selectionTable.setObjectName(_fromUtf8("selectionTable"))
        self.selectionTable.setColumnCount(4)
        self.selectionTable.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.selectionTable.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.selectionTable.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.selectionTable.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.selectionTable.setHorizontalHeaderItem(3, item)
        self.gridLayout_3.addWidget(self.selectionTable, 8, 0, 1, 1)
        self.tabWidget.addTab(self.tabWidgetPage3, _fromUtf8(""))
        self.multitemporalTabWidget = QtGui.QWidget()
        self.multitemporalTabWidget.setObjectName(_fromUtf8("multitemporalTabWidget"))
        self.formLayout = QtGui.QFormLayout(self.multitemporalTabWidget)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.enableMTAnalysesCheckBox = QtGui.QCheckBox(self.multitemporalTabWidget)
        self.enableMTAnalysesCheckBox.setObjectName(_fromUtf8("enableMTAnalysesCheckBox"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.SpanningRole, self.enableMTAnalysesCheckBox)
        self.priorityLabel = QtGui.QLabel(self.multitemporalTabWidget)
        self.priorityLabel.setEnabled(False)
        self.priorityLabel.setObjectName(_fromUtf8("priorityLabel"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.SpanningRole, self.priorityLabel)
        self.extractionPriorityListWidget = QtGui.QListWidget(self.multitemporalTabWidget)
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
        item.setCheckState(QtCore.Qt.Unchecked)
        self.extractionPriorityListWidget.addItem(item)
        item = QtGui.QListWidgetItem()
        item.setCheckState(QtCore.Qt.Unchecked)
        self.extractionPriorityListWidget.addItem(item)
        self.formLayout.setWidget(2, QtGui.QFormLayout.SpanningRole, self.extractionPriorityListWidget)
        self.cutFirst = QtGui.QSpinBox(self.multitemporalTabWidget)
        self.cutFirst.setMaximum(999)
        self.cutFirst.setObjectName(_fromUtf8("cutFirst"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.SpanningRole, self.cutFirst)
        self.dateLength = QtGui.QSpinBox(self.multitemporalTabWidget)
        self.dateLength.setMaximum(999)
        self.dateLength.setProperty("value", 0)
        self.dateLength.setObjectName(_fromUtf8("dateLength"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.SpanningRole, self.dateLength)
        self.sampleLabel = QtGui.QLabel(self.multitemporalTabWidget)
        self.sampleLabel.setObjectName(_fromUtf8("sampleLabel"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.LabelRole, self.sampleLabel)
        self.sampleLineEdit = QtGui.QLineEdit(self.multitemporalTabWidget)
        self.sampleLineEdit.setReadOnly(True)
        self.sampleLineEdit.setObjectName(_fromUtf8("sampleLineEdit"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.FieldRole, self.sampleLineEdit)
        self.patternLabel = QtGui.QLabel(self.multitemporalTabWidget)
        self.patternLabel.setEnabled(False)
        self.patternLabel.setObjectName(_fromUtf8("patternLabel"))
        self.formLayout.setWidget(6, QtGui.QFormLayout.LabelRole, self.patternLabel)
        self.patternLineEdit = QtGui.QLineEdit(self.multitemporalTabWidget)
        self.patternLineEdit.setEnabled(False)
        self.patternLineEdit.setObjectName(_fromUtf8("patternLineEdit"))
        self.formLayout.setWidget(6, QtGui.QFormLayout.FieldRole, self.patternLineEdit)
        self.writeMetaDataCheckBox = QtGui.QCheckBox(self.multitemporalTabWidget)
        self.writeMetaDataCheckBox.setEnabled(False)
        self.writeMetaDataCheckBox.setChecked(True)
        self.writeMetaDataCheckBox.setObjectName(_fromUtf8("writeMetaDataCheckBox"))
        self.formLayout.setWidget(7, QtGui.QFormLayout.SpanningRole, self.writeMetaDataCheckBox)
        self.tabWidget.addTab(self.multitemporalTabWidget, _fromUtf8(""))
        self.gridLayout.addWidget(self.tabWidget, 1, 0, 1, 3)
        self.labelStatus = QtGui.QLabel(ValueWidgetBase)
        self.labelStatus.setText(_fromUtf8(""))
        self.labelStatus.setObjectName(_fromUtf8("labelStatus"))
        self.gridLayout.addWidget(self.labelStatus, 2, 0, 1, 1)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 0, 1, 1, 1)

        self.retranslateUi(ValueWidgetBase)
        self.tabWidget.setCurrentIndex(2)
        self.stackedWidget.setCurrentIndex(-1)
        QtCore.QObject.connect(self.toggleValueTool, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.toggleFilter.setEnabled)
        QtCore.QMetaObject.connectSlotsByName(ValueWidgetBase)

    def retranslateUi(self, ValueWidgetBase):
        ValueWidgetBase.setWindowTitle(_translate("ValueWidgetBase", "Form", None))
        self.toggleValueTool.setToolTip(_translate("ValueWidgetBase", "Can also be enabled using the \"Value Tool\" toolbar icon", None))
        self.toggleValueTool.setText(_translate("ValueWidgetBase", "Enable", None))
        self.toggleFilter.setToolTip(_translate("ValueWidgetBase", "Can also be enabled using the \"Value Tool\" toolbar icon", None))
        self.toggleFilter.setText(_translate("ValueWidgetBase", "Enable Filtering", None))
        self.cbxDigits.setToolTip(_translate("ValueWidgetBase", "Specify how many digits to show in table", None))
        self.cbxDigits.setText(_translate("ValueWidgetBase", "Decimals", None))
        self.exportPushButton.setText(_translate("ValueWidgetBase", "Export to CSV", None))
        self.valueTable.setSortingEnabled(True)
        item = self.valueTable.horizontalHeaderItem(0)
        item.setText(_translate("ValueWidgetBase", "Layer", None))
        item = self.valueTable.horizontalHeaderItem(1)
        item.setText(_translate("ValueWidgetBase", "Value", None))
        item = self.valueTable.horizontalHeaderItem(2)
        item.setText(_translate("ValueWidgetBase", "Date", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabWidgetPage1), _translate("ValueWidgetBase", "Table", None))
        self.enableStatistics.setToolTip(_translate("ValueWidgetBase", "Compute min/max when layers are loaded", None))
        self.enableStatistics.setText(_translate("ValueWidgetBase", "Stats", None))
        self.yAutoCheckBox.setToolTip(_translate("ValueWidgetBase", "Autozoom to min and max of all loaded values", None))
        self.yAutoCheckBox.setText(_translate("ValueWidgetBase", "Auto", None))
        self.minYLabel.setText(_translate("ValueWidgetBase", "Y min", None))
        self.maxYLabel.setText(_translate("ValueWidgetBase", "Y max", None))
        self.plotLibSelector.setToolTip(_translate("ValueWidgetBase", "Select plotting toolkit\n"
"Qwt toolkit (faster but soon unmaintained)\n"
"matplotlib (slower but maintained)\n"
"PyQtGraph (fast but lacking some features)", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabWidgetPage2), _translate("ValueWidgetBase", "Graph", None))
        self.bandSelectionLabel.setText(_translate("ValueWidgetBase", "Show bands:", None))
        self.layerSelectionLabel.setText(_translate("ValueWidgetBase", "Show layers:", None))
        self.layerSelection.setItemText(0, _translate("ValueWidgetBase", "Visible layers", None))
        self.layerSelection.setItemText(1, _translate("ValueWidgetBase", "All layers", None))
        self.layerSelection.setItemText(2, _translate("ValueWidgetBase", "Manual selection", None))
        self.layerSelection.setItemText(3, _translate("ValueWidgetBase", "By selection string", None))
        self.bandSelection.setItemText(0, _translate("ValueWidgetBase", "All bands", None))
        self.bandSelection.setItemText(1, _translate("ValueWidgetBase", "Active bands", None))
        self.bandSelection.setItemText(2, _translate("ValueWidgetBase", "Selected bands", None))
        self.plotOnMove.setToolTip(_translate("ValueWidgetBase", "Replaces active map tool. Use this to select a particular point or if plotting is slow (e.g. when using mpl Graph).", None))
        self.plotOnMove.setText(_translate("ValueWidgetBase", "Plot values only when mouse is clicked", None))
        self.setActiveLayerLabel.setText(_translate("ValueWidgetBase", "Select layers by selection string:", None))
        self.selectionStringLabel.setToolTip(_translate("ValueWidgetBase", "<html><head/><body>\n"
"<table border=\"0\">\n"
"<tr><td>*</td><td> matches everything</td></tr>\n"
"<tr><td>?</td><td> matches any single character</td></tr>\n"
"<tr><td>[seq]</td><td> matches any character in seq</td></tr>\n"
"<tr><td>[!seq]</td><td> matches any character not in seq</td></tr>\n"
"</table></body></html>", None))
        self.selectionStringLabel.setText(_translate("ValueWidgetBase", "Selection string:", None))
        self.selectionStringLineEdit.setToolTip(_translate("ValueWidgetBase", "<html><head/><body>\n"
"<table border=\"0\">\n"
"<tr><td>*</td><td> matches everything</td></tr>\n"
"<tr><td>?</td><td> matches any single character</td></tr>\n"
"<tr><td>[seq]</td><td> matches any character in seq</td></tr>\n"
"<tr><td>[!seq]</td><td> matches any character not in seq</td></tr>\n"
"</table></body></html>", None))
        self.selectionStringLineEdit.setText(_translate("ValueWidgetBase", "*1?[89][!5-8]*", None))
        self.label_5.setText(_translate("ValueWidgetBase", "Select active layers and display options:", None))
        item = self.selectionTable.horizontalHeaderItem(0)
        item.setToolTip(_translate("ValueWidgetBase", "Select layers", None))
        item = self.selectionTable.horizontalHeaderItem(1)
        item.setText(_translate("ValueWidgetBase", "Layer", None))
        item = self.selectionTable.horizontalHeaderItem(2)
        item.setText(_translate("ValueWidgetBase", "#", None))
        item.setToolTip(_translate("ValueWidgetBase", "Select bands", None))
        item = self.selectionTable.horizontalHeaderItem(3)
        item.setText(_translate("ValueWidgetBase", "Bands", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabWidgetPage3), _translate("ValueWidgetBase", "Options", None))
        self.enableMTAnalysesCheckBox.setToolTip(_translate("ValueWidgetBase", "If you enable this Option your data will be reorder chronologically and points with no data will be omitted in the graph.", None))
        self.enableMTAnalysesCheckBox.setText(_translate("ValueWidgetBase", "Enable multi-temporal analysis", None))
        self.priorityLabel.setText(_translate("ValueWidgetBase", "Extract time from (highest priority on top):", None))
        __sortingEnabled = self.extractionPriorityListWidget.isSortingEnabled()
        self.extractionPriorityListWidget.setSortingEnabled(False)
        item = self.extractionPriorityListWidget.item(0)
        item.setText(_translate("ValueWidgetBase", "XML", None))
        item = self.extractionPriorityListWidget.item(1)
        item.setText(_translate("ValueWidgetBase", "Filename", None))
        item = self.extractionPriorityListWidget.item(2)
        item.setText(_translate("ValueWidgetBase", "Exif", None))
        item = self.extractionPriorityListWidget.item(3)
        item.setText(_translate("ValueWidgetBase", "TIFF-Header", None))
        self.extractionPriorityListWidget.setSortingEnabled(__sortingEnabled)
        self.cutFirst.setSuffix(_translate("ValueWidgetBase", " characters", None))
        self.cutFirst.setPrefix(_translate("ValueWidgetBase", "Cut first ", None))
        self.dateLength.setSuffix(_translate("ValueWidgetBase", " characters long", None))
        self.dateLength.setPrefix(_translate("ValueWidgetBase", "Datestring is ", None))
        self.sampleLabel.setText(_translate("ValueWidgetBase", "Sample", None))
        self.patternLabel.setText(_translate("ValueWidgetBase", "Datepattern:", None))
        self.patternLineEdit.setText(_translate("ValueWidgetBase", "%Y%j%H%M%S", None))
        self.writeMetaDataCheckBox.setText(_translate("ValueWidgetBase", "Write time to metadata (XML)", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.multitemporalTabWidget), _translate("ValueWidgetBase", "Time", None))

