import os
import time


class ApkEntity:

    def __init__(self, device_type, channel, package_name, version_name, version_code, file_size, md5):
        self.device_type = device_type
        self.channel = channel
        self.package_name = package_name
        self.version_name = version_name
        self.version_code = version_code
        self.file_size = file_size
        self.md5 = md5

    # 根据信息拼接成路径
    def get_path(self):
        return self.device_type + os.sep + self.channel + os.sep + self.version_code + os.sep + self.package_name

    # 返回文件内容
    def file_content(self):
        return self.md5 + \
               self.file_size + \
               self.version_name + \
               time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))

    def to_string(self):
        print("apkEntity =", self.device_type, self.channel, self.package_name, self.version_name,
              self.version_code, self.file_size, self.md5)
