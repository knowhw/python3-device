
from os import popen
from os import path as mountpoint
from os import system as udisksctl

from os import getenv
from json import dumps, loads




class path:
	mountpoint=f"/media/{getenv('USER')}"
	dev="/dev"


class collections:
	dictionary={}
	array=list
class keys:
	NAME,FSTYPE,LABEL,UUID,MOUNTPOINT="NAME","FSTYPE","LABEL","UUID","MOUNTPOINT";
	



	


