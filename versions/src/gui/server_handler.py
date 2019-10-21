# 基于ssh,用于连接远程服务器做操作：远程执行命令，上传或下载文件

import paramiko
import os
import re


class ServerClient:

    def __init__(self):
        self.remote_code_path = "/home/user/workspace/work/mstar938vfc/code"
        self.remote_path_parent = "/home/user/workspace/work/mstar938vfc/code/vendor/mstar/dangs/systemapk"
        self.local_path_parent = "/Users/nemoli/Downloads/remoteApks"
        self.sftp_client = None

    def login(self, callback):
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
        callback("登录服务器成功")

    def download_apks(self, callback):
        # 4. 打开sftp连接
        self.sftp_client = self.client.open_sftp()

        remote_apks = self.sftp_client.listdir(self.remote_path_parent)
        log = ""
        for apk in remote_apks:
            remote_path = self.remote_path_parent + "/" + apk
            local_path = self.local_path_parent + "/" + apk
            # sftp_client.get(remote_path, local_path)
            callback("下载文件:" + local_path)
            # print(remote_path)

    def push_apks(self, apkInfos, callback):
        if not self.sftp_client:
            self.sftp_client = self.client.open_sftp()
        for apkInfo in apkInfos:
            local_path = apkInfo["localPath"]
            remote_path = apkInfo["remote_full_path"]
            self.sftp_client.put(local_path, remote_path)
            callback("本地地址:{}--远程地址:{}".format(local_path, remote_path))

    def getBranch(self, callback, listBranchs):
        # 4.执行操作
        # 标准输入，标准输出，标准错误输出。
        cmd = 'cd {}; git branch'.format(self.remote_code_path)
        stdin, stdout, stderr = self.client.exec_command(cmd)
        # Execute a command on the SSH server.  A new `.Channel` is opened and
        # the requested command is executed.  The command's input and output
        # streams are returned as Python ``file``-like objects representing
        # stdin, stdout, and stderr.

        # 5.获取命令的执行结果
        # 使结果具有可读性
        res = stdout.read().decode('utf-8')
        print(res)
        branch_line = re.search('\* (\w+)', res)
        branch = branch_line.group(1)
        callback("当前服务端的分支为:" + branch)
        listBranchs(res.split("\n"))

    def run_command(self, command, callback):
        stdin, stdout, stderr = self.client.exec_command(command)
        res = stdout.read().decode('utf-8')
        print(res)
        callback(res)

    def logout(self, callback):
        # 6.断开连接
        self.client.close()
        callback("退出登录")

    def callback(self, log):
        print(log)


if __name__ == "__main__":
    client = ServerClient()
    # def log(result):
    # print(result)
    # client.login(client.callback)
    # client.download_apks(client.callback)
    # client.getBranch(client.callback, client.callback)
    # client.run_command("cd /home/user/workspace/work/mstar938vfc/code; pwd",
    # client.callback)
    # client.run_command('git checkout develop', client.callback)
