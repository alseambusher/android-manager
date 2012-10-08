from config import *
import os
#use file explorer and write music files..etc
def main():
	dbdir=os.path.join(local,".%s"%software_name)
	dbfile=os.path.join(dbdir,"database.sqlite")
	logfile=os.path.join(dbdir,"log")
	temp=os.path.join(dbdir,"temp")
	if not os.path.isdir(dbdir):
		os.mkdir(dbdir)
	if not os.path.isdir(temp):
		os.mkdir(temp)
	else:
		#delete all the temporary files
		for _temp in os.listdir(temp):
			os.remove("%s/.%s/temp/%s"%(local,software_name,_temp))
	if not os.path.exists(dbfile):
		open(dbfile,"w+")
	if not os.path.exists(logfile):
		open(logfile,"w+")

if __name__ == '__main__':
	main()
