#os.system("%s push README.md /sdcard/apk"%adb)
#make local storage
#make config.py file if it doesnt exits
import adb
import gtk,sys
import config
class window(gtk.Window):
	def __init__(self):
		super(window,self).__init__()
		self.set_title("Install android manager")
		self.set_size_request(500,500)
		self.modify_bg(gtk.STATE_NORMAL,gtk.gdk.Color(config.background))
		self.set_position(gtk.WIN_POS_CENTER)
		#self.set_icon_from_file("icon.png")
		self.connect("delete_event",gtk.main_quit)

		self.show_all()
window()
gtk.main()
#adb.open_file("/sdcard/download/timetable.xls")
#if adb.push("log","/sdcard/"):
	#print "success"
#else:
	#print "failed"
file_explorer=adb.file_explorer()
adb.stdout_printer(file_explorer.search("/sdcard/","srs"))
#adb.stdout_pull(file_explorer.documents("/sdcard/","xls"),"/home/alse/temp/")
#adb.stdout_pull(file_explorer.documents("/sdcard/","pdf"),"/home/alse/temp/")
#adb.stdout_pull(file_explorer.documents("/sdcard/","doc"),"/home/alse/temp/")
#adb.stdout_pull(file_explorer.documents("/sdcard/","docx"),"/home/alse/temp/")
#adb.stdout_pull(file_explorer.documents("/sdcard/","ppt"),"/home/alse/temp/")
#adb.stdout_pull(file_explorer.documents("/sdcard/","pptx"),"/home/alse/temp/")
#adb.stdout_printer(file_explorer.documents("/sdcard/","pdf"))
#file_explorer.files_formatted("/sdcard/")
#adb.stdout_printer(adb.services())
#adb.file_explorer.print_directories("/sdcard")
#a=adb.shell("ls")
#k="0"
#for i in a.stdout.readlines():
	#print i
#system=adb.system()
#system.reboot("recovery")
if __name__=='__main__':
	pass
