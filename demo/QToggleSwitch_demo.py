#!/usr/bin/env python3

# Demo of QToggleSwitch

from PyQt5 import QtCore, QtGui, QtWidgets
import QToggleSwitch
from sys import argv


def message():

    print("Toggled.")

def onMessage():

    print("Switched on.")

def offMessage():

    print("Switched off.")

def documentationDialog():

    documentationText = '''
    <h1>QToggleSwitch</h1> <br />

    <code>QToggleSwitch</code> - An on/off switch for Qt. <br />

    Inherits <code>QSlider</code>.<br />

    Licensed under the Apache License 2.0 - http://www.apache.org/licenses/LICENSE-2.0

    <h2>Parameters:</h2>

    Default value of switch is 0 (off). This can be changed by passing the
    <code>default=</code> argument on intitialization. This argument accepts
    <code>0</code> for off and <code>1</code> for on.

    <h2>Signals:</h2>
    <ul>

    <li> <code>toggled</code> - Emitted when switch's value changes </li>
    <li> <code>switchedOn</code> - Emitted when value becomes 1 (on) </li>
    <li> <code>switchedOff</code> - Emitted when value becomes 0 (off) </li>
    </ul>

    <h2>Functions:</h2>
    <ul>
    <li> <code>toggle()</code> - Programmatically switch on/off </li>
    </ul>

    <h2>Properties:</h2>
    <ul>
    <li> (Boolean) <code>isOn()</code> - Returns <code>True</code> if on </li>
    </ul>
    '''

    dialog = QtWidgets.QMessageBox()

    dialog.setWindowTitle('Documentation')
    dialog.setText(documentationText)

    dialog.exec_()

app = QtWidgets.QApplication(argv)

mainWindow = QtWidgets.QMainWindow()

switch = QToggleSwitch.QToggleSwitch(default=0)

documentationButton = QtWidgets.QPushButton('Documentation')

documentationButton.clicked.connect(documentationDialog)

mainWidget = QtWidgets.QWidget()

layout = QtWidgets.QVBoxLayout()

layout.addWidget(switch)

layout.addWidget(documentationButton)

mainWidget.setLayout(layout)

mainWindow.setCentralWidget(mainWidget)

mainWindow.show()

switch.toggled.connect(message)

switch.switchedOn.connect(onMessage)

switch.switchedOff.connect(offMessage)

app.exec_()
