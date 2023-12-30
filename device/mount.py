#!/usr/bin/env python

from os import * 
from device import module, state


class test:
	
	@classmethod
	def device(self):
		return state.devices()
		
	def all(devices):
		
		
		keys = module.collections.array(devices.keys())
		
		for item in keys:
			
			if not state.ismount.device(uuid=devices[item] .get('uuid')):
				module.udisksctl('udisksctl mount -b %s' % path.join(module.path.dev, item))
			
			
		return __class__.device()
	# def mount(devices):
	#	pass
def all(devices): 
	""" # device.mount.all(devices) """
	return test.all(devices)
	

