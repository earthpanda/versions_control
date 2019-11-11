
"""

	提供关于平台信息的配置入口类
	主要提供如下信息：
	1. 平台信息 含有哪些平台
	2. 平台中关于具体apk的上传路径
	3. 其它的一些约定行为 如 framework使用 customConfig这种类似的手段等... 这个也可以考虑在内部定义


"""
class ConfigIndex(object) :
	"""

		平台信息 如F1 C1 ....
	"""
	platform=""

	"""

		依据一定的规则书写的路径 目前路径存放的地址在VersionsRecords>>config下
	
	"""
	config_path=""

	def  __init__(self):
		pass

	def set_platform(self,platform):
		
		self.platform=platform
		pass
	
	def get_platform(self):

		return self.platform

	def set_config_path(self,config_path):
		self.config_path=config_path
		pass


	def get_config_path(self):
		
		return self.config_path	
		


