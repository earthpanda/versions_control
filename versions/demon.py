import filehelper,os

print(filehelper.getCurrentPath())


filehelper.writeFileString("test","test.txt","this is a test",True)
filehelper.writeFileString("one\\two\\three","test.txt","this is a test",True)



