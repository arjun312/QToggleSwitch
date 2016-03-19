/* QToggleSwitch

   Copyright (c) 2016 Bharadwaj Raju All Rights Reserved.

   Licensed under the Apache License 2.0 - http://www.apache.org/licenses/LICENSE-2.0

 */

#include <Qt>
#include <QtCore>
#include <QObject>
#include <QSlider>
#include "QToggleSwitch.h"


void QToggleSwitch::QToggleSwitch(int defaultValue=0)
{

    QSlider(this, Qt::Horizontal);

    this->setMaximumWidth(30);

    this->setMinimum(0);

    this->setMaximum(1);

    int currentValue = defaultValue;

    this->setSliderPosition(defaultValue);

    this->sliderReleased->connect(this->toggle);

}


void QToggleSwitch::toggle()
{

    if (value == 1)
    {

        this->setSliderPosition(0);

        currentValue = 0;

        this->value = 0;

        emit toggled();

        emit switchedOff();

    }

    else
    {

        this->setSliderPosition(1);

        currentValue = 1;

        value = 1;

        emit this.toggled;

        emit this.switchedOn;

    }
}

bool QToggleSwitch::isOn()
{

    if (currentValue == 1) { return true; }

    else { return false; }

}
