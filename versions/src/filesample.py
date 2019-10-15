import os
from util.filehelper import write_file_string,read_file_string,rename_file

s=os.path.join(os.getcwd(),"..","file")
print(s)


write_file_string(os.path.join(s,"one","two","three"), "test.txt", "this is a test in three ", False)
write_file_string(os.path.join(s,"test"), "test.txt", "this is a test", False)

print(read_file_string(os.path.join(s,"one","two","three","test.txt")))

rename_file(os.path.join(s,"test"), "test.txt","new.txt")
rename_file(os.path.join(s,"test"), "error.txt","new.txt")





