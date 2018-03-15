import os
import sys

def rootname(f):
	a = os.path.basename(f)
	aParts = a.split('.')
	return aParts[0]

def makeTrackStr(f,tag):
	str = (	
		'track ' + tag + '\n'
		'bigDataUrl ' + f + '\n'
		'shortLabel ' + tag + '\n'
		'longLabel '  +tag + '\n'
		'type bigBed 5\n'
		'spectrum on\n\n\n'
	       )
	return str

#get top folders
top_folders = [a for a in os.listdir('hg19') if os.path.isdir('hg19/' + a)]

#folder iter
fout = open('hg19/trackDb.txt','w')
for f in top_folders:
	files = [f + '/' + a for a in os.listdir('hg19/' + f) if ".bb" in a]
	for urlIndex in xrange(0,len(files)):
		url = files[urlIndex]
		command = makeTrackStr(url,f+'-'+rootname(url))
		if(urlIndex==len(files)-1):
			command = command.rstrip()
		fout.write(command)
fout.close()
