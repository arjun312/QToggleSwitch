/* QToggleSwitch

   Copyright (c) 2016 Bharadwaj Raju All Rights Reserved.

   Licensed under the Apache License 2.0 - http://www.apache.org/licenses/LICENSE-2.0

 */

#include <Qt>
#include <QtCore>
#include <QObject>
#include <QSlider>
#include "QToggleSwitch.hpp"
#include <iostream>
#include <string>


QToggleSwitch::QToggleSwitch()
{
    int defaultValue = 0;

    //TODO: Allow parameter checking in C++ version

    QSlider(Qt::Horizontal);

    this->setMaximumWidth(30);

    this->setMinimum(0);

    this->setMaximum(1);

    int currentValue = defaultValue;

    this->setSliderPosition(defaultValue);

    connect(this, QSlider::sliderReleased, toggleWrapper);

}


void QToggleSwitch::toggle()
{
    extern int currentValue;

    if (this->value() == 1)
    {

        this->setSliderPosition(0);

        currentValue = 0;

        this->setValue(0);

        emit toggled();

        emit switchedOff();

    }

    else
    {

        this->setSliderPosition(1);

        currentValue = 1;

        this->setValue(1);

        emit toggled();

        emit switchedOn();

    }
}

bool QToggleSwitch::isOn()
{
    extern int currentValue;

    if (currentValue == 1) { return true; }

    else { return false; }

}

void QToggleSwitch::toggleWrapper(QToggleSwitch *toggleSwitch)
{
    toggleSwitch->toggle();
}
