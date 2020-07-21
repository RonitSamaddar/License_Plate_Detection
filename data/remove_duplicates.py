import hashlib
import os


IMAGE_PATH="Google_Search2"
DUPLICATES_PATH="Duplicates"
def file_hash(filepath):
	with open(filepath,'rb') as f:
		return hashlib.md5(f.read()).hexdigest()


file_list=os.listdir(IMAGE_PATH)
print(len(file_list))

duplicates={}
flag=0
for filename in file_list:
	fhash=file_hash(IMAGE_PATH+"/"+filename)
	if(fhash in duplicates.keys()):
		duplicates[fhash].append(filename)
		flag=1
	else:
		duplicates[fhash]=[filename]
if(flag==1):
	print("DUPLICATES : ")
	if(DUPLICATES_PATH not in os.listdir()):
		os.system("mkdir "+DUPLICATES_PATH)
	index=1
	for k in duplicates.keys():
		if(len(duplicates[k])>1):
			print("SET "+str(index))
			orig_file=duplicates[k][0]
			os.system("cp "+IMAGE_PATH+"/"+orig_file+" "+DUPLICATES_PATH+"/"+orig_file)
			print(orig_file,end=' ')
			for j in range(1,len(duplicates[k])):
				dup_file=duplicates[k][j]
				os.system("cp "+IMAGE_PATH+"/"+orig_file+" "+DUPLICATES_PATH+"/CopyOf"+orig_file)
				os.remove(IMAGE_PATH+"/"+dup_file)
				print(dup_file,end=' ')
			print(" ")
			index+=1


