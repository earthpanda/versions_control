# 基于ssh,用于连接远程服务器做操作：远程执行命令，上传或下载文件
import paramiko
import os
import re


class ServerClient:

    def __init__(self):
        self.remote_code_path = "/home/user/workspace/work/mstar938vfc/code"
        self.remote_path_parent = "/home/user/workspace/work/mstar938vfc/code/vendor/mstar/dangs/systemapk"
        self.local_path_parent = "/Users/nemoli/Downloads/remoteApks"

    def login(self):
        # 创建一个ssh对象
        self.client = paramiko.SSHClient()

        # 2.解决问题：首次连接，会出现
        # Are you sure you want to continue connecting (yes/no)? yes
        # 自动选择yes

        # 允许连接不在know_hosts文件中的主机
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        # 3.连接服务器
        self.client.connect(hostname='192.168.18.168', port=22,
                            username='user', password='123456')

    def download_apks(self):
        # 4. 打开sftp连接
        sftp_client = self.client.open_sftp()

        remote_apks = sftp_client.listdir(self.remote_path_parent)
        log = ""
        for apk in remote_apks:
            remote_path = self.remote_path_parent + "/" + apk
            local_path = self.local_path_parent + "/" + apk

            # sftp_client.get(remote_path, local_path)
            # print(remote_path)
            log = log + remote_path + "\n"
        return log

    def getBranch(self):
        # 4.执行操作
        # 标准输入，标准输出，标准错误输出。
        cmd = 'cd {}; pwd; git branch'.format(self.remote_code_path)
        stdin, stdout, stderr = self.client.exec_command(cmd)
        # Execute a command on the SSH server.  A new `.Channel` is opened and
        # the requested command is executed.  The command's input and output
        # streams are returned as Python ``file``-like objects representing
        # stdin, stdout, and stderr.

        # 5.获取命令的执行结果
        # 使结果具有可读性
        res = stdout.read().decode('utf-8')
        print(res)
        return res

    def logout(self):
        # 6.断开连接
        self.client.close()


if __name__ == "__main__":
    client = ServerClient()
    client.login()
    log = client.download_apks()
    client.getBranch()
