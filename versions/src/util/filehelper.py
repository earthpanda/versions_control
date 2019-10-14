import os,traceback  


### 默认使用编码格式为utf-8

defaultEncoding="utf-8"

###　得到当前路径 
###  如:D:\workspace\AS_workspace\versions_control\versions
def getCurrentPath():
	return os.path.dirname(__file__)
	pass



### 以当前.py文件的路径作为对照路径作为参考 	
### 举例 writeFileString("test","test.txt","this is a test",True)
### \test\test.txt

### 多级目录 writeFileString("one\\two\\three","test.txt","this is a test",True)
### \one\two\three\test.txt

### 如果没有文件 则生成相应的文件
### relativeFolderPath 相对路径 以当前.py文件作为参考路径 进行相应文件夹创建
### content 要书写的内容 请确保是 string 格式
### append 是否追加 true 在原文件后面进行内容的书写 
###                false 清空内容后 从开头进行文件的书写
		
def writeFileString(relativeFolderPath,fileName,content,append):

	mode="w" 
	file=None

	if(append):
		mode="a"	

	else:	
		mode="w"

	try:
		folder=os.path.join(getCurrentPath(),relativeFolderPath)
		
		#如果文件夹不存在 则进行创建	
		if not(os.path.exists(folder)):
			os.makedirs(folder,0o777)
	
		path=os.path.join(folder,fileName)
		flie=open(path,mode,encoding=defaultEncoding)
		flie.write(content)
		flie.flush
		pass

	except Exception as e:
		traceback.print_exc()

	else:
		pass

	finally:
		if (None!=file):
			flie.close()
		pass

	pass


### 读取一个文件的内容 以String的格式返回
### 举例 filehelper.readFileString("one\\two\\three\\test.txt")
### 以当前.py文件的路径作为对照路径作为参考
### 如果没有文件 则不做任何处理 给于相应的提示
### relativePath 相对路径带文件名 如 "one\\two\\three\\test.txt"
### 返回内容的格式为String
def readFileString(relativePath):
	mode="r"
	file=None

	try:
		file=open(os.path.join(getCurrentPath(),relativePath),mode,encoding=defaultEncoding)
		contentLines=file.readlines()
		content=""
		for line in contentLines:
			content=content+line
			pass

		return content


	except Exception as e:
		traceback.print_exc()

	finally:
		if(None!=file):
			file.close()

		pass


	pass


### 以当前.py文件的路径作为对照路径作为参考
### 如果文件不存在 则不做任何处理 给予相应的提示
### relativePath 相对路径 如 os.sep+"test.txt" 代表 "\test.txt"
### 重命名文件 返回重命名后的绝对路径
def renameFile(relativePath):
	pass

### 以当前.py文件的路径作为对照路径作为参考
### 如果文件不存在 则不做任何处理 给予相应的提示
### relativePath 相对路径 如 os.sep+"test.txt" 代表 "\test.txt"
### 如果删除成功 返回 true 否则 返回false
def deleteFile(relativePath):
	pass

### 以当前.py文件的路径作为对照路径作为参考
### 进行文件copy 如果没有原文件 则 不做任何处理 给予相应的提示
### relativePathSrc 原相对路径 如 os.sep+"test.txt" 代表 "\test.txt"
### relativePathDst 需要copy的文件地址 如 os.sep+"test.txt" 代表 "\test.txt"
### 如果copy成功 返回 true 否则 返回false
def copyFile(relativePathSrc,relativePathDst):
	pass






