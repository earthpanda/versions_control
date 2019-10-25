import os
from src.util.time import *


class ApkEntity:
    """
    初始化apk实体类
    channel : 渠道
    package_name : 包名
    version_name : 版本名
    version_code : 版本号
    file_size : 文件大小
    md5 : 文件md5值
    """
    def __init__(self, package_name, version_name, version_code, channel, md5, file_size):
        self.channel = channel
        self.package_name = package_name
        self.version_name = version_name
        self.version_code = version_code
        self.file_size = file_size
        self.md5 = md5

    # 根据信息拼接成路径
    def get_path(self):
        return self.channel + os.sep + self.version_code + os.sep + self.package_name

    # 返回文件内容
    def file_content(self):
        return "上传时间：" + format_time2() + "\n" + \
               "MD5：" + self.md5 + "\n" + \
               "apk大小：" + self.file_size + "\n" + \
               "版本名称：" + self.version_name

    def to_string(self):
        print("apkEntity =", self.channel, self.package_name, self.version_name,
              self.version_code, self.file_size, self.md5)
