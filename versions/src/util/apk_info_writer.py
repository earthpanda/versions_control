from .filehelper import *
from ..apk.apk_info import *
from ..util.apk_info_util import *


class ApkInfoWriter:

    def write_to_file(self, apk_infos):
        for i in apk_infos:
            # 获取文件路径
            path = i.get_path()
            print(path)
            # 创建文件夹
            mkdir(path)
            # 获取当前路径下所有文件
            L = file_list(path)
            if len(L) > 10:
                os.remove(get_farthest_file(path))
            # 创建文件夹
            mkdir(path + os.sep + time)
