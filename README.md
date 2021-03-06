# QToggleSwitch

`QToggleSwitch` - An on/off switch for Qt

Licensed under the [Apache License 2.0](http://www.apache.org/licenses/LICENSE-2.0)

Inherits `QSlider`.

# Languages

* Python
* C++ (incomplete; do not use)

# Demo

(Requires `PyQt5`)

A demo written in Python is included. Run `demo/QToggleSwitch_demo.py`.

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

QToggleSwitch *toggleSwitch = new QToggleSwitch();
```

## Parameters

Default value of switch is 0 (off). This can be changed by passing the
`default=` argument on intitialization. This argument accepts
`0` for off and `1` for on.

NOTE: Not yet supported in C++ version.

## Signals

* `toggled` - Emitted when switch's value changes
* `switchedOn` - Emitted when value becomes 1 (on)
* `switchedOff` - Emitted when value becomes 0 (off)

## Functions

* `toggle()` - Programmatically switch on/off

## Properties

* `isOn()` (`Boolean`) - Returns `True` if on; else returns `False`
