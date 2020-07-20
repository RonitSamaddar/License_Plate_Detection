from PIL import Image
import os

IMAGE_PATH="Google_Search2"
filelist=os.listdir(IMAGE_PATH)
count1=0
count2=0
count=len(filelist)
print("TOTAL FILES : "+str(count))
index=0
for infile in filelist:
	index+=1
	outfile = os.path.splitext(infile)[0] + ".png"
	if infile != outfile:
		try:
			Image.open(IMAGE_PATH+"/"+infile).save(IMAGE_PATH+"/"+outfile)
			count1+=1
			os.remove(IMAGE_PATH+"/"+infile)
		except IOError:
			print ("cannot convert "+infile)
			count2+=1
			os.remove(IMAGE_PATH+"/"+infile)
	print("Finished "+str(index)+"/"+str(count)+" files")
print("TOTAL NOT IN PNG FILES : "+str(count1+count2))
print("CONVERTED : "+str(count1))
print("COULD NOT CONVERTED : "+str(count2))