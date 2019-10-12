class ApkEntity:
    def __init__(self, devicename, channel, packagename, vername, vercode, filesize, md5):
        self.devicename = devicename
        self.channel = channel
        self.packagename = packagename
        self.vername = vername
        self.vercode = vercode
        self.filesize = filesize
        self.md5 = md5

    def toString(self):
        print("apkEntity =", self.devicename, self.channel, self.packagename, self.vername, self.vercode, self.filesize, self.md5)
