

import traceback
import os
import json

from ...util.filehelper import write_file_string,read_file_string
from ...util.time import format_time2
from ...entity.ApkEntity import ApkEntity


root=os.path.join(os.getcwd(),"file")

"""
更新apk的信息

{
	"model": "F1",
	"code": "20800",
	"content": [{
		"versionName": "f1_20800",
		"versionCode": "20800",
		"packageName": "com.dangbei.xxx",
		"md5": "xxxx",
		"length": "11111",
		"channel": "DBOS_F1"}]
}

"""
def update_apk_infos(json_string):

	try:

	   	### 进行json解析
	   	data_in=json.loads(json_string)

	   	### 获取相关的model和code
	   	model=data_in["model"]
	   	code=data_in["code"]
	   	app_infos=data_in["content"]


	   	### 进行文件夹和文件名称的定义
	   	folder_path=os.path.join(root,model,code)
	   	file_name="1.txt"
	   	### 最新需要写入的信息
	   	write_info=format_time2()
	   	### 是否需要新建文件
	   	create_new_file=False
	   	### 如果文件存在 需要通过某种规则更新文件信息
	   	if(os.path.exists(os.path.join(folder_path,file_name))):

	   		
	   		
	   		### 读取文件中存储的内容 过滤更新时间的信息 将
	   		s=read_file_string(os.path.join(folder_path,file_name))
	   		file_infos=list(s.split("\n"))[1:]

	   		### 将app_info中含有的信息写入文件
	   		for app_info in iter(app_infos):
	   			i=0
	   			### 读取的在文件中已经保存的信息	
	   			for file_info in iter(file_infos):
	   				### demo ['com.dangbei.2', 'f1_20800', '20800', 'DBOS_F1', 'xxxx', '11111']
	   				### 格式转换成list
	   				
	   				file_info_entity=list(file_info.split(" "))
	   				###判断是否包名一致
	   				if(file_info_entity[0]==app_info["packageName"]):
	   					###如果版本一致 则需要把文件中的信息替换成app_info的信息
	   					if(file_info_entity[2]==app_info["versionCode"]):

	   						write_info=write_info+"\n"+app_info["packageName"]+" "+app_info["versionName"]+" "+app_info["versionCode"]+" "+app_info["channel"]+" "+app_info["md5"]+" "+app_info["length"]
	   						pass

	   					###发现有一个版本code不一致 则需要将信息写入新的文件中去	
	   					else:
	   						write_info=write_info+"\n"+app_info["packageName"]+" "+app_info["versionName"]+" "+app_info["versionCode"]+" "+app_info["channel"]+" "+app_info["md5"]+" "+app_info["length"]
	   						create_new_file=True
	   						file_name="2.txt"
	   						pass
	   				###包名不一致 则进行i++ 如果i最终值和file_infos.length一致 说明该app_info 在文件中不存在 需要进行添加	
	   				else:	
	   					i=i+1

	   				pass
	   			### 说明该app_info 在文件中以前没有写入过 则需要进行添加
	   			if(i==len(file_infos)):
	   				write_info=write_info+"\n"+app_info["packageName"]+" "+app_info["versionName"]+" "+app_info["versionCode"]+" "+app_info["channel"]+" "+app_info["md5"]+" "+app_info["length"]
	   				pass

	   		### 将file_info中含有的信息 但是 app_info中不含有的信息 写入文件

	   		for file_info in iter(file_infos):

	   			i=0
	   			file_info_entity=list(file_info.split(" "))

	   			for app_info in iter(app_infos):

	   				if(app_info["packageName"]!=file_info_entity[0]):
	   					i=i+1
	   					pass

	   				pass
	   			
	   			if(i==len(app_infos)):

	   				write_info=write_info+"\n"+file_info_entity[0]+" "+file_info_entity[1]+" "+file_info_entity[2]+" "+file_info_entity[3]+" "+file_info_entity[4]+" "+file_info_entity[5]
	   			
	   			pass		

	   	### 如果文件不存在			
	   	else:

	   			### 获取相关apk信息
	   		for app_info in iter(app_infos):

	   			write_info=write_info+"\n"+app_info["packageName"]+" "+app_info["versionName"]+" "+app_info["versionCode"]+" "+app_info["channel"]+" "+app_info["md5"]+" "+app_info["length"]

	   			pass
	   		pass	

	   	if(create_new_file):

	   		write_file_string(os.path.join(root,model,code),file_name,write_info,False)
	   		pass
	   	else:

	   		write_file_string(os.path.join(root,model,code),file_name,write_info,False)

	   		pass	



	   	
	
	except Exception as e:
		traceback.print_exc()
	else:
		pass
	finally:
		pass
	pass

"""

得到最近一次的apk信息

{
	"model": "F1",
	"code": "20800"
}

"""
def get_apk_infos(json):
	print("get_apk_infos")
	pass

"""

创建需要记录的文件

"""
def _update_record_file():

	pass	




	


"""

需要记录的文件是否存在

"""
def _is_record_file_exist(model,os):

	pass			

