#!/usr/bin/env python
# coding:utf-8

import os
import re

# 检查apk版本号等信息


class ApkParser:

    apkInfo = {'packagename': '', 'versionCode': '', 'versionName': '',
               "localPath": ''}

    def getAppBaseInfo(self, param_apk_path):
        get_info_command = "aapt dump badging %s" % (param_apk_path)
        output = os.popen(get_info_command).read()
        match = re.compile(
            "package: name='(\S+)' versionCode='(\d+)' versionName='(\S+)'").match(output)
        if not match:
            print(output)
            raise Exception("can't get packageinfo")

        packagename = match.group(1)
        versionCode = match.group(2)
        versionName = match.group(3)
        # print(u" 包名：%s \n 版本号：%s \n 版本名称：%s " % (packagename,
        # versionCode,
        # versionName))
        self.apkInfo['packagename'] = packagename
        self.apkInfo['versionCode'] = versionCode
        self.apkInfo['versionName'] = versionName
        self.apkInfo['localPath'] = param_apk_path


if __name__ == '__main__':
    # path = os.path.abspath(os.path.dirname(__file__)) + "\\"
    apk_path = "adb.apk"  # apk地址
    apkParser = ApkParser()
    apkParser.getAppBaseInfo(apk_path)
    print(apkParser.apkInfo)
