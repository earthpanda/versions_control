import os


"""
	用来上传apk信息的path
"""

def debug():
	return root.endswith("versions")

global upload_folder_path

root=os.getcwd()


print("config.py "+"root is "+root)




"""
根据是否是debug 来进行不同值的配置
"""
if(debug()):
	upload_folder_path=os.path.join(os.getcwd(), "..", "..", "VersionsRecord", "file")
else:
	upload_folder_path=os.path.join(os.getcwd(),"file")
	





### debug windows 
# upload_folder_path=os.path.join(os.getcwd(), "..", "..", "VersionsRecord", "file")

### debug mac
# upload_folder_path=os.path.join(os.getcwd(),"..","..","VersionsRecord","file")


### .exe windows 
# upload_folder_path=os.path.join(os.getcwd(),"file")


### .exe mac 
# upload_folder_path=os.path.join(os.getcwd(),"file")



