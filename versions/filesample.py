import os
import json
import src.util.time
import sys
import paramiko
from PyQt5 import QtWidgets
from src.util.filehelper import write_file_string, read_file_string, rename_file, delete_file, copy_file
from src.midground.file.midfile import delete_apks, delete_all
from src.entity.ApkEntity import *
from src.util.apk_info_writer import *
from src.apk.apk_info import *
from src.midground.file.midapk import update_apk_infos, get_apk_infos


# write_file_string(os.path.join(s,"one","two","three"), "test.txt", "this is a test in three ", False)
# write_file_string(os.path.join(s,"test"), "test.txt", "this is a test", False)

# print(read_file_string(os.path.join(s,"one","two","three","test.txt")))

# rename_file(os.path.join(s,"test"), "test.txt","new.txt")
# rename_file(os.path.join(s,"test"), "error.txt","new.txt")

# delete_file(os.path.join(s,"test","new.txt"),False)
# delete_file(os.path.join(s,"one"),True)
# delete_file(os.path.join(s,"unexist"),True)

# copy_file(os.path.join(s,"one","two","three","test.txt"),os.path.join(s,"one","two","three","test1.txt"))


# delete_apks(s)
# delete_all(s)


# def print_log(log):
#     print(log)
#
#
# def test():
#     apk_infos = ApkInfo()
#     apk1 = apk_infos.create_apk_entity("F1", "DBOS_F1", "launcher", "F12080", "2080", "100", "xc")
#     apk2 = apk_infos.create_apk_entity("C1", "DBOS_C1", "launcher", "C12080", "2080", "100", "xcc")
#     apk_infos.add_apk_entity(apk1)
#     apk_infos.add_apk_entity(apk2)
#
#     file_writer = ApkInfoWriter()
#     file_writer.write_to_file(apk_infos, print_log)
#
#
# if __name__ == '__main__':
#     test()


# print(update_apk_infos(p))

# test={"model": "C1",
# 	"code": "20801"
# }


# print(get_apk_infos(json.dumps(test)))

# app = QtWidgets.QApplication(sys.argv)
# widget = QtWidgets.QWidget()
# widget.resize(360, 360)
# widget.setWindowTitle("hello, pyqt5")
# widget.show()
# sys.exit(app.exec())


def main():


	s={"model": "F1",
		"code": "20804",
		"content": [{
			"versionName": "f1_20800",
			"versionCode": "20806",
			"packageName": "com.dangbei.0",
			"md5": "xxxx",
			"length": "11112",
			"channel": "DBOS_F1"},{
			"versionName": "f1_20800",
			"versionCode": "20800",
			"packageName": "com.dangbei.2",
			"md5": "xxxxxxxxxx",
			"length": "11111",
			"channel": "DBOS_F1"}]
	}
	p = json.dumps(s)
	data = json.loads(p)
	root = os.getcwd()
	update_apk_infos(p)
	print(root)
	pass


# 增加调用main()函数
if __name__ == '__main__':
    main()
