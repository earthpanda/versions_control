import os
import traceback
from ...util.filehelper import *



"""
删除某个文件夹下的所有apk文件

folder_path 文件夹路径

如果文件夹不存在 或者 不是文件夹则不处理

"""
def delete_apks(folder_path):

	if not (os.path.exists(folder_path)):
		print(folder_path +" is not exits")
		return
	
	if not (os.path.isdir(folder_path)):
		print(folder_path+" is not a folder")
		return
	
	try:

		for root,dirs,files in os.walk(folder_path,followlinks=False): 
			for file in files:
				print(os.path.join(root,file))
				pass

		pass

	except Exception as e:
		traceback.print_exc()		
	else:
		pass
	finally:
		pass				



	