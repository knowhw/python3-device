from device import attrib
from device import *
# from threading import Thread
# import asyncio # https://docs.python.org/3/library/asyncio.html
import json
device_list=module.collections.dictionary
""" device list """




def popen(argument):
	
	# asyncio.sleep(10, result='hello')
	
	
	return module.popen(argument).read()
"""def ismount_catch(**disk):
	
	test=device_list [disk.get("item")].get(disk ["point"])
	try: 
		return module.mountpoint.exists(test) 
	except: 
		return False
"""
class ismount:
	@classmethod
	def device(name=None, 
uuid=None, label=None):
	
		point = attrib.mountpoint
		if label is not None:
			""" ismount.device(label='pardus') """
			for item in device_list:
				
				if device_list [item][attrib.label] == label:
					path = module.mountpoint.join(module.path.mountpoint, label)
					
					
					return module.mountpoint.exists(path)
		if uuid is not None:
			""" ismount.device(uuid='6335-3364') """
			
			for item in device_list:
				if device_list [item][attrib.uuid] == uuid:
					path = module.mountpoint.join(module.path.mountpoint, uuid)
					
					
					return module.mountpoint.exists(path)
		# if name is not None:
		#	test = device_list[name].get(point)
		#	if test == None: return False
def devices():
	"""
	
	name  device name
	fstype  filesystem type
	mountpoint  where the device is mounted
	label  filesystem LABEL
	uuid  filesystem UUID

	"""
	
	
	for item in module.loads(popen("lsblk --json --fs")). get(attrib.blockdevices.name) :
		
		
		
		if attrib.children in item:
			for item in item.get(attrib.children):
				



				if not item.get(attrib.mountpoint) == "/":
					
					name = item.get(attrib.name)
					device_list [name] = item ; item.pop(attrib.name)
	for disk in device_list:
		
		""" isim\etiket tanimlanmis disk """
		if not device_list [disk] .get("label") == None:
			
			state = ismount.device(label=device_list [disk].get(attrib.label))
			device_list [disk]["plugged"] = attrib.mounted not in device_list.get(disk)
			device_list [disk][attrib.mounted] = state
			
			
			
		else:
			""" isim\etiket tanimlanmamis disk """
			state = ismount.device(uuid=device_list [disk].get(attrib.uuid))
			device_list [disk]["plugged"] = attrib.mounted not in device_list.get(disk)
			device_list [disk][attrib.mounted] = state
	return device_list
def test():
	return devices()
class device:
	def export(devices, path):
		data = json.dumps(devices, indent=4)
		with open(path, "w") as f : 
			f.write(data)



	
