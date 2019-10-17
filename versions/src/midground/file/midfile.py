import os
import traceback
from ...util.filehelper import delete_feature_file



"""
删除某个文件夹下的所有apk文件 只处理这层的目录 不继续处理下层目录

folder_path 文件夹路径()

如果文件夹不存在 或者 不是文件夹则不处理

"""
def delete_apks(folder_path):
	delete_feature_file(folder_path,".apk")
	pass
	







	