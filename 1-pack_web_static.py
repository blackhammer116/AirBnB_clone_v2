#!/usr/bin/python3
from datetime import datetime
from fabric.api import local
import os
""" 
	These are modules we're going to use to pack the AirBnB file 
"""
def do_pack():
	"""
		this function performs the task of
		archiving the file web_static
	"""
	timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
	path = "versions/web_static_{}.tzg".format(timestamp)
	if not os.path.exists("versions"):
		local ("mkdir versions")
	if (local("tar cvf {} web_static".format(path))):
		return path
	else:
		return None
