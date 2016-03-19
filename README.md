# QToggleSwitch

`QToggleSwitch` - An on/off switch for Qt

Licensed under the [Apache License 2.0](http://www.apache.org/licenses/LICENSE-2.0)

Inherits `QSlider`.

# Languages

* Python
* C++ (incomplete)

# Demo

(Requires `PyQt5`)

Demos written in Python 2 and 3 are included.

* For Python 2 demo: Run `demo/QToggleSwitch_demo_python2.py`
* For Python 3 demo: Run `demo/QToggleSwitch_demo.py`

# Documentation

## Usage

### Python:
```python
import QToggleSwitch

toggleSwitch = QToggleSwitch.QToggleSwitch(default=0)
```

### C++:
```cpp
#include "QToggleSwitch.hpp"

QToggleSwitch *toggleSwitch = new QToggleSwitch::QToggleSwitch();
```

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
