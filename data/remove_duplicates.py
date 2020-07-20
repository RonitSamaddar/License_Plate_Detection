import hashlib
import os

IMAGE_PATH="Google_Search2"
def file_hash(filepath):
	with open(filepath,'rb') as f:
		return md5(f.read()).hexdigest()


file_list=os.listdir(IMAGE_PATH)
print(len(file_list))

duplicates={}

