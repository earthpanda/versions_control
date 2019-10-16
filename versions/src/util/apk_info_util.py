import os


# 获取当前文件夹下全部文件，以创建的时间升级排序，返回最早创建的文件路径
# file_dir表示完整的文件夹路径，例如：xx/xx/versions_control/versions/document
def get_farthest_file(file_dir):
    lists = os.listdir(file_dir)
    lists.sort(key=lambda fn: os.path.getctime(file_dir + os.sep + fn))
    # 传入-1表示最晚创建的文件
    file_path = os.path.join(file_dir, lists[0])
    return file_path


def mkdir(path):
    # 引入模块
    import os
    # 去除首位空格
    path = path.strip()
    # 去除尾部 \ 符号
    path = path.rstrip("\\")
    # 判断路径是否存在
    # 存在     True
    # 不存在   False
    exists = os.path.exists(path)
    # 判断结果
    if not exists:
        # 如果不存在则创建目录
        # 创建目录操作函数
        os.makedirs(path)
        print(path + ' 创建成功')
        return True
    else:
        # 如果目录存在则不创建，并提示目录已存在
        print(path + ' 目录已存在')
        return False


def file_list(file_dir):
    # root 当前目录路径
    # dirs 当前路径下所有子目录
    # files 当前路径下所有非目录的目录文件
    for root, dirs, files in os.walk(file_dir):
        return files
