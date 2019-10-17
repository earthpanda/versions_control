import os
import traceback
import shutil

### 默认使用编码格式为utf-8

defaultEncoding = "utf-8"

"""

对文件进行写入操作
如果没有文件 则生成相应的文件
folder_path 文件夹目录
content 要书写的内容 请确保是 string 格式
append 是否追加 true 在原文件后面进行内容的书写 
               false 清空内容后 从开头进行文件的书写

"""


def write_file_string(folder_path, file_name, content, append):
    mode = "w"
    file = None

    if (append):
        mode = "a"

    else:
        mode = "w"

    try:
        folder = os.path.join(folder_path)

        # 如果文件夹不存在 则进行创建
        if not (os.path.exists(folder)):
            os.makedirs(folder, 0o777)

        path = os.path.join(folder, file_name)
        flie = open(path, mode, encoding=defaultEncoding)
        flie.write(content)
        flie.flush
        pass

    except Exception as e:
        traceback.print_exc()


    else:
        pass


    finally:
        if (None != file):
            flie.close()
        pass

    pass


"""

读取一个文件的内容 以String的格式返回
如果没有文件 则不做任何处理 给于相应的提示
file_path 文件路径
返回内容的格式为String

"""


def read_file_string(file_path):
    mode = "r"
    file = None

    try:
        file = open(os.path.join(file_path), mode, encoding=defaultEncoding)
        contentLines = file.readlines()
        content = ""
        for line in contentLines:
            content = content + line
            pass

        return content



    except Exception as e:
        traceback.print_exc()

    finally:
        if (None != file):
            file.close()

        pass

    pass


"""
重命名一个文件 返回重命名后的绝对路径
如果文件不存在 则不做任何处理 给予相应的提示
folder_path 文件夹目录
file_name 原先的文件名称
file_rename 重命名的文件名称

"""


def rename_file(folder_path, file_name, file_rename):
    try:
        os.rename(os.path.join(folder_path, file_name), os.path.join(folder_path, file_rename))
        return os.path.join(folder_path, file_rename)
    except Exception as e:

        traceback.print_exc()
    else:
        pass
    finally:
        pass




"""

 如果文件不存在 则不做任何处理 给予相应的提示
 path 文件或者文件夹的路径 
 is_folder 是否是文件夹
 如果删除成功 返回 true 否则 返回false
 注意os.removedirs 用于删除空目录 如果有文件则不删除

"""
def delete_file(path,is_folder):



	try:

		if(is_folder):

			shutil.rmtree(path)

		else:
			os.remove(path)

		return True
		
	except Exception as e:
		traceback.print_exc()
	else:
		pass
	finally:
		pass


"""

copy文件
进行文件copy 如果没有原文件 则 不做任何处理 给予相应的提示
path_src 原路径 
path_dst 目标路径
如果copy成功 返回 true 否则 返回false

"""

def copy_file(path_src, path_dst):

	try:

		shutil.copyfile(path_src,path_dst)
		pass

	except Exception as e:
		
		traceback.print_exc()

	else:
		pass
	finally:
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

"""
    删除某个文件夹下的所有文件
    如果不是文件夹 或者 文件不存在则不处理

    folder_path 文件夹路径
"""
def delete_all_in_folder(folder_path):

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
            path=os.path.join(folder_path,list[i])
            delete_file(path,os.path.isdir(path))
          
        pass

    except Exception as e:
        traceback.print_exc()       
    else:
        pass
    finally:
        pass    

    pass    


    pass    
    
