import os
from src.util.filehelper import write_file_string, read_file_string, rename_file, delete_file, copy_file
from src.midground.file.midfile import delete_apks
from src.entity.ApkEntity import *
from src.util.apk_info_writer import *
from src.apk.apk_info import *
import src.util.time



s=os.path.join(os.getcwd(),"file","test")

print(s)


# write_file_string(os.path.join(s,"one","two","three"), "test.txt", "this is a test in three ", False)
# write_file_string(os.path.join(s,"test"), "test.txt", "this is a test", False)

# print(read_file_string(os.path.join(s,"one","two","three","test.txt")))

# rename_file(os.path.join(s,"test"), "test.txt","new.txt")
# rename_file(os.path.join(s,"test"), "error.txt","new.txt")

# delete_file(os.path.join(s,"test","new.txt"),False)
# delete_file(os.path.join(s,"one"),True)
# delete_file(os.path.join(s,"unexist"),True)

# copy_file(os.path.join(s,"one","two","three","test.txt"),os.path.join(s,"one","two","three","test1.txt"))


delete_apks(s)


# def test():
#     apk_infos = ApkInfo()
#     apk1 = apk_infos.create_apk_entity("F1", "DBOS_F1", "launcher", "F12080", "2080", "100", "xc")
#     apk2 = apk_infos.create_apk_entity("C1", "DBOS_C1", "launcher", "C12080", "2080", "100", "xcc")
#     apk_infos.add_apk_entity(apk1)
#     apk_infos.add_apk_entity(apk2)

#     file_writer = ApkInfoWriter()
#     file_writer.write_to_file(apk_infos)


# if __name__ == '__main__':
#     test()
