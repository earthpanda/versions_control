


import sys,os



### 默认使用编码格式为utf-8


defaultEncoding="utf-8"

###　得到当前路径 以 文件分隔符 作为结尾
def getCurrentPath():
	return os.path.dirname(__file__)+os.sep
	pass


### 以当前.py文件作为参考 进行文件的创建
def createRelativeFile(relatetivePath,append):
	
	pass