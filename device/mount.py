#!/usr/bin/env python

from device import lsblk
from device import *
from os import * 


class state:
	@classmethod
	def device(self):
		return lsblk.devices()
		
	def all(devices):
		
		
		keys = module.collections.array(devices.keys())
		
		for item in keys:

			module.udisksctl('udisksctl mount -b %s' % path.join(module.path.dev, item))
			
			return __class__.device()
			
	# def mount(devices):
	#	pass
def all(devices): 
	""" # device.mount.all(devices) """
	return state.all(devices)
	
