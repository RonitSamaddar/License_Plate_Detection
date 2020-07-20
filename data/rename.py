import os
import argparse
import sys

"""ap = argparse.ArgumentParser()
ap.add_argument('-t', '--target', required=True,
                help = 'Target Path (Path where files to be renamed are in)')
args = ap.parse_args()"""

#TARGET_PATH=args.target+'/'
TARGET_PATH="/media/ronit/DATA21/Programming/License_Plate_Detection/data/Google_Search2"
DEST_PATH="/media/ronit/DATA21/Programming/License_Plate_Detection/data/Google_Search2"

if(DEST_PATH==TARGET_PATH):
	count=1
else:
	count=len(os.listdir(DEST_PATH))+1

files=os.listdir(TARGET_PATH)
for f in files:
	f2=f.split('.')
	#print(f,f2)
	#sys.stdin.read(2)
	
	if(f2[-1]=='jpg' or f2[-1]=='jpeg' or f2[-1]=='png'):
		print(f,f2)
		f3="i"+str(count)+"."+f2[-1]
		count=count+1
		os.rename(TARGET_PATH+'/'+f,TARGET_PATH+'/'+f3)
	else:
		os.remove(TARGET_PATH+'/'+f)