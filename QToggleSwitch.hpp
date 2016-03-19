/* QToggleSwitch - Header

   Copyright (c) 2016 Bharadwaj Raju All Rights Reserved.

   Licensed under the Apache License 2.0 - http://www.apache.org/licenses/LICENSE-2.0

 */

#ifndef QTOGGLESWITCH_H
#define  QTOGGLESWITCH_H

class QToggleSwitch : public QSlider():

    /* # QToggleSwitch - An on/off switch for Qt

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

    */

    Q_OBJECT

    public:

        QToggleSwitch(int defaultValue);

        bool isOn();

    signals:

        void toggled();

        void switchedOn();

        void switchedOff();

    slots:

        void toggle();


#endif
