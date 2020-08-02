import cv2
import os

img_path="Google_Search"
dest_path="Google_Search_resized"
files=os.listdir(img_path)
#print(files)
for f in files:
	img=cv2.imread(img_path+'/'+f)
	new_img=cv2.resize(img,(200,200))
	#cv2.imshow(str(f),new_img)
	#cv2.waitKey()
	#cv2.destroyWindow(str(f))
	cv2.imwrite(dest_path+'/'+f,new_img)
