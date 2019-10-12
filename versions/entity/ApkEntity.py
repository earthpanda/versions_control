class ApkEntity:
    def __init__(self, packagename, vername, vercode, filesize, md5):
        self.packagename = packagename
        self.vername = vername
        self.vercode = vercode
        self.filesize = filesize
        self.md5 = md5

    def toString(self):
        print("apkEntity =", self.packagename, self.vername, self.vercode, self.filesize, self.md5)
