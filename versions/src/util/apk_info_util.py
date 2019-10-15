import os

# 获取当前文件夹下全部文件，以创建的时间升级排序，返回最早创建的文件路径
# file_dir表示完整的文件夹路径，例如：xx/xx/versions_control/versions/document
def get_farthest_file(file_dir):
    lists = os.listdir(file_dir)
    lists.sort(key=lambda fn:os.path.getctime(file_dir + os.sep + fn))
    # 传入-1表示最晚创建的文件
    file_path = os.path.join(file_dir, lists[0])
    return file_path