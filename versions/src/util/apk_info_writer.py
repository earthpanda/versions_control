from .filehelper import *
from ..apk.apk_info import *
from ..util.apk_info_util import *


class ApkInfoWriter:

    def write_to_file(self, apk_infos, callback):
        callback("本次写入apk信息，apk个数：" + str(len(apk_infos)) + "个")
        for i in apk_infos:
            # 获取文件路径
            path = i.get_path()
            callback("文件上传路径：" + path)
            # 创建文件夹
            mkdir(path)
            # 获取当前路径下所有文件
            L = file_list(path)
            if len(L) >= 10:
                os.remove(get_farthest_file(path))
            # 切换到当前文件路径下
            # os.chdir(path)
            # 生成文件路径
            file_name = format_time1() + ".txt"
            # 创建文件
            # file = open(file_name, "w")
            # 写入内容
            write_file_string(path, file_name, i.file_content(), False)
            callback("文件写入成功！")
