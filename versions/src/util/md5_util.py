import hashlib


# 读取字符串MD5值
def str_md5(content):
    md5hash = hashlib.md5(content)
    md5 = md5hash.hexdigest()
    return md5


# 读取文件MD5值
def file_md5(path):
    with open(path, 'rb') as fp:
        data = fp.read()
    md5 = hashlib.md5(data).hexdigest()
    return md5


# 读取大文件MD5值
def large_file_md5(path):
    m = hashlib.md5()  # 创建md5对象
    with open(path, 'rb') as fo_bj:
        while True:
            data = fo_bj.read(4096)
            if not data:
                break
            m.update(data)  # 更新md5对象
    return m.hexdigest()  # 返回md5对象
