import os
import traceback
from ...util.filehelper import delete_feature_file,delete_all_in_folder



"""
删除某个文件夹下的所有apk文件 只处理这层的目录 不继续处理下层目录

folder_path 文件夹路径()

如果文件夹不存在 或者 不是文件夹则不处理

"""
def delete_apks(folder_path):
	delete_feature_file(folder_path,".apk")
	pass

"""
清空某个目录下的所有文件
folder_path 文件夹路径
"""
def delete_all(folder_path):
	delete_all_in_folder(folder_path)
	pass	


def rename_apks(folder_path):

	pass





	







	