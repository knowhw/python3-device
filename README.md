
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

## Library usage
~~~python
from device import lsblk

lsblk.popen("lsblk -fs")
devices = lsblk.devices()

~~~









