import os


### 默认使用编码格式为utf-8

defaultEncoding="utf-8"

###　得到当前路径 
###  如:D:\workspace\AS_workspace\versions_control\versions
def getCurrentPath():
	return os.path.dirname(__file__)
	pass



### 以当前.py文件的路径作为对照路径作为参考
### 这里的文件夹要事先 创建好 这是个问题，需要修改，会有多级目录存在的情况 需要改成引用文件夹的方式
### 如果没有文件 则生成相应的文件
### relativePath 相对路径 如 os.sep+"test.txt" 代表 "\test.txt"
### content 要书写的内容 请确保是 string 格式
### append 是否追加 true 在原文件后面进行内容的书写 
###                false 清空内容后 从开头进行文件的书写
		
def writeFileString(relativePath,content,append):

	mode="w" 

	if(append):

		mode="a"	

	else:	
		mode="w"

	flie=open(getCurrentPath()+relativePath,mode,encoding=defaultEncoding)	

	try:
		flie.write(content)
		flie.flush
		pass
	except Exception as e:
		raise
	else:
		pass
	finally:
		flie.close()
		pass

	pass

### 以当前.py文件的路径作为对照路径作为参考
### 如果没有文件 则不做任何处理 给于相应的提示
### relativePath 相对路径 如 os.sep+"test.txt" 代表 "\test.txt"
### 返回内容的格式为String
def readFileString(relativePath):
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






