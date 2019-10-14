import filehelper,os

print(filehelper.getCurrentPath())


filehelper.writeFileString(os.sep+"file"+os.sep+"test.txt","this is a test",True)

filehelper.writeFileString(os.sep+"file"+os.sep+"test.txt","this is a test",True)

filehelper.writeFileString(os.sep+"file"+os.sep+"test.txt","this is a test",False)

