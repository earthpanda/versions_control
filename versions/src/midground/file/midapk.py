

import traceback
import os
import json
import git
import re



from ...util.filehelper import write_file_string, read_file_string
from ...util.time import format_time2
from ...entity.ApkEntity import ApkEntity
from ...util.apk_info_reader import *
from ...config import config as gl

# 需项目工程配置和VersionsRecord 项目同目录
root = gl.upload_folder_path

print("midapk root is "+root)


"""
更新apk的信息

json_string

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


如果存储成功 返回True 否则返回 None

"""


def update_apk_infos(json_string):
    _pull_file_from_git()
    # 将记录更新到文件中
    if(_update_record_file(json_string)):
        _push_file_to_git()
        return True
    pass


"""

得到最近一次的apk信息

{
	"model": "F1",
	"code": "20800"
}


如果文件不存在 则返回""
如果存在则返回

{"model": "F1",
	"code": "20801",
	"content": [{
		"versionName": "f1_20802",
		"versionCode": "20803",
		"packageName": "com.dangbei.0",
		"md5": "xxxx",
		"length": "11112",
		"channel": "DBOS_F1"}]
}

这样的json格式

"""


def get_apk_infos(json_string):

    try:
        data_in = json.loads(json_string)
        model = data_in["model"]
        code = data_in["code"]

        folder_path = os.path.join(root, model, code)

        # 文件不存在
        if not (os.path.exists(folder_path)):
            return ""

        file_name = _get_recent_file_name(folder_path)

        # 列表中第一个字符是更新时间 这里将它剔除 从而获取到相关的文件信息展示
        # packageName versionName versionCode channel md5 length
        apk_infos = list(read_file_string(os.path.join(
            folder_path, file_name)).split("\n"))[1:]

        # 声明列表
        items = []

        for apk_info in iter(apk_infos):
            dict = {}

            apk_list = list(apk_info.split(" "))
            dict["packageName"] = apk_list[0]
            dict["versionName"] = apk_list[1]
            dict["versionCode"] = apk_list[2]
            dict["channel"] = apk_list[3]
            dict["md5"] = apk_list[4]
            dict["length"] = apk_list[5]

            # 在列表中添加关于相应的字典
            items.append(dict)

            pass

        # 字典转json
        dict = {}
        dict["model"] = model
        dict["code"] = code
        dict["content"] = items

        return json.dumps(dict)

    except Exception as e:

        traceback.print_exc()
    else:
        pass
    finally:
        pass

    pass


"""

更新需要记录的文件

"""


def _update_record_file(json_string):

    try:
        # 进行json解析
        data_in = json.loads(json_string)

        # 获取相关的model和code
        model = data_in["model"]
        code = data_in["code"]
        app_infos = data_in["content"]

        # 进行文件夹和文件名称的定义
        folder_path = os.path.join(root, model, code)

        file_name = _get_recent_file_name(folder_path)
        # 最新需要写入的信息
        write_info = format_time2()
        # 如果文件存在 需要通过某种规则更新文件信息
        if(os.path.exists(os.path.join(folder_path, file_name))):

            # 读取文件中存储的内容 过滤更新时间的信息 将
            s = read_file_string(os.path.join(folder_path, file_name))
            file_infos = list(s.split("\n"))[1:]

            # 将app_info中含有的信息写入文件
            for app_info in iter(app_infos):
                i = 0
                # 读取的在文件中已经保存的信息
                for file_info in iter(file_infos):
                    ### demo ['com.dangbei.2', 'f1_20800', '20800', 'DBOS_F1', 'xxxx', '11111']
                    # 格式转换成list

                    file_info_entity = list(file_info.split(" "))
                    # 判断是否包名一致
                    if(file_info_entity[0] == app_info["packageName"]):
                        # 如果版本一致 则需要把文件中的信息替换成app_info的信息
                        if(file_info_entity[2] == app_info["versionCode"]):

                            write_info = write_info+"\n"+app_info["packageName"]+" "+app_info["versionName"]+" " + \
                                app_info["versionCode"]+" "+app_info["channel"] + \
                                " "+app_info["md5"]+" "+app_info["length"]
                            pass

                        # 发现有一个版本code不一致 则需要将信息写入新的文件中去
                        else:
                            write_info = write_info+"\n"+app_info["packageName"]+" "+app_info["versionName"]+" " + \
                                app_info["versionCode"]+" "+app_info["channel"] + \
                                " "+app_info["md5"]+" "+app_info["length"]
                            file_name = (str)(
                                len(os.listdir(folder_path))+1)+".txt"
                            pass
                    # 包名不一致 则进行i++ 如果i最终值和file_infos.length一致 说明该app_info 在文件中不存在 需要进行添加
                    else:
                        i = i+1

                    pass
                # 说明该app_info 在文件中以前没有写入过 则需要进行添加
                if(i == len(file_infos)):
                    write_info = write_info+"\n"+app_info["packageName"]+" "+app_info["versionName"]+" " + \
                        app_info["versionCode"]+" "+app_info["channel"] + \
                        " "+app_info["md5"]+" "+app_info["length"]
                    pass

            # 将file_info中含有的信息 但是 app_info中不含有的信息 写入文件

            for file_info in iter(file_infos):

                i = 0
                file_info_entity = list(file_info.split(" "))

                for app_info in iter(app_infos):

                    if(app_info["packageName"] != file_info_entity[0]):
                        i = i+1
                        pass

                    pass

                if(i == len(app_infos)):

                    write_info = write_info+"\n"+file_info_entity[0]+" "+file_info_entity[1]+" " + \
                        file_info_entity[2]+" "+file_info_entity[3] + \
                        " "+file_info_entity[4]+" "+file_info_entity[5]

                pass

        # 如果文件不存在
        else:
            # 获取相关apk信息
            for app_info in iter(app_infos):
                write_info = write_info+"\n"+app_info["packageName"]+" "+app_info["versionName"]+" " + \
                    app_info["versionCode"]+" "+app_info["channel"] + \
                    " "+app_info["md5"]+" "+app_info["length"]
                pass
            pass

        write_file_string(os.path.join(root, model, code),
                          file_name, write_info, False)
        print("_update_record_file")

        return True

    except Exception as e:
        traceback.print_exc()

    else:
        pass
    finally:
        pass
    pass


"""
上传文件到git仓库


"""


def _push_file_to_git():

    try:

        folder_path = os.path.abspath(os.path.join(root, ".."))
        repo = git.Repo.init(path=folder_path)
        repo.git.add(".")
        repo.git.commit(m="update_file "+str(format_time2()))
        repo.git.push()
        print(repo.git.status())
        pass

    except Exception as e:
        traceback.print_exc()
    else:
        pass
    finally:
        pass


"""
拉文件到本地
"""


def _pull_file_from_git():

    try:
        print("_pull_file_from_git")
        folder_path = os.path.abspath(os.path.join(root, ".."))
        repo = git.Repo.init(path=folder_path)
        repo.git.fetch()
        repo.git.pull()

        pass
    except Exception as e:
        traceback.print_exc()
    else:
        pass


"""
得到最新的一个文件的名称
"""


def _get_recent_file_name(folder_path):

    # 如果文件夹存在
    if(os.path.exists(folder_path)):
        length = len(os.listdir(folder_path))
        if(length == 0):
            return "1.txt"
        else:
            return str(length)+".txt"

    return "1.txt"


class ApkParser:

    apkInfo = {'packageName': '', 'versionCode': '', 'versionName': '',
               "localPath": ''}

    def getAppBaseInfo(self, param_apk_path):
        get_info_command = "aapt dump badging %s" % (param_apk_path)
        output = os.popen(get_info_command).read()
        match = re.compile(
            "package: name='(\S+)' versionCode='(\d+)' versionName='(\S+)'").match(output)
        if not match:
            print(output)
            raise Exception("can't get packageinfo")

        packageName = match.group(1)
        versionCode = match.group(2)
        versionName = match.group(3)
        # print(u" 包名：%s \n 版本号：%s \n 版本名称：%s " % (packageName,
        # versionCode,
        # versionName))
        self.apkInfo['packageName'] = packageName
        self.apkInfo['versionCode'] = versionCode
        self.apkInfo['versionName'] = versionName
        self.apkInfo['localPath'] = param_apk_path
        self.apkInfo['channel'] = get_channel(param_apk_path)
        self.apkInfo['md5'] = md5(param_apk_path)
        self.apkInfo['length'] = file_size(param_apk_path)
