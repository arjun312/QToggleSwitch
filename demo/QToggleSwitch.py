#!/usr/bin/env python3

# QToggleSwitch

# Copyright (c) 2016 Bharadwaj Raju All Rights Reserved.

# Licensed under the Apache License 2.0 - http://www.apache.org/licenses/LICENSE-2.0

from PyQt5 import QtCore, QtWidgets

class QToggleSwitch(QtWidgets.QSlider):

    ''' QToggleSwitch - An on/off switch for Qt

        Inherits QSlider

        ## Parameters

        Default value of switch is 0 (off). This can be changed by passing the
        `default=` argument on intitialization. This argument accepts
        `0` for off and `1` for on.

        ## Signals

        * `toggled` - Emitted when switch's value changes
        * `switchedOn` - Emitted when value becomes 1 (on)
        * `switchedOff` - Emitted when value becomes 0 (off)

        ## Functions

        * `toggle()` - Programmatically switch on/off

        ## Properties

        * `isOn()` (`Boolean`) - Returns `True` if on; else returns `False`

    '''

    # Custom signals work only when in decorator

    toggled = QtCore.pyqtSignal()

    switchedOn = QtCore.pyqtSignal()

    switchedOff = QtCore.pyqtSignal()

    def __init__(self, default=0):

        QtWidgets.QSlider.__init__(self, QtCore.Qt.Horizontal)

        self.setMaximumWidth(30)

        self.setMinimum(0)

        self.setMaximum(1)

        self.currentValue = default

        self.setSliderPosition(default)

        self.sliderReleased.connect(self.toggle)

    def toggle(self):

        if self.value == 1:

            self.setSliderPosition(0)

            self.currentValue = 0

            self.value = 0

            self.toggled.emit()

            self.switchedOff.emit()

        else:

            self.setSliderPosition(1)

            self.currentValue = 1

            self.value = 1

            self.toggled.emit()

            self.switchedOn.emit()

    def isOn(self):

        if self.currentValue == 1:

            return True

        else:

            return False
