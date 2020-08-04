import cv2
import os

img_path="Google_Search"
dest_path="Google_Search_high_res(200)"
files=os.listdir(img_path)
#print(files)
for f in files:
	img=cv2.imread(img_path+'/'+f)
	(h,w,d)=img.shape
	#new_img=cv2.resize(img,(200,200))
	#cv2.imshow(str(f),img)
	#print(h,w,d)
	#cv2.waitKey()
	#cv2.destroyWindow(str(f))
	
	"""
	if(h>415 and w > 415):
		cv2.imwrite(dest_path+'/'+f,img)
		#This gave around 151 images
	"""
	
	if(h>199 and w > 199):
		cv2.imwrite(dest_path+'/'+f,img)
		#This gave around 239 images
	


