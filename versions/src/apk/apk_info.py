from ..entity.ApkEntity import *


class ApkInfo:
    arr = []

    # 创建apk实体类
    def create_apk_entity(self, device_type, channel, package_name, version_name, version_code, file_size, md5):
        apk_entity = ApkEntity(device_type, channel, package_name, version_name, version_code, file_size, md5)
        return apk_entity

    # 将apk放入集合中
    def add_apk_entity(self, apk_entity):
        self.arr.append(apk_entity)

    # 从集合中移除apk
    def remove_apk_entity(self, apk_entity):
        self.arr.remove(apk_entity)

    def __len__(self):
        return len(self.arr)

    def __getitem__(self, item):
        return self.arr[item]


if __name__ == '__main__':
    apk_info = ApkInfo()
    apk = apk_info.create_apk_entity(1, 1, 1, 1, 1, 1, 1)
    print(apk.to_string())
