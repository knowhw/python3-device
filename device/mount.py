#!/usr/bin/env python

from os import * 
from device import module, state



class test:
	__result=module.collections.array()
	
	@classmethod
	def device(self):
		return state.devices()
	def hellousb(item):
		module.udisksctl('udisksctl mount -b %s ' % path.join(module.path.dev, item))
		
	def all(devices):
		
		
		keys = module.collections.array(devices.keys())
		push=__class__.__result.append
		
		for item in keys:
			
			label = devices[item] .get('label')
			
			
			uuid = label is None
			if uuid:
				if not state.ismount.device(uuid=devices[item]['uuid']):
					
					push(path.join(module.path.mountpoint, devices[item]['uuid']))
			else:
				if not state.ismount.device(label=label):
					push(push(path.join(module.path.mountpoint, label)))
					
					
					
					
			module.udisksctl('udisksctl mount -b %s > /dev/null 2>1&' % path.join(module.path.dev, item))
		return __class__.__result
	# def mount(devices):
	#	pass
def all(devices): 
	""" # device.mount.all(devices) """
	return test.all(devices)
	

