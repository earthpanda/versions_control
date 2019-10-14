from versions.src.util import filehelper

print(filehelper.getCurrentPath())


filehelper.writeFileString("test", "test.txt", "this is a test", False)
filehelper.writeFileString("one\\two\\three", "test.txt", "this is a test", False)

print(filehelper.readFileString("one\\two\\three\\four\\test.txt"))
print(filehelper.readFileString("one\\two\\three\\test.txt"))



