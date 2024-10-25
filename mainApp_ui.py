# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainApp.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QListWidget, QListWidgetItem, QMainWindow,
    QMenuBar, QPushButton, QRadioButton, QSizePolicy,
    QSlider, QSpacerItem, QSpinBox, QStatusBar,
    QVBoxLayout, QWidget)

from pyqtgraph import PlotWidget

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1139, 545)
        MainWindow.setStyleSheet(u"background-color: #242526;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(10, 15, 0, -1)
        self.uploadButton = QPushButton(self.centralwidget)
        self.uploadButton.setObjectName(u"uploadButton")
        self.uploadButton.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uploadButton.sizePolicy().hasHeightForWidth())
        self.uploadButton.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamilies([u"-apple-system"])
        font.setPointSize(18)
        font.setBold(True)
        self.uploadButton.setFont(font)
        self.uploadButton.setStyleSheet(u"QPushButton{\n"
"  appearance: button;\n"
"  backface-visibility: hidden;\n"
"  background-color: #405cf5;\n"
"  border-radius: 6px;\n"
"  border-width: 0;\n"
"  box-shadow: rgba(50, 50, 93, .1) 0 0 0 1px inset,rgba(50, 50, 93, .1) 0 2px 5px 0,rgba(0, 0, 0, .07) 0 1px 1px 0;\n"
"  box-sizing: border-box;\n"
"  color: #fff;\n"
"  cursor: pointer;\n"
"  font-family: -apple-system,system-ui,\"Segoe UI\",Roboto,\"Helvetica Neue\",Ubuntu,sans-serif;\n"
"  font-size: 100%;\n"
"  height: 44px;\n"
"  line-height: 1.15;\n"
"\n"
"  outline: none;\n"
"  overflow: hidden;\n"
"  padding: 0 10px;\n"
"  position: relative;\n"
"  text-align: center;\n"
"  text-transform: none;\n"
"  transform: translateZ(0);\n"
"  transition: all .2s,box-shadow .08s ease-in;\n"
"  touch-action: manipulation;\n"
"  width:155px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: #283999;\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: #1c2973;\n"
"}\n"
"")
        icon = QIcon()
        icon.addFile(u":/Icons/Icons/upload-square-svgrepo-com.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.uploadButton.setIcon(icon)
        self.uploadButton.setIconSize(QSize(25, 25))

        self.verticalLayout_5.addWidget(self.uploadButton)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalSpacer_7 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)

        self.verticalLayout_2.addItem(self.verticalSpacer_7)

        self.mixer = QLabel(self.centralwidget)
        self.mixer.setObjectName(u"mixer")
        font1 = QFont()
        font1.setFamilies([u"Overpass Black"])
        font1.setBold(True)
        self.mixer.setFont(font1)
        self.mixer.setStyleSheet(u"color:white;\n"
"font-size:20px;\n"
"margin: 0 0 ;")
        self.mixer.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.mixer)

        self.line_11 = QFrame(self.centralwidget)
        self.line_11.setObjectName(u"line_11")
        self.line_11.setStyleSheet(u"/* Line style */\n"
"\n"
"  /* Set the width of the line */\n"
"  width: 20px;\n"
"\n"
"  /* Set the height of the line */\n"
"  height: 5px;\n"
"\n"
"  /* Set the background color of the line */\n"
"  background-color: #3a3b3c;\n"
"\n"
"  /* Set the border of the line */\n"
"  border: 10px;\n"
"\n"
"  /* Set the border radius of the line */\n"
"  border-radius:5px;\n"
"\n"
"	margin: 0 0 0px 0;\n"
"\n"
"\n"
"\n"
"")
        self.line_11.setFrameShape(QFrame.Shape.HLine)
        self.line_11.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_2.addWidget(self.line_11)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(-1, -1, 0, -1)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.Frequency = QLabel(self.centralwidget)
        self.Frequency.setObjectName(u"Frequency")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.Frequency.sizePolicy().hasHeightForWidth())
        self.Frequency.setSizePolicy(sizePolicy1)
        font2 = QFont()
        font2.setFamilies([u"Overpass SemiBold"])
        font2.setPointSize(11)
        font2.setBold(False)
        font2.setKerning(True)
        self.Frequency.setFont(font2)
        self.Frequency.setStyleSheet(u"color:white;\n"
"font-weight:10000px;\n"
"margin: 5px 0 ;")

        self.horizontalLayout.addWidget(self.Frequency)

        self.freqSpinBox = QSpinBox(self.centralwidget)
        self.freqSpinBox.setObjectName(u"freqSpinBox")
        self.freqSpinBox.setEnabled(True)
        self.freqSpinBox.setStyleSheet(u"/* QSpinBox */\n"
"QSpinBox {\n"
"    background-color: #f0f0f0; /* Light background color */\n"
"    color: #405cf5; /* Dark text color */\n"
"    border: 2px solid #405cf5; /* Add a border for a modern look */\n"
"    border-radius: 10px; /* Slightly rounder corners */\n"
"    padding: 3px 8px; /* Increase padding for spacing */\n"
"	padding-left: 15px;\n"
"	margin: 0 5px;\n"
"    font-weight: bold;\n"
"    font-size: 18px; /* Adjust font size */\n"
"    text-align: center;\n"
"	height:20px; \n"
"width: 50px;\n"
"}\n"
"\n"
"/* QSpinBox Up Button (on the right) */\n"
"QSpinBox::up-button {\n"
"	\n"
"	image: url(Icons/plus-circle.png);\n"
"    border-radius: 50%; /* Round button corners */\n"
"    width: 25px;\n"
"    height: 25px;\n"
"    subcontrol-position: right; /* Place the up-button on the right */\n"
"}\n"
"\n"
"/* QSpinBox Down Button (on the left) */\n"
"QSpinBox::down-button {\n"
"	\n"
"	image: url(Icons/minus-circle.png);\n"
"    border-radius: 5px; /* Round button corners */\n"
"    width: 25px;\n"
""
                        "    height: 25px;\n"
"    subcontrol-position: left; /* Place the down-button on the left */\n"
"}\n"
"\n"
"QSpinBox::up-button:hover, QSpinBox::down-button:hover {\n"
"    background-color: #9fadfa; /* Change button color on hover */\n"
"	 border-radius: 10px;\n"
"}\n"
"")

        self.horizontalLayout.addWidget(self.freqSpinBox)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.Amplitude = QLabel(self.centralwidget)
        self.Amplitude.setObjectName(u"Amplitude")
        sizePolicy1.setHeightForWidth(self.Amplitude.sizePolicy().hasHeightForWidth())
        self.Amplitude.setSizePolicy(sizePolicy1)
        font3 = QFont()
        font3.setFamilies([u"Overpass SemiBold"])
        font3.setPointSize(11)
        font3.setBold(False)
        self.Amplitude.setFont(font3)
        self.Amplitude.setStyleSheet(u"color:white;\n"
"font-weight:10000px;\n"
"margin: 5px 0 ;")

        self.horizontalLayout_6.addWidget(self.Amplitude)

        self.ampSpinBox = QSpinBox(self.centralwidget)
        self.ampSpinBox.setObjectName(u"ampSpinBox")
        self.ampSpinBox.setEnabled(True)
        self.ampSpinBox.setStyleSheet(u"/* QSpinBox */\n"
"QSpinBox {\n"
"    background-color: #f0f0f0; /* Light background color */\n"
"    color: #405cf5; /* Dark text color */\n"
"    border: 2px solid #405cf5; /* Add a border for a modern look */\n"
"    border-radius: 10px; /* Slightly rounder corners */\n"
"    padding: 3px 8px; /* Increase padding for spacing */\n"
"	padding-left: 15px;\n"
"	margin: 0 5px;\n"
"    font-weight: bold;\n"
"    font-size: 18px; /* Adjust font size */\n"
"    text-align: center;\n"
"	height:20px; \n"
"width: 50px;\n"
"}\n"
"\n"
"/* QSpinBox Up Button (on the right) */\n"
"QSpinBox::up-button {\n"
"	\n"
"	image: url(Icons/plus-circle.png);\n"
"    border-radius: 50%; /* Round button corners */\n"
"    width: 25px;\n"
"    height: 25px;\n"
"    subcontrol-position: right; /* Place the up-button on the right */\n"
"}\n"
"\n"
"/* QSpinBox Down Button (on the left) */\n"
"QSpinBox::down-button {\n"
"	\n"
"	image: url(Icons/minus-circle.png);\n"
"    border-radius: 5px; /* Round button corners */\n"
"    width: 25px;\n"
""
                        "    height: 25px;\n"
"    subcontrol-position: left; /* Place the down-button on the left */\n"
"}\n"
"\n"
"QSpinBox::up-button:hover, QSpinBox::down-button:hover {\n"
"    background-color: #9fadfa; /* Change button color on hover */\n"
"	 border-radius: 10px;\n"
"}\n"
"")

        self.horizontalLayout_6.addWidget(self.ampSpinBox)


        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setSpacing(33)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.Phase = QLabel(self.centralwidget)
        self.Phase.setObjectName(u"Phase")
        sizePolicy1.setHeightForWidth(self.Phase.sizePolicy().hasHeightForWidth())
        self.Phase.setSizePolicy(sizePolicy1)
        self.Phase.setFont(font3)
        self.Phase.setStyleSheet(u"color:white;\n"
"font-weight:10000px;\n"
"margin: 5px 0 ;")

        self.horizontalLayout_7.addWidget(self.Phase)

        self.phaseSpinBox = QSpinBox(self.centralwidget)
        self.phaseSpinBox.setObjectName(u"phaseSpinBox")
        self.phaseSpinBox.setEnabled(True)
        self.phaseSpinBox.setStyleSheet(u"/* QSpinBox */\n"
"QSpinBox {\n"
"    background-color: #f0f0f0; /* Light background color */\n"
"    color: #405cf5; /* Dark text color */\n"
"    border: 2px solid #405cf5; /* Add a border for a modern look */\n"
"    border-radius: 10px; /* Slightly rounder corners */\n"
"    padding: 3px 8px; /* Increase padding for spacing */\n"
"	padding-left: 15px;\n"
"	margin: 0 5px;\n"
"    font-weight: bold;\n"
"    font-size: 18px; /* Adjust font size */\n"
"    text-align: center;\n"
"	height:20px; \n"
"width: 50px;\n"
"}\n"
"\n"
"/* QSpinBox Up Button (on the right) */\n"
"QSpinBox::up-button {\n"
"	\n"
"	image: url(Icons/plus-circle.png);\n"
"    border-radius: 50%; /* Round button corners */\n"
"    width: 25px;\n"
"    height: 25px;\n"
"    subcontrol-position: right; /* Place the up-button on the right */\n"
"}\n"
"\n"
"/* QSpinBox Down Button (on the left) */\n"
"QSpinBox::down-button {\n"
"	\n"
"	image: url(Icons/minus-circle.png);\n"
"    border-radius: 5px; /* Round button corners */\n"
"    width: 25px;\n"
""
                        "    height: 25px;\n"
"    subcontrol-position: left; /* Place the down-button on the left */\n"
"}\n"
"\n"
"QSpinBox::up-button:hover, QSpinBox::down-button:hover {\n"
"    background-color: #9fadfa; /* Change button color on hover */\n"
"	 border-radius: 10px;\n"
"}\n"
"")

        self.horizontalLayout_7.addWidget(self.phaseSpinBox)


        self.verticalLayout.addLayout(self.horizontalLayout_7)


        self.horizontalLayout_8.addLayout(self.verticalLayout)

        self.attrList = QListWidget(self.centralwidget)
        self.attrList.setObjectName(u"attrList")
        self.attrList.setStyleSheet(u"QListWidget {\n"
"    background-color: #4a4a4a; /* Background color of the list widget */\n"
"    /*border: 1px solid #c0c0c0; /* Border color and width */\n"
"    padding: 5px; /* Padding around the list items */\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"QListWidget::item {\n"
"    background-color: #4a4a4a; /* Background color of each list item */\n"
"    padding: 5px; /* Padding inside each list item */\n"
"    border-bottom: 1px solid #c0c0c0; /* Separator between list items */\n"
"    border-radius: 15px; /* Border radius for rounded corners */\n"
"	color: #ffffff;\n"
"}\n"
"\n"
"\n"
"QListWidget::item:selected {\n"
"    background-color: #3399ff; /* Background color of selected item */\n"
"    color: #ffffff; /* Text color of selected item */\n"
"}\n"
"\n"
"QListWidget::item:hover {\n"
"    background-color: #e0e0e0; /* Background color when hovering over an item */\n"
"}\n"
"")

        self.horizontalLayout_8.addWidget(self.attrList)

        self.horizontalLayout_8.setStretch(0, 2)
        self.horizontalLayout_8.setStretch(1, 2)

        self.verticalLayout_2.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.addComponent = QPushButton(self.centralwidget)
        self.addComponent.setObjectName(u"addComponent")
        font4 = QFont()
        font4.setFamilies([u"-apple-system"])
        font4.setPointSize(11)
        font4.setBold(True)
        self.addComponent.setFont(font4)
        self.addComponent.setStyleSheet(u"QPushButton{\n"
"  appearance: button;\n"
"  backface-visibility: hidden;\n"
"  background-color: #405cf5;\n"
"  border-radius: 6px;\n"
"  border-width: 0;\n"
"  box-shadow: rgba(50, 50, 93, .1) 0 0 0 1px inset,rgba(50, 50, 93, .1) 0 2px 5px 0,rgba(0, 0, 0, .07) 0 1px 1px 0;\n"
"  box-sizing: border-box;\n"
"  color: #fff;\n"
"  cursor: pointer;\n"
"  font-family: -apple-system,system-ui,\"Segoe UI\",Roboto,\"Helvetica Neue\",Ubuntu,sans-serif;\n"
"  font-size: 100%;\n"
"  height: 35px;\n"
"  line-height: 1.15;\n"
"\n"
"  outline: none;\n"
"  overflow: hidden;\n"
"  padding: 0 5px;\n"
"  position: relative;\n"
"  text-align: center;\n"
"  text-transform: none;\n"
"  transform: translateZ(0);\n"
"  transition: all .2s,box-shadow .08s ease-in;\n"
"  touch-action: manipulation;\n"
"  width:100px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: #283999;\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: #1c2973;\n"
"}\n"
"")

        self.horizontalLayout_2.addWidget(self.addComponent)

        self.horizontalSpacer_3 = QSpacerItem(20, 22, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.GenerateButton = QPushButton(self.centralwidget)
        self.GenerateButton.setObjectName(u"GenerateButton")
        self.GenerateButton.setFont(font4)
        self.GenerateButton.setStyleSheet(u"QPushButton{\n"
"  appearance: button;\n"
"  backface-visibility: hidden;\n"
"  background-color: #405cf5;\n"
"  border-radius: 6px;\n"
"  border-width: 0;\n"
"  box-shadow: rgba(50, 50, 93, .1) 0 0 0 1px inset,rgba(50, 50, 93, .1) 0 2px 5px 0,rgba(0, 0, 0, .07) 0 1px 1px 0;\n"
"  box-sizing: border-box;\n"
"  color: #fff;\n"
"  cursor: pointer;\n"
"  font-family: -apple-system,system-ui,\"Segoe UI\",Roboto,\"Helvetica Neue\",Ubuntu,sans-serif;\n"
"  font-size: 100%;\n"
"  height: 35px;\n"
"  line-height: 1.15;\n"
"\n"
"  outline: none;\n"
"  overflow: hidden;\n"
"  padding: 0 5px;\n"
"  position: relative;\n"
"  text-align: center;\n"
"  text-transform: none;\n"
"  transform: translateZ(0);\n"
"  transition: all .2s,box-shadow .08s ease-in;\n"
"  touch-action: manipulation;\n"
"  width:100px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: #283999;\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: #1c2973;\n"
"}\n"
"")

        self.horizontalLayout_2.addWidget(self.GenerateButton)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)


        self.verticalLayout_5.addLayout(self.verticalLayout_2)

        self.line_7 = QFrame(self.centralwidget)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setStyleSheet(u"/* Line style */\n"
"\n"
"  /* Set the width of the line */\n"
"  width: 20px;\n"
"\n"
"  /* Set the height of the line */\n"
"  height: 5px;\n"
"\n"
"  /* Set the background color of the line */\n"
"  background-color: #3a3b3c;\n"
"\n"
"  /* Set the border of the line */\n"
"  border: 10px;\n"
"\n"
"  /* Set the border radius of the line */\n"
"  border-radius:5px;\n"
"\n"
"\n"
"\n"
"")
        self.line_7.setFrameShape(QFrame.Shape.HLine)
        self.line_7.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_5.addWidget(self.line_7)

        self.verticalSpacer_9 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)

        self.verticalLayout_5.addItem(self.verticalSpacer_9)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.Signals = QLabel(self.centralwidget)
        self.Signals.setObjectName(u"Signals")
        self.Signals.setFont(font1)
        self.Signals.setStyleSheet(u"color:white;\n"
"font-size:20px;\n"
"margin: 0 0 ;")
        self.Signals.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.Signals)

        self.line_12 = QFrame(self.centralwidget)
        self.line_12.setObjectName(u"line_12")
        self.line_12.setStyleSheet(u"/* Line style */\n"
"\n"
"  /* Set the width of the line */\n"
"  width: 20px;\n"
"\n"
"  /* Set the height of the line */\n"
"  height: 5px;\n"
"\n"
"  /* Set the background color of the line */\n"
"  background-color: #3a3b3c;\n"
"\n"
"  /* Set the border of the line */\n"
"  border: 10px;\n"
"\n"
"  /* Set the border radius of the line */\n"
"  border-radius:5px;\n"
"\n"
"	margin: 0 0 0px 0;\n"
"\n"
"\n"
"\n"
"")
        self.line_12.setFrameShape(QFrame.Shape.HLine)
        self.line_12.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_7.addWidget(self.line_12)

        self.signalsList = QListWidget(self.centralwidget)
        self.signalsList.setObjectName(u"signalsList")
        self.signalsList.setStyleSheet(u"QListWidget {\n"
"    background-color: #4a4a4a; /* Background color of the list widget */\n"
"    /*border: 1px solid #c0c0c0; /* Border color and width */\n"
"    padding: 5px; /* Padding around the list items */\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"QListWidget::item {\n"
"    background-color: #4a4a4a; /* Background color of each list item */\n"
"    padding: 5px; /* Padding inside each list item */\n"
"    border-bottom: 1px solid #c0c0c0; /* Separator between list items */\n"
"    border-radius: 15px; /* Border radius for rounded corners */\n"
"	color: #ffffff;\n"
"}\n"
"\n"
"\n"
"QListWidget::item:selected {\n"
"    background-color: #3399ff; /* Background color of selected item */\n"
"    color: #ffffff; /* Text color of selected item */\n"
"}\n"
"\n"
"QListWidget::item:hover {\n"
"    background-color: #e0e0e0; /* Background color when hovering over an item */\n"
"}\n"
"")

        self.verticalLayout_7.addWidget(self.signalsList)

        self.verticalSpacer_8 = QSpacerItem(30, 20, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)

        self.verticalLayout_7.addItem(self.verticalSpacer_8)


        self.horizontalLayout_3.addLayout(self.verticalLayout_7)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.Components = QLabel(self.centralwidget)
        self.Components.setObjectName(u"Components")
        self.Components.setFont(font1)
        self.Components.setStyleSheet(u"color:white;\n"
"font-size:20px;\n"
"margin: 0 0 ;")
        self.Components.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.Components)

        self.line_15 = QFrame(self.centralwidget)
        self.line_15.setObjectName(u"line_15")
        self.line_15.setStyleSheet(u"/* Line style */\n"
"\n"
"  /* Set the width of the line */\n"
"  width: 20px;\n"
"\n"
"  /* Set the height of the line */\n"
"  height: 5px;\n"
"\n"
"  /* Set the background color of the line */\n"
"  background-color: #3a3b3c;\n"
"\n"
"  /* Set the border of the line */\n"
"  border: 10px;\n"
"\n"
"  /* Set the border radius of the line */\n"
"  border-radius:5px;\n"
"\n"
"	margin: 0 0 0px 0;\n"
"\n"
"\n"
"\n"
"")
        self.line_15.setFrameShape(QFrame.Shape.HLine)
        self.line_15.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_8.addWidget(self.line_15)

        self.componList = QListWidget(self.centralwidget)
        self.componList.setObjectName(u"componList")
        self.componList.setStyleSheet(u"QListWidget {\n"
"    background-color: #4a4a4a; /* Background color of the list widget */\n"
"    /*border: 1px solid #c0c0c0; /* Border color and width */\n"
"    padding: 5px; /* Padding around the list items */\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"QListWidget::item {\n"
"    background-color: #4a4a4a; /* Background color of each list item */\n"
"    padding: 5px; /* Padding inside each list item */\n"
"    border-bottom: 1px solid #c0c0c0; /* Separator between list items */\n"
"    border-radius: 15px; /* Border radius for rounded corners */\n"
"	color: #ffffff;\n"
"}\n"
"\n"
"\n"
"QListWidget::item:selected {\n"
"    background-color: #3399ff; /* Background color of selected item */\n"
"    color: #ffffff; /* Text color of selected item */\n"
"}\n"
"\n"
"QListWidget::item:hover {\n"
"    background-color: #e0e0e0; /* Background color when hovering over an item */\n"
"}\n"
"")

        self.verticalLayout_8.addWidget(self.componList)

        self.verticalSpacer_10 = QSpacerItem(30, 20, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)

        self.verticalLayout_8.addItem(self.verticalSpacer_10)


        self.horizontalLayout_3.addLayout(self.verticalLayout_8)


        self.verticalLayout_5.addLayout(self.horizontalLayout_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setSpacing(4)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")

        self.verticalLayout_4.addLayout(self.horizontalLayout_4)


        self.verticalLayout_5.addLayout(self.verticalLayout_4)

        self.line_8 = QFrame(self.centralwidget)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setStyleSheet(u"/* Line style */\n"
"\n"
"  /* Set the width of the line */\n"
"  width: 20px;\n"
"\n"
"  /* Set the height of the line */\n"
"  height: 5px;\n"
"\n"
"  /* Set the background color of the line */\n"
"  background-color: #3a3b3c;\n"
"\n"
"  /* Set the border of the line */\n"
"  border: 10px;\n"
"\n"
"  /* Set the border radius of the line */\n"
"  border-radius:5px;\n"
"\n"
"\n"
"\n"
"")
        self.line_8.setFrameShape(QFrame.Shape.HLine)
        self.line_8.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_5.addWidget(self.line_8)


        self.horizontalLayout_9.addLayout(self.verticalLayout_5)

        self.horizontalSpacer = QSpacerItem(25, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 10, -1, -1)
        self.graph1 = PlotWidget(self.centralwidget)
        self.graph1.setObjectName(u"graph1")

        self.verticalLayout_6.addWidget(self.graph1)

        self.graph2 = PlotWidget(self.centralwidget)
        self.graph2.setObjectName(u"graph2")

        self.verticalLayout_6.addWidget(self.graph2)

        self.graph3 = PlotWidget(self.centralwidget)
        self.graph3.setObjectName(u"graph3")

        self.verticalLayout_6.addWidget(self.graph3)

        self.graph4 = PlotWidget(self.centralwidget)
        self.graph4.setObjectName(u"graph4")

        self.verticalLayout_6.addWidget(self.graph4)


        self.horizontalLayout_9.addLayout(self.verticalLayout_6)

        self.horizontalSpacer_2 = QSpacerItem(25, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_2)

        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(-1, -1, 10, -1)
        self.verticalSpacer_2 = QSpacerItem(20, 80, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)

        self.verticalLayout_13.addItem(self.verticalSpacer_2)

        self.Noise = QLabel(self.centralwidget)
        self.Noise.setObjectName(u"Noise")
        self.Noise.setFont(font1)
        self.Noise.setStyleSheet(u"color:white;\n"
"font-size:20px;\n"
"margin: 0 0 ;")
        self.Noise.setAlignment(Qt.AlignCenter)

        self.verticalLayout_13.addWidget(self.Noise)

        self.line_10 = QFrame(self.centralwidget)
        self.line_10.setObjectName(u"line_10")
        self.line_10.setStyleSheet(u"/* Line style */\n"
"\n"
"  /* Set the width of the line */\n"
"  width: 20px;\n"
"\n"
"  /* Set the height of the line */\n"
"  height: 5px;\n"
"\n"
"  /* Set the background color of the line */\n"
"  background-color: #3a3b3c;\n"
"\n"
"  /* Set the border of the line */\n"
"  border: 10px;\n"
"\n"
"  /* Set the border radius of the line */\n"
"  border-radius:5px;\n"
"\n"
"	margin: 0 0 0px 0;\n"
"\n"
"\n"
"\n"
"")
        self.line_10.setFrameShape(QFrame.Shape.HLine)
        self.line_10.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_13.addWidget(self.line_10)

        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.SNR = QLabel(self.centralwidget)
        self.SNR.setObjectName(u"SNR")
        font5 = QFont()
        font5.setFamilies([u"Overpass SemiBold"])
        font5.setPointSize(11)
        font5.setBold(True)
        self.SNR.setFont(font5)
        self.SNR.setStyleSheet(u"color:white;\n"
"font-weight:10000px;\n"
"margin-top: 7px;")
        self.SNR.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.verticalLayout_12.addWidget(self.SNR)

        self.snrLabel = QLabel(self.centralwidget)
        self.snrLabel.setObjectName(u"snrLabel")
        self.snrLabel.setStyleSheet(u"color:white;\n"
"margin-top: 3px;\n"
"")

        self.verticalLayout_12.addWidget(self.snrLabel)

        self.noiseSlider = QSlider(self.centralwidget)
        self.noiseSlider.setObjectName(u"noiseSlider")
        self.noiseSlider.setStyleSheet(u"/* Style for the QSlider */\n"
"\n"
"/* Background of the slider track */\n"
"QSlider {\n"
"background-color: transparent;\n"
"height: 10px; /* Set the height of the track */\n"
"\n"
"}\n"
"\n"
"/* Style for the groove (track) */\n"
"QSlider::groove {\n"
"background: #595a5c; /* Color of the track */\n"
"border: 0px solid #999; /* Border of the track */\n"
"height: 5px; /* Set the height of the track */\n"
"border-radius: 2px; /* Round the corners of the track */\n"
"}\n"
"\n"
"/* Style for the slider handle (thumb) */\n"
"QSlider::handle {\n"
"background: #FF4742; /* Color of the handle */\n"
"border: 1px solid ; /* Border of the handle */\n"
"width: 20px; /* Width of the handle */\n"
"height: 30px; /* Height of the handle */\n"
"margin: -5px 0; /* Negative margin to center the handle vertically */\n"
"border-radius: 7px; /* Round the corners of the handle to make it into a circle */\n"
"}\n"
"\n"
"/* Style for the slider handle when pressed */\n"
"QSlider::handle:pressed {\n"
"background: #992a27; /* Color o"
                        "f the handle when pressed */\n"
"border: 1px solid #3498db; /* Border of the handle when pressed */\n"
"}")
        self.noiseSlider.setOrientation(Qt.Horizontal)

        self.verticalLayout_12.addWidget(self.noiseSlider)


        self.verticalLayout_13.addLayout(self.verticalLayout_12)

        self.verticalSpacer_5 = QSpacerItem(20, 60, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)

        self.verticalLayout_13.addItem(self.verticalSpacer_5)

        self.Frequency_2 = QLabel(self.centralwidget)
        self.Frequency_2.setObjectName(u"Frequency_2")
        self.Frequency_2.setFont(font1)
        self.Frequency_2.setStyleSheet(u"color:white;\n"
"font-size:20px;\n"
"margin: 0 0 ;")
        self.Frequency_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_13.addWidget(self.Frequency_2)

        self.line_9 = QFrame(self.centralwidget)
        self.line_9.setObjectName(u"line_9")
        self.line_9.setStyleSheet(u"/* Line style */\n"
"\n"
"  /* Set the width of the line */\n"
"  width: 20px;\n"
"\n"
"  /* Set the height of the line */\n"
"  height: 5px;\n"
"\n"
"  /* Set the background color of the line */\n"
"  background-color: #3a3b3c;\n"
"\n"
"  /* Set the border of the line */\n"
"  border: 10px;\n"
"\n"
"  /* Set the border radius of the line */\n"
"  border-radius:5px;\n"
"\n"
"	margin: 0 0 0px 0;\n"
"\n"
"\n"
"\n"
"")
        self.line_9.setFrameShape(QFrame.Shape.HLine)
        self.line_9.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_13.addWidget(self.line_9)

        self.verticalSpacer_11 = QSpacerItem(20, 13, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)

        self.verticalLayout_13.addItem(self.verticalSpacer_11)

        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.actualRadio = QRadioButton(self.centralwidget)
        self.actualRadio.setObjectName(u"actualRadio")
        self.actualRadio.setFont(font5)
        self.actualRadio.setStyleSheet(u"color:white;\n"
"font-weight:10000px;")

        self.verticalLayout_11.addWidget(self.actualRadio)

        self.normalRadio = QRadioButton(self.centralwidget)
        self.normalRadio.setObjectName(u"normalRadio")
        self.normalRadio.setFont(font5)
        self.normalRadio.setStyleSheet(u"color:white;\n"
"font-weight:10000px;")

        self.verticalLayout_11.addWidget(self.normalRadio)

        self.verticalSpacer_6 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)

        self.verticalLayout_11.addItem(self.verticalSpacer_6)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.indicatLabel = QLabel(self.centralwidget)
        self.indicatLabel.setObjectName(u"indicatLabel")
        font6 = QFont()
        font6.setFamilies([u"Overpass Medium"])
        font6.setPointSize(10)
        self.indicatLabel.setFont(font6)
        self.indicatLabel.setStyleSheet(u"color:white;\n"
"margin-top: 3px;")

        self.horizontalLayout_10.addWidget(self.indicatLabel)

        self.fmaxLabel = QLabel(self.centralwidget)
        self.fmaxLabel.setObjectName(u"fmaxLabel")
        self.fmaxLabel.setFont(font5)
        self.fmaxLabel.setStyleSheet(u"color:white;\n"
"font-weight:10000px;\n"
"margin-top: 3px;")
        self.fmaxLabel.setAlignment(Qt.AlignRight|Qt.AlignTop|Qt.AlignTrailing)

        self.horizontalLayout_10.addWidget(self.fmaxLabel)


        self.verticalLayout_11.addLayout(self.horizontalLayout_10)

        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.sampleSlider = QSlider(self.centralwidget)
        self.sampleSlider.setObjectName(u"sampleSlider")
        self.sampleSlider.setStyleSheet(u"/* Style for the QSlider */\n"
"\n"
"/* Background of the slider track */\n"
"QSlider {\n"
"background-color: transparent;\n"
"height: 10px; /* Set the height of the track */\n"
"margin:0 0;\n"
"}\n"
"\n"
"/* Style for the groove (track) */\n"
"QSlider::groove {\n"
"background: #595a5c; /* Color of the track */\n"
"border: 0px solid #999; /* Border of the track */\n"
"height: 5px; /* Set the height of the track */\n"
"border-radius: 2px; /* Round the corners of the track */\n"
"margin:0 0;\n"
"}\n"
"\n"
"/* Style for the slider handle (thumb) */\n"
"QSlider::handle {\n"
"background: #FF4742; /* Color of the handle */\n"
"border: 1px solid ; /* Border of the handle */\n"
"width: 20px; /* Width of the handle */\n"
"height: 30px; /* Height of the handle */\n"
"margin: -5px 0; /* Negative margin to center the handle vertically */\n"
"border-radius: 7px; /* Round the corners of the handle to make it into a circle */\n"
"}\n"
"\n"
"/* Style for the slider handle when pressed */\n"
"QSlider::handle:pressed {\n"
"back"
                        "ground: #992a27; /* Color of the handle when pressed */\n"
"border: 1px solid #3498db; /* Border of the handle when pressed */\n"
"}")
        self.sampleSlider.setOrientation(Qt.Horizontal)

        self.verticalLayout_9.addWidget(self.sampleSlider)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.startLabel = QLabel(self.centralwidget)
        self.startLabel.setObjectName(u"startLabel")
        self.startLabel.setFont(font6)
        self.startLabel.setStyleSheet(u"color:white;\n"
"margin-top: 3px;")

        self.horizontalLayout_5.addWidget(self.startLabel)

        self.endLabel = QLabel(self.centralwidget)
        self.endLabel.setObjectName(u"endLabel")
        self.endLabel.setFont(font6)
        self.endLabel.setStyleSheet(u"color:white;\n"
"margin-top: 3px;")
        self.endLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.endLabel)


        self.verticalLayout_9.addLayout(self.horizontalLayout_5)


        self.verticalLayout_10.addLayout(self.verticalLayout_9)

        self.verticalSpacer_4 = QSpacerItem(20, 30, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)

        self.verticalLayout_10.addItem(self.verticalSpacer_4)


        self.verticalLayout_11.addLayout(self.verticalLayout_10)


        self.verticalLayout_13.addLayout(self.verticalLayout_11)

        self.downloadButton = QPushButton(self.centralwidget)
        self.downloadButton.setObjectName(u"downloadButton")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.downloadButton.sizePolicy().hasHeightForWidth())
        self.downloadButton.setSizePolicy(sizePolicy2)
        font7 = QFont()
        font7.setFamilies([u"-apple-system"])
        font7.setPointSize(16)
        font7.setBold(True)
        self.downloadButton.setFont(font7)
        self.downloadButton.setLayoutDirection(Qt.LeftToRight)
        self.downloadButton.setStyleSheet(u"QPushButton{\n"
"  appearance: button;\n"
"  backface-visibility: hidden;\n"
"  background-color: #405cf5;\n"
"  border-radius: 6px;\n"
"  border-width: 0;\n"
"  box-shadow: rgba(50, 50, 93, .1) 0 0 0 1px inset,rgba(50, 50, 93, .1) 0 2px 5px 0,rgba(0, 0, 0, .07) 0 1px 1px 0;\n"
"  box-sizing: border-box;\n"
"  color: #fff;\n"
"  cursor: pointer;\n"
"  font-family: -apple-system,system-ui,\"Segoe UI\",Roboto,\"Helvetica Neue\",Ubuntu,sans-serif;\n"
"  font-size: 100%;\n"
"  height: 44px;\n"
"  line-height: 1.15;\n"
"  margin: 0 0 0 25px;\n"
"  outline: none;\n"
"  overflow: hidden;\n"
"  padding: 0 10px;\n"
"  position: relative;\n"
"  text-align: center;\n"
"  text-transform: none;\n"
"  transform: translateZ(0);\n"
"  transition: all .2s,box-shadow .08s ease-in;\n"
"  touch-action: manipulation;\n"
"  width:140px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: #283999;\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: #1c2973;\n"
"}\n"
"")
        icon1 = QIcon()
        icon1.addFile(u":/Icons/Icons/save-svgrepo-com.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.downloadButton.setIcon(icon1)
        self.downloadButton.setIconSize(QSize(30, 27))

        self.verticalLayout_13.addWidget(self.downloadButton)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_13.addItem(self.verticalSpacer_3)


        self.horizontalLayout_9.addLayout(self.verticalLayout_13)

        self.horizontalLayout_9.setStretch(0, 2)
        self.horizontalLayout_9.setStretch(2, 4)

        self.gridLayout.addLayout(self.horizontalLayout_9, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1139, 26))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.uploadButton.setText(QCoreApplication.translate("MainWindow", u"Upload", None))
        self.mixer.setText(QCoreApplication.translate("MainWindow", u"Mixer", None))
        self.Frequency.setText(QCoreApplication.translate("MainWindow", u"Frequency", None))
        self.Amplitude.setText(QCoreApplication.translate("MainWindow", u"Amplitude", None))
        self.Phase.setText(QCoreApplication.translate("MainWindow", u"Phase", None))
        self.addComponent.setText(QCoreApplication.translate("MainWindow", u"Add Comp", None))
        self.GenerateButton.setText(QCoreApplication.translate("MainWindow", u"Create Signal", None))
        self.Signals.setText(QCoreApplication.translate("MainWindow", u"Signals", None))
        self.Components.setText(QCoreApplication.translate("MainWindow", u"Components", None))
        self.Noise.setText(QCoreApplication.translate("MainWindow", u"Noise", None))
        self.SNR.setText(QCoreApplication.translate("MainWindow", u"SNR", None))
        self.snrLabel.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.Frequency_2.setText(QCoreApplication.translate("MainWindow", u"Frequency", None))
        self.actualRadio.setText(QCoreApplication.translate("MainWindow", u"Actual Sampling Freq", None))
        self.normalRadio.setText(QCoreApplication.translate("MainWindow", u"Normailzed Sampling Freq", None))
        self.indicatLabel.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.fmaxLabel.setText(QCoreApplication.translate("MainWindow", u"fmax", None))
        self.startLabel.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.endLabel.setText(QCoreApplication.translate("MainWindow", u"20", None))
        self.downloadButton.setText(QCoreApplication.translate("MainWindow", u"Save File", None))
    # retranslateUi

