import os, re, _locale, hashlib

_locale._getdefaultlocale = (lambda *args: ['en_US', 'utf8'])


# 传入aapt路径和文件路径
# 返回packagename,versionCode,versionName
def get_app_base_info(parm_aapt_path, parm_apk_path):
    get_info_command = "%s dump badging %s" % (parm_aapt_path, parm_apk_path)
    output = os.popen(get_info_command).read()
    match = re.compile("package: name='(\S+)' versionCode='(\d+)' versionName='(\S+)'").match(
        output)  # 通过正则匹配，获取包名，版本号，版本名称
    if not match:
        print(output)
        raise Exception("can't get packageinfo")
    return match.group(1), match.group(2), match.group(3)


# 在android->defaultConfig中buildConfigField "String", "CHANNEL"同级的地方
# 添加：resValue "string", "defaultChannelLib"（名字随意不和现有string资源重复）,
# "<channel>" + （channel的获取方式和上面CHANNEL一样）+ "</channel>"
def get_channle(parm_aapt_path, parm_apk_path):
    get_info_command = "%s dump strings %s" % (parm_aapt_path, parm_apk_path)
    output = os.popen(get_info_command).read()
    match = re.compile("String #(\d+): <channel>(\S+)</channel>").search(output)
    if not match:
        return "unknown"
        # raise Exception("can't get getChannle")
    return match.group(2)


# 传入文件路径，返回md5
def md5(parm_apk_path):
    if not os.path.isfile(parm_apk_path):
        return
    myHash = hashlib.md5()
    f = open(parm_apk_path, 'rb')
    while True:
        b = f.read(8096)
        if not b:
            break
        myHash.update(b)
    f.close()
    return myHash.hexdigest()


# 获取文件大小，返回字节
def file_size(parm_apk_path):
    size = os.path.getsize(parm_apk_path)
    return size


# 字节bytes转化kb\m\g
def format_size(bytes):
    try:
        bytes = float(bytes)
        kb = bytes / 1024
    except:
        print("传入的字节格式不对")
        return "Error"

    if kb >= 1024:
        M = kb / 1024
        if M >= 1024:
            G = M / 1024
            return "%fG" % (G)
        else:
            return "%fM" % (M)
    else:
        return "%fkb" % (kb)
