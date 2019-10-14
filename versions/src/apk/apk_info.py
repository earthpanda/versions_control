class ApkInfo:
    arr = []

    def create_apk_entity(self, devices_name, channel, package_name, version_name, version_code, file_size, md5):
        apk_entity = ApkEntity(devices_name, channel, package_name, version_name, version_code, file_size, md5)
        return apk_entity

    def add_apk_entity(self, apk_entity):
        self.arr.append(apk_entity)

    def remove_apk_entity(self, apk_entity):
        self.arr.remove(apk_entity)

    def __len__(self):
        return len(self.arr)

    def __getitem__(self, item):
        return self.arr[item]


if __name__ == '__main__':
    apk_info = ApkInfo()
    apk = apk_info.create_apk_entity(1, 1, 1, 1, 1)
    print(apk.toString())
