import os
import platform


"""
是否是debug
"""
def debug():
	return root.endswith("versions")

"""
是否是windows
"""
def windows():
	return (platform.system())=="Windows"	




"""
	用来上传apk信息的path
"""
global upload_folder_path


"""

	本地下载的apk的路径 如tower下载下来的路径

"""
global default_local_download_apk_path

root=os.getcwd()


print("config.py "+"root is "+root)


"""
根据是否是debug 来进行不同值的配置
"""
if(debug()):
	upload_folder_path=os.path.join(os.getcwd(), "..", "..", "VersionsRecord", "file")
else:
	upload_folder_path=os.path.join(os.getcwd(),"file")


"""
根据不同平台设置不同的一些值
"""
if(windows()):
	default_local_download_apk_path="C:/Users/Admin/Downloads"
	pass
else:
	pass	
	




