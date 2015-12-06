# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qt\ui\fontgenwidget.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
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

class Ui_FontGenWidget(object):
    def setupUi(self, FontGenWidget):
        FontGenWidget.setObjectName(_fromUtf8("FontGenWidget"))
        FontGenWidget.resize(742, 464)
        FontGenWidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.verticalLayout = QtGui.QVBoxLayout(FontGenWidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.groupBox = QtGui.QGroupBox(FontGenWidget)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.groupBox)
        self.horizontalLayout_4.setContentsMargins(-1, 4, -1, 8)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.cboFont = QtGui.QFontComboBox(self.groupBox)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Meiryo UI"))
        self.cboFont.setCurrentFont(font)
        self.cboFont.setObjectName(_fromUtf8("cboFont"))
        self.horizontalLayout_4.addWidget(self.cboFont)
        self.label_5 = QtGui.QLabel(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout_4.addWidget(self.label_5)
        self.spnFontSize = QtGui.QSpinBox(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spnFontSize.sizePolicy().hasHeightForWidth())
        self.spnFontSize.setSizePolicy(sizePolicy)
        self.spnFontSize.setMinimum(1)
        self.spnFontSize.setMaximum(128)
        self.spnFontSize.setProperty("value", 11)
        self.spnFontSize.setObjectName(_fromUtf8("spnFontSize"))
        self.horizontalLayout_4.addWidget(self.spnFontSize)
        self.label = QtGui.QLabel(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_4.addWidget(self.label)
        self.spnFontWeight = QtGui.QSpinBox(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spnFontWeight.sizePolicy().hasHeightForWidth())
        self.spnFontWeight.setSizePolicy(sizePolicy)
        self.spnFontWeight.setProperty("value", 50)
        self.spnFontWeight.setObjectName(_fromUtf8("spnFontWeight"))
        self.horizontalLayout_4.addWidget(self.spnFontWeight)
        self.verticalLayout.addWidget(self.groupBox)
        self.groupBox_2 = QtGui.QGroupBox(FontGenWidget)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout.setContentsMargins(-1, 4, -1, 8)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setSpacing(4)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.label_7 = QtGui.QLabel(self.groupBox_2)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.horizontalLayout_5.addWidget(self.label_7)
        self.spnXOffset = QtGui.QSpinBox(self.groupBox_2)
        self.spnXOffset.setMinimum(-25)
        self.spnXOffset.setMaximum(25)
        self.spnXOffset.setObjectName(_fromUtf8("spnXOffset"))
        self.horizontalLayout_5.addWidget(self.spnXOffset)
        self.verticalLayout_4.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.label_8 = QtGui.QLabel(self.groupBox_2)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.horizontalLayout_6.addWidget(self.label_8)
        self.spnYOffset = QtGui.QSpinBox(self.groupBox_2)
        self.spnYOffset.setMinimum(-25)
        self.spnYOffset.setMaximum(25)
        self.spnYOffset.setProperty("value", 0)
        self.spnYOffset.setObjectName(_fromUtf8("spnYOffset"))
        self.horizontalLayout_6.addWidget(self.spnYOffset)
        self.verticalLayout_4.addLayout(self.horizontalLayout_6)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setSpacing(4)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.label_2 = QtGui.QLabel(self.groupBox_2)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_7.addWidget(self.label_2)
        self.spnXMargin = QtGui.QSpinBox(self.groupBox_2)
        self.spnXMargin.setProperty("value", 2)
        self.spnXMargin.setObjectName(_fromUtf8("spnXMargin"))
        self.horizontalLayout_7.addWidget(self.spnXMargin)
        self.verticalLayout_5.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.label_10 = QtGui.QLabel(self.groupBox_2)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.horizontalLayout_8.addWidget(self.label_10)
        self.spnYMargin = QtGui.QSpinBox(self.groupBox_2)
        self.spnYMargin.setProperty("value", 2)
        self.spnYMargin.setObjectName(_fromUtf8("spnYMargin"))
        self.horizontalLayout_8.addWidget(self.spnYMargin)
        self.verticalLayout_5.addLayout(self.horizontalLayout_8)
        self.horizontalLayout.addLayout(self.verticalLayout_5)
        self.horizontalLayout_11 = QtGui.QHBoxLayout()
        self.horizontalLayout_11.setObjectName(_fromUtf8("horizontalLayout_11"))
        self.label_12 = QtGui.QLabel(self.groupBox_2)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.horizontalLayout_11.addWidget(self.label_12)
        self.spnYShift = QtGui.QSpinBox(self.groupBox_2)
        self.spnYShift.setMinimum(-128)
        self.spnYShift.setMaximum(127)
        self.spnYShift.setProperty("value", 0)
        self.spnYShift.setObjectName(_fromUtf8("spnYShift"))
        self.horizontalLayout_11.addWidget(self.spnYShift)
        self.horizontalLayout.addLayout(self.horizontalLayout_11)
        self.chkTrace = QtGui.QGroupBox(self.groupBox_2)
        self.chkTrace.setCheckable(True)
        self.chkTrace.setChecked(True)
        self.chkTrace.setObjectName(_fromUtf8("chkTrace"))
        self.horizontalLayout_13 = QtGui.QHBoxLayout(self.chkTrace)
        self.horizontalLayout_13.setContentsMargins(-1, 4, -1, 8)
        self.horizontalLayout_13.setSpacing(6)
        self.horizontalLayout_13.setObjectName(_fromUtf8("horizontalLayout_13"))
        self.label_6 = QtGui.QLabel(self.chkTrace)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.horizontalLayout_13.addWidget(self.label_6)
        self.spnPenSize = QtGui.QDoubleSpinBox(self.chkTrace)
        self.spnPenSize.setEnabled(True)
        self.spnPenSize.setDecimals(4)
        self.spnPenSize.setMinimum(0.0001)
        self.spnPenSize.setSingleStep(0.01)
        self.spnPenSize.setProperty("value", 0.3333)
        self.spnPenSize.setObjectName(_fromUtf8("spnPenSize"))
        self.horizontalLayout_13.addWidget(self.spnPenSize)
        self.label_13 = QtGui.QLabel(self.chkTrace)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.horizontalLayout_13.addWidget(self.label_13)
        self.cboPenCap = QtGui.QComboBox(self.chkTrace)
        self.cboPenCap.setObjectName(_fromUtf8("cboPenCap"))
        self.cboPenCap.addItem(_fromUtf8(""))
        self.cboPenCap.addItem(_fromUtf8(""))
        self.cboPenCap.addItem(_fromUtf8(""))
        self.horizontalLayout_13.addWidget(self.cboPenCap)
        self.label_14 = QtGui.QLabel(self.chkTrace)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.horizontalLayout_13.addWidget(self.label_14)
        self.cboPenJoin = QtGui.QComboBox(self.chkTrace)
        self.cboPenJoin.setObjectName(_fromUtf8("cboPenJoin"))
        self.cboPenJoin.addItem(_fromUtf8(""))
        self.cboPenJoin.addItem(_fromUtf8(""))
        self.cboPenJoin.addItem(_fromUtf8(""))
        self.cboPenJoin.addItem(_fromUtf8(""))
        self.horizontalLayout_13.addWidget(self.cboPenJoin)
        self.horizontalLayout.addWidget(self.chkTrace)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addWidget(self.groupBox_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.label_3 = QtGui.QLabel(FontGenWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout_2.addWidget(self.label_3)
        self.lblPreview = QtGui.QLabel(FontGenWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblPreview.sizePolicy().hasHeightForWidth())
        self.lblPreview.setSizePolicy(sizePolicy)
        self.lblPreview.setMinimumSize(QtCore.QSize(256, 256))
        self.lblPreview.setMaximumSize(QtCore.QSize(256, 16777215))
        self.lblPreview.setStyleSheet(_fromUtf8("background-color: black;"))
        self.lblPreview.setFrameShape(QtGui.QFrame.StyledPanel)
        self.lblPreview.setFrameShadow(QtGui.QFrame.Sunken)
        self.lblPreview.setText(_fromUtf8(""))
        self.lblPreview.setObjectName(_fromUtf8("lblPreview"))
        self.verticalLayout_2.addWidget(self.lblPreview)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.chkBoundingBoxes = QtGui.QCheckBox(FontGenWidget)
        self.chkBoundingBoxes.setChecked(True)
        self.chkBoundingBoxes.setObjectName(_fromUtf8("chkBoundingBoxes"))
        self.horizontalLayout_2.addWidget(self.chkBoundingBoxes)
        self.chkAutoRefresh = QtGui.QCheckBox(FontGenWidget)
        self.chkAutoRefresh.setChecked(True)
        self.chkAutoRefresh.setObjectName(_fromUtf8("chkAutoRefresh"))
        self.horizontalLayout_2.addWidget(self.chkAutoRefresh)
        self.btnRefreshPreview = QtGui.QPushButton(FontGenWidget)
        self.btnRefreshPreview.setObjectName(_fromUtf8("btnRefreshPreview"))
        self.horizontalLayout_2.addWidget(self.btnRefreshPreview)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.label_4 = QtGui.QLabel(FontGenWidget)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout_3.addWidget(self.label_4)
        self.txtChars = QtGui.QTextEdit(FontGenWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txtChars.sizePolicy().hasHeightForWidth())
        self.txtChars.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Meiryo UI"))
        font.setPointSize(11)
        self.txtChars.setFont(font)
        self.txtChars.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.txtChars.setObjectName(_fromUtf8("txtChars"))
        self.verticalLayout_3.addWidget(self.txtChars)
        self.horizontalLayout_3.addLayout(self.verticalLayout_3)
        self.verticalLayout_7 = QtGui.QVBoxLayout()
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.label_9 = QtGui.QLabel(FontGenWidget)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.verticalLayout_7.addWidget(self.label_9)
        self.treeSubs = QtGui.QTreeWidget(FontGenWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.treeSubs.sizePolicy().hasHeightForWidth())
        self.treeSubs.setSizePolicy(sizePolicy)
        self.treeSubs.setMaximumSize(QtCore.QSize(192, 16777215))
        self.treeSubs.setMidLineWidth(0)
        self.treeSubs.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.treeSubs.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.treeSubs.setAlternatingRowColors(True)
        self.treeSubs.setRootIsDecorated(False)
        self.treeSubs.setUniformRowHeights(True)
        self.treeSubs.setItemsExpandable(False)
        self.treeSubs.setObjectName(_fromUtf8("treeSubs"))
        item_0 = QtGui.QTreeWidgetItem(self.treeSubs)
        item_0 = QtGui.QTreeWidgetItem(self.treeSubs)
        self.treeSubs.header().setDefaultSectionSize(36)
        self.treeSubs.header().setMinimumSectionSize(0)
        self.treeSubs.header().setStretchLastSection(True)
        self.verticalLayout_7.addWidget(self.treeSubs)
        self.horizontalLayout_12 = QtGui.QHBoxLayout()
        self.horizontalLayout_12.setObjectName(_fromUtf8("horizontalLayout_12"))
        self.btnNewSub = QtGui.QPushButton(FontGenWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnNewSub.sizePolicy().hasHeightForWidth())
        self.btnNewSub.setSizePolicy(sizePolicy)
        self.btnNewSub.setText(_fromUtf8(""))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/new.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnNewSub.setIcon(icon)
        self.btnNewSub.setObjectName(_fromUtf8("btnNewSub"))
        self.horizontalLayout_12.addWidget(self.btnNewSub)
        self.btnDelSub = QtGui.QPushButton(FontGenWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnDelSub.sizePolicy().hasHeightForWidth())
        self.btnDelSub.setSizePolicy(sizePolicy)
        self.btnDelSub.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/cross.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnDelSub.setIcon(icon1)
        self.btnDelSub.setObjectName(_fromUtf8("btnDelSub"))
        self.horizontalLayout_12.addWidget(self.btnDelSub)
        self.label_11 = QtGui.QLabel(FontGenWidget)
        self.label_11.setText(_fromUtf8(""))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.horizontalLayout_12.addWidget(self.label_11)
        self.verticalLayout_7.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_3.addLayout(self.verticalLayout_7)
        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.retranslateUi(FontGenWidget)
        self.cboPenCap.setCurrentIndex(2)
        self.cboPenJoin.setCurrentIndex(2)
        QtCore.QObject.connect(self.cboFont, QtCore.SIGNAL(_fromUtf8("currentFontChanged(QFont)")), FontGenWidget.font_changed)
        QtCore.QObject.connect(self.spnFontSize, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), FontGenWidget.font_changed)
        QtCore.QObject.connect(self.spnFontWeight, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), FontGenWidget.font_changed)
        QtCore.QObject.connect(self.spnXOffset, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), FontGenWidget.adv_changed)
        QtCore.QObject.connect(self.spnYOffset, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), FontGenWidget.adv_changed)
        QtCore.QObject.connect(self.btnRefreshPreview, QtCore.SIGNAL(_fromUtf8("clicked()")), FontGenWidget.update_preview)
        QtCore.QObject.connect(self.spnXMargin, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), FontGenWidget.adv_changed)
        QtCore.QObject.connect(self.spnYMargin, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), FontGenWidget.adv_changed)
        QtCore.QObject.connect(self.spnYShift, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), FontGenWidget.adv_changed)
        QtCore.QObject.connect(self.chkBoundingBoxes, QtCore.SIGNAL(_fromUtf8("stateChanged(int)")), FontGenWidget.auto_update)
        QtCore.QObject.connect(self.spnPenSize, QtCore.SIGNAL(_fromUtf8("valueChanged(double)")), FontGenWidget.adv_changed)
        QtCore.QObject.connect(self.btnNewSub, QtCore.SIGNAL(_fromUtf8("clicked()")), FontGenWidget.add_sub)
        QtCore.QObject.connect(self.btnDelSub, QtCore.SIGNAL(_fromUtf8("clicked()")), FontGenWidget.del_sub)
        QtCore.QObject.connect(self.treeSubs, QtCore.SIGNAL(_fromUtf8("itemChanged(QTreeWidgetItem*,int)")), FontGenWidget.sub_changed)
        QtCore.QObject.connect(self.txtChars, QtCore.SIGNAL(_fromUtf8("textChanged()")), FontGenWidget.chars_changed)
        QtCore.QObject.connect(self.cboPenCap, QtCore.SIGNAL(_fromUtf8("currentIndexChanged(int)")), FontGenWidget.adv_changed)
        QtCore.QObject.connect(self.cboPenJoin, QtCore.SIGNAL(_fromUtf8("currentIndexChanged(int)")), FontGenWidget.adv_changed)
        QtCore.QObject.connect(self.chkTrace, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), FontGenWidget.adv_changed)
        QtCore.QMetaObject.connectSlotsByName(FontGenWidget)
        FontGenWidget.setTabOrder(self.cboFont, self.spnFontSize)
        FontGenWidget.setTabOrder(self.spnFontSize, self.spnFontWeight)
        FontGenWidget.setTabOrder(self.spnFontWeight, self.spnXOffset)
        FontGenWidget.setTabOrder(self.spnXOffset, self.spnYOffset)
        FontGenWidget.setTabOrder(self.spnYOffset, self.spnXMargin)
        FontGenWidget.setTabOrder(self.spnXMargin, self.spnYMargin)
        FontGenWidget.setTabOrder(self.spnYMargin, self.spnYShift)
        FontGenWidget.setTabOrder(self.spnYShift, self.chkBoundingBoxes)
        FontGenWidget.setTabOrder(self.chkBoundingBoxes, self.chkAutoRefresh)
        FontGenWidget.setTabOrder(self.chkAutoRefresh, self.btnRefreshPreview)
        FontGenWidget.setTabOrder(self.btnRefreshPreview, self.treeSubs)
        FontGenWidget.setTabOrder(self.treeSubs, self.btnNewSub)
        FontGenWidget.setTabOrder(self.btnNewSub, self.btnDelSub)
        FontGenWidget.setTabOrder(self.btnDelSub, self.txtChars)

    def retranslateUi(self, FontGenWidget):
        FontGenWidget.setWindowTitle(_translate("FontGenWidget", "[*]", None))
        self.groupBox.setTitle(_translate("FontGenWidget", "Font Settings", None))
        self.label_5.setText(_translate("FontGenWidget", "Size", None))
        self.label.setText(_translate("FontGenWidget", "Weight", None))
        self.groupBox_2.setTitle(_translate("FontGenWidget", "Advanced", None))
        self.label_7.setText(_translate("FontGenWidget", "X Offset", None))
        self.label_8.setText(_translate("FontGenWidget", "Y Offset", None))
        self.label_2.setText(_translate("FontGenWidget", "X Margin", None))
        self.label_10.setText(_translate("FontGenWidget", "Y Margin", None))
        self.label_12.setText(_translate("FontGenWidget", "Y Shift", None))
        self.chkTrace.setTitle(_translate("FontGenWidget", "Trace Outlines", None))
        self.label_6.setText(_translate("FontGenWidget", "Pen Size", None))
        self.label_13.setText(_translate("FontGenWidget", "Cap Style", None))
        self.cboPenCap.setItemText(0, _translate("FontGenWidget", "Square", None))
        self.cboPenCap.setItemText(1, _translate("FontGenWidget", "Flat", None))
        self.cboPenCap.setItemText(2, _translate("FontGenWidget", "Round", None))
        self.label_14.setText(_translate("FontGenWidget", "Join Style", None))
        self.cboPenJoin.setItemText(0, _translate("FontGenWidget", "Miter", None))
        self.cboPenJoin.setItemText(1, _translate("FontGenWidget", "Bevel", None))
        self.cboPenJoin.setItemText(2, _translate("FontGenWidget", "Round", None))
        self.cboPenJoin.setItemText(3, _translate("FontGenWidget", "SVG Miter", None))
        self.label_3.setText(_translate("FontGenWidget", "Preview", None))
        self.chkBoundingBoxes.setText(_translate("FontGenWidget", "Bounding Boxes", None))
        self.chkAutoRefresh.setText(_translate("FontGenWidget", "Auto", None))
        self.btnRefreshPreview.setText(_translate("FontGenWidget", "Refresh", None))
        self.label_4.setText(_translate("FontGenWidget", "Characters", None))
        self.label_9.setText(_translate("FontGenWidget", "Substitutions", None))
        self.treeSubs.setSortingEnabled(True)
        self.treeSubs.headerItem().setText(0, _translate("FontGenWidget", "Replace", None))
        self.treeSubs.headerItem().setText(1, _translate("FontGenWidget", "With", None))
        __sortingEnabled = self.treeSubs.isSortingEnabled()
        self.treeSubs.setSortingEnabled(False)
        self.treeSubs.topLevelItem(0).setText(0, _translate("FontGenWidget", "…", None))
        self.treeSubs.topLevelItem(0).setText(1, _translate("FontGenWidget", "...", None))
        self.treeSubs.topLevelItem(1).setText(0, _translate("FontGenWidget", "\\t", None))
        self.treeSubs.setSortingEnabled(__sortingEnabled)

import icons_rc
