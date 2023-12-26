
[![python](https://img.shields.io/badge/Python-3.10-3776AB.svg?style=flat&logo=python&logoColor=white)](https://www.python.org)
[![python](https://img.shields.io/badge/Python-3.11-3776AB.svg?style=flat&logo=python&logoColor=white)](https://www.python.org)
[![python](https://img.shields.io/badge/Python-3.12-3776AB.svg?style=flat&logo=python&logoColor=white)](https://www.python.org)
<br/>

# Device Python Library
device library is a Open Source Python Library that lists USB devices mounted to your computer.
<br/>
<br/>

## Installation
~~~
git clone https://github.com/knowhw/python3-device.git
sudo cp -R python3-device/device /usr/local/lib/python3.10
~~~


## How to Export Device List.
~~~
{
    "sda1": {
        "fstype": "vfat",
        "label": null,
        "uuid": "4A35-C66D",
        "mountpoint": "/media/linux/4A35-C66D",
        "mounted": false
    },
    "mmcblk1p1": {
        "fstype": "vfat",
        "label": null,
        "uuid": "6335-3364",
        "mountpoint": "/media/linux/6335-3364",
        "mounted": false
    }
}
~~~
## Library usage
~~~python
from device import lsblk

lsblk.popen("lsblk -fs")
devices = lsblk.devices()

~~~






