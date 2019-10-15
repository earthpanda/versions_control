from versions.src.util import filehelper

print(filehelper.get_current_path())


filehelper.write_file_string("test", "test.txt", "this is a test", False)
filehelper.write_file_string("one\\two\\three", "test.txt", "this is a test", False)

print(filehelper.read_file_string("one\\two\\three\\four\\test.txt"))
print(filehelper.read_file_string("one\\two\\three\\test.txt"))



