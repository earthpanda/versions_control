import os
import time


class ApkEntity:

    def __init__(self, device_name, channel, packagename, vername, vercode, filesize, md5):
        self.devicename = device_name
        self.channel = channel
        self.packagename = packagename
        self.vername = vername
        self.vercode = vercode
        self.filesize = filesize
        self.md5 = md5

    # 根据信息拼接成路径
    def get_path(self):
        return self.devicename + os.sep + self.channel + os.sep + self.vercode + os.sep + self.packagename

    # 返回文件内容
    def file_content(self):
        return self.md5 + \
               self.filesize + \
               self.vername + \
               time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))

    def to_string(self):
        print("apkEntity =", self.devicename, self.channel, self.packagename, self.vername, self.vercode, self.filesize,
              self.md5)
