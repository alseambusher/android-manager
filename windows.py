import pygtk
pygtk.require('2.0')
import gtk
class main_window:
	def __init__(self):
		self.window=gtk.Window(gtk.WINDOW_TOPLEVEL)
		self.window.connect('delete_event',self.quit)
		self.window.show()
	def main(self):
		gtk.main()
	def quit(self,widget,data=None):
		gtk.main_quit()
if __name__=='__main__':
	window=main_window()
	window.main()
