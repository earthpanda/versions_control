import os
import traceback
from ...util.filehelper import delete_file



"""
删除某个文件夹下的所有apk文件 只处理这层的目录 不继续处理下层目录

folder_path 文件夹路径()

如果文件夹不存在 或者 不是文件夹则不处理

"""
def delete_apks(folder_path):
	delete_feature_file(folder_path,".apk")
	pass
	


"""
	删除某路径当前目录下的某种文件

	older_path 文件夹路径()
	suffix 文件格式后缀 ".txt" ".apk"...
	如果文件夹不存在 或者 不是文件夹则不处理
"""
def delete_feature_file(folder_path,suffix):


	if not (os.path.exists(folder_path)):
		print(folder_path +" is not exits")
		return
	
	if not (os.path.isdir(folder_path)):
		print(folder_path+" is not a folder")
		return
	
	try:
		# 获取当前目录下的所有文件
		list=os.listdir(folder_path)

		for i in range(len(list)):

			is_detele_file=str(list[i]).endswith(suffix)

			if(is_detele_file):
				delete_file(os.path.join(folder_path,list[i]),False)
				print(os.path.join(folder_path,list[i])+" deleted")
			pass

		pass

	except Exception as e:
		traceback.print_exc()		
	else:
		pass
	finally:
		pass	

	pass




	