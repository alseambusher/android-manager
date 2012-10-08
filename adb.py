from config import *
import os
import sys
import subprocess
import time
import basic_functions
#TODO find a way to log all the commands into the sys log
def stdout_printer(data):
	for i in data.stdout.readlines():
		i=i[:len(i)-2]
		print i

def stdout_pull(data,location):
	for i in data.stdout.readlines():
		i=i[:len(i)-2]
		print i
		pull("'%s'"%i,location)

def push(content,destination):
	if os.system("%s push %s %s"%(adb,content,destination)) is not 0:
		return False
	else:
		return True
def pull(content,destination):
	if os.system("%s pull %s %s"%(adb,content,destination)) is not 0:
		return False
	else:
		return True
def open_file(_file):
	print "opening %s"%_file
	pull(_file,"%s/.%s/temp/ "%(local,software_name))
	_file_temp="%s/.%s/temp/%s"%(local,software_name,_file.split("/")[-1])
	#mac
	if sys.platform.startswith('darwin'):
		subprocess.call(('open',_file_temp))
	#windows
	elif os.name=='nt':
		os.startfile(_file_temp)
	#linux
	elif os.name=='posix':
		subprocess.call(('xdg-open',_file_temp))
	# TODO push it back and delete temporary file
	#push(_file_temp,_file)
	#os.remove(_file_temp)
#TODO make a sqlite database and push all the temp files
def push_temp_all():
	pass

def shell(command):
	#this will just  execute it
	if os.system("%s shell %s &"%(adb,command)) is not 0:
		return False
	else:
		return True
def terminal(command):
	#this will execute values and return results
	return subprocess.Popen("%s shell %s"%(adb,command),shell=True,stdout=subprocess.PIPE)
def services():
	return terminal("service list")
class file_explorer:
	def directories(self,location):
		return terminal("ls -l -a %s | egrep '^d'"%location)
	def files(self,location):
		return terminal("ls -l -a  %s | egrep '^-'"%location)
	def links(self,location):
		return terminal("ls -l -a %s | egrep '^l'"%location)
	def others(self,location):
		return terminal("ls -l -a %s | egrep -v -e '^d' -e '^-' -e '^l'"%location)
	def music(self,location):
		return terminal("find %s -name '*.mp3' | grep 'mp3'"%location)
	def photos(self,location):
		return terminal("find %s -name '*.jpg' -o -name '*.png' -o -name '*.gif'"%location)
	def documents(self,location,doc_type):
		return terminal("find %s -name '*.%s'"%(location,doc_type))
	def directories_formatted(self,location):
	#TODO trim each string and do this
		#0-permissions 1-owner 4-group 14-date 15-time 16 and above -name
		for directory in self.directories(location).stdout.readlines():
			print directory[:len(directory)-2].split(" ")[1]
	def files_formatted(self,location):
	#TODO fix this
		#0-permissions 1-owner 4-group 14-date 15-time 16-name
		for _file in self.files(location).stdout.readlines():
			print _file[:len(_file)-2].split(" ")[0]
	def print_directories(self,location):
		for directory in self.directories(location).stdout.readlines():
			print directory[:len(directory)-2]
	def print_files(self,location):
		for _file in self.files(location).stdout.readlines():
			print _file[:len(_file)-2]
	def print_links(self,location):
		for link in self.links(location).stdout.readlines():
			print link[:len(link)-2]
	def print_others(self,location):
		for other in self.others(location).stdout.readlines():
			print other[:len(other)-2]
	def print_music(self,location='/sdcard/'):
		for _music in self.music(location).stdout.readlines():
			print _music[:len(_music)-2]
	def print_photos(self,location='/sdcard/'):
		for photo in self.photos(location).stdout.readlines():
			print photo[:len(photo)-2]

class dumpsys:
	def all(self):
		return terminal("dumpsys")
	def specific(self,query):
		#can be battery wifi bluetooth cpuinfo meminfo 
		return terminal("dumpsys %s"%query);
class system:
	def reboot(self,mode=""):
		#"", recovery
		shell("adb reboot %s"%mode)	
