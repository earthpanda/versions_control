
import os,re,_locale
_locale._getdefaultlocale = (lambda *args: ['en_US', 'utf8'])

class ApkInfo:

    def __init__(self, name, code, vname):
        self.packagename = name
        self.versionCode = code
        self.versionName = vname

def getAppBaseInfo(parm_aapt_path, parm_apk_path):
    get_info_command ="%s dump badging %s" % (parm_aapt_path, parm_apk_path)
    output = os.popen(get_info_command).read() 
    match = re.compile("package: name='(\S+)' versionCode='(\d+)' versionName='(\S+)'").match(output) #通过正则匹配，获取包名，版本号，版本名称
    if not match:
        print(output)
        raise Exception("can't get packageinfo")

    p = ApkInfo(match.group(1),match.group(2),match.group(3))
    return p

def getChannle(parm_aapt_path, parm_apk_path):
    get_info_command ="%s dump strings %s" % (parm_aapt_path, parm_apk_path)
    output = os.popen(get_info_command).read()
    match = re.compile("String #(\d+): DBOS(\S+)").search(output) 
    if not match:
        raise Exception("can't get getChannle")
    return "DBOS" + match.group(2)
               

if __name__=='__main__':

    path = os.path.abspath(os.path.dirname(__file__)) + "\\"
    aapt_path = path + "tools\\aapt.exe"  
    apk_path = path + "Leradlauncher_vD1_2.0.8.0_debug.apk"   #apk地址
    #apk = getAppBaseInfo(aapt_path, apk_path)
    #print (u" 包名：%s \n 版本号：%s \n 版本名称：%s " % (apk.packagename, apk.versionCode, apk.versionName))
    print(getChannle(aapt_path, apk_path))

    
