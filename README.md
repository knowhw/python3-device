
<div align="right">

[![python](https://img.shields.io/badge/Python-3.10-3776AB.svg?style=flat&logo=python&logoColor=white)](https://www.python.org)
[![python](https://img.shields.io/badge/Python-3.11-3776AB.svg?style=flat&logo=python&logoColor=white)](https://www.python.org)
[![python](https://img.shields.io/badge/Python-3.12-3776AB.svg?style=flat&logo=python&logoColor=white)](https://www.python.org)

</div>

<br/>

# #Device Python Library
device library is a Open Source Python Library that lists USB devices plugged to your computer.
<br/>
<br/>

## Installation
~~~bash
git clone https://github.com/knowhw/python3-device.git
sudo cp -R python3-device/device /usr/local/lib/python3.10
~~~



## Library usage
~~~python
from device import state
devices = state.devices()

~~~
## How to Mounting ALL Usb Disk to System Directory [/media]
~~~python
devices = state.devices()
device.mount.all(devices)
~~~

## How to Export Devices List 
~~~python
devices = state.devices()
state.device.export(devices, "/home/linux/devices.json")
~~~

## devices.json
~~~
{
    "sda1": {
        "fstype": "vfat",
        "label": null,
        "uuid": "4A35-C66D",
        "mountpoint": "/media/linux/4A35-C66D",
        "mounted": false,
        "plugged": true
    },
    "mmcblk1p1": {
        "fstype": "vfat",
        "label": null,
        "uuid": "6335-3364",
        "mountpoint": "/media/linux/6335-3364",
        "mounted": true,
        "plugged": true
    }
}
~~~




