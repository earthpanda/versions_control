# -*- coding: utf-8 -*-
# (C) WangLi, Inc. 2019
# All rights reserved
# Licensed under Simplified BSD License (see LICENSE)

"""
apk上传固件小工具
"""

import shutil
import sys

from PyQt5.QtGui import QTextCursor
from PyQt5.QtWidgets import *

from src.midground.config.mid_platform_data import *
from src.midground.file.midapk import *
from src.midground.file.midserver import ServerClient
from src.util.apk_info_reader import *


class Main(QWidget):
    """
    apk上传工具主界面，整体分为左右两个纵向布局
    """

    def __init__(self):
        super().__init__()
        self.l_edit_version = QLineEdit()
        self.remote_branch_combobox = QComboBox()
        self.text_edit_log = QTextEdit()
        self.remote_apk_table = QTableWidget(15, 6)
        self.drag_table = DragTable(15, 6)
        self.platform_kinds = ['F1', 'B1', 'C1', 'D1']
        self.current_platform = "F1"
        self.serverClient = ServerClient()
        self.init_ui()

    def init_ui(self):
        """
        初始化布局，整体界面在这里完成搭建
        """
        # 设置位置和大小
        self.setGeometry(250, 100, 1200, 800)
        self.setWindowTitle('文件上传以及信息打印')
        upload_label = QLabel("需要上传的apk，拖拽文件进入")

        self.drag_table.setHorizontalHeaderLabels(['包名', '版本号', '版本名称',
                                                   '重命名', '渠道', '服务端路径'])
        self.drag_table.setAcceptDrops(True)

        platform_layout = QGridLayout()
        platform_position = [(i, j) for i in range(0, 2) for j in range(0, 2)]

        for platform, position in zip(self.platform_kinds, platform_position):
            platform_radio = QRadioButton(platform, self)
            platform_radio.setObjectName(platform)
            if platform == self.current_platform:
                platform_radio.setChecked(True)
            platform_radio.toggled.connect(self.change_platform)
            platform_layout.addWidget(platform_radio, *position)

        # 手动输入版本号信息区域
        label_note_version = QLabel("请输入版本号:")
        size_policy = self.l_edit_version.sizePolicy()
        size_policy.setHorizontalPolicy(QSizePolicy.Preferred)
        self.l_edit_version.setSizePolicy(size_policy)

        apk_down_path_label = QLabel("服务端apk下载文件目录")
        l_edit_down_path = QLineEdit()
        l_edit_down_path.setText(os.path.abspath('./remote_apks'))
        btn_select_down_path = QPushButton("选择apk下载目录")
        btn_open_download_path = QPushButton("打开当前系统的下载目录")

        file_path_label = QLabel("apk提交信息记录文件保存路径")
        l_edit_file_path = QLineEdit()
        l_edit_file_path.setText(os.path.abspath('.'))
        btn_select_file_path = QPushButton("选择文件保存路径")

        remote_apk_label = QLabel("远程apk包信息")
        self.remote_apk_table.setHorizontalHeaderLabels(['包名', '版本号', '版本名称',
                                                         '重命名', '渠道', '服务端路径'])
        self.remote_apk_table.horizontalHeader().resizeSection(0, 220)
        self.remote_apk_table.horizontalHeader().resizeSection(5, 380)

        btn_action_down = QPushButton("下载apk并解析")
        log_view_label = QLabel("信息输出打印区")
        open_file_btn = QPushButton("查看往期提交记录")
        upload_btn = QPushButton("上传文件")

        select_branch_label = QLabel("请选择需要切换的分支名")

        btn_checkout_branch = QPushButton("切换到选中分支")

        # 主界面主布局，横行布局，分为左右两部分
        h_main_layout = QHBoxLayout()
        v_left_layout = QVBoxLayout()
        v_right_layout = QVBoxLayout()
        h_main_layout.addLayout(v_left_layout)
        h_main_layout.addLayout(v_right_layout)

        # 左边布局添加控件
        v_left_layout.addWidget(upload_label)
        v_left_layout.addWidget(self.drag_table)
        v_left_layout.addWidget(apk_down_path_label)
        v_left_layout.addWidget(l_edit_down_path)
        v_left_layout.addWidget(file_path_label)
        v_left_layout.addWidget(l_edit_file_path)
        v_left_layout.addWidget(remote_apk_label)
        v_left_layout.addWidget(self.remote_apk_table)
        v_left_layout.addWidget(log_view_label)
        v_left_layout.addWidget(self.text_edit_log)

        # 右边布局添加控件
        v_right_layout.addLayout(platform_layout)
        v_right_layout.addWidget(label_note_version)
        v_right_layout.addWidget(self.l_edit_version)
        v_right_layout.addWidget(btn_select_down_path)
        v_right_layout.addWidget(btn_open_download_path)
        v_right_layout.addWidget(btn_select_file_path)
        v_right_layout.addWidget(btn_action_down)
        v_right_layout.addWidget(open_file_btn)
        v_right_layout.addWidget(upload_btn)
        v_right_layout.addWidget(select_branch_label)
        v_right_layout.addWidget(self.remote_branch_combobox)
        v_right_layout.addWidget(btn_checkout_branch)
        v_right_layout.addStretch(1)

        btn_select_down_path.clicked.connect(
            lambda: self.open_dir_dialog(l_edit_down_path))
        btn_open_download_path.clicked.connect(
            lambda: self.open_download_dialog(gl.default_local_download_apk_path))
        btn_select_file_path.clicked.connect(
            lambda: self.open_dir_dialog(l_edit_file_path))
        btn_action_down.clicked.connect(self.down_apks)
        btn_checkout_branch.clicked.connect(lambda:
                                            self.checkout_branch(self.remote_branch_combobox.currentText()))
        upload_btn.clicked.connect(self.upload_apks)

        self.setLayout(h_main_layout)
        self.show()
        # 登录服务器
        self.serverClient.login(self.show_infos)
        # 获取分支名称
        self.serverClient.getBranch(self.show_infos, self.init_combo_box)

        # 生成需要使用的文件夹路径
        download_path_f1 = "./remote_apks/F1"
        download_path_b1 = "./remote_apks/B1"
        cache_path = "./cache_apks"
        if not os.path.exists(download_path_f1):
            os.makedirs(download_path_f1)

        if not os.path.exists(download_path_b1):
            os.makedirs(download_path_b1)

        if not os.path.exists(cache_path):
            os.makedirs(cache_path)

    def auto_scroll_text_edit(self):
        cursor = self.text_edit_log.textCursor()
        cursor.movePosition(QTextCursor.End)
        self.text_edit_log.setTextCursor(cursor)

    def open_dir_dialog(self, line_edit):
        path = QFileDialog.getExistingDirectory(self, "", "./")
        if path:
            line_edit.setText(path)

    def open_download_dialog(self, current_path):
        files, filetype = QFileDialog.getOpenFileNames(self,
                                                       "多文件选择",
                                                       current_path,  # 起始路径
                                                       "All Files (*);;PDF Files (*.pdf);;Text Files (*.txt)")
        if len(files) == 0:
            print("\n取消选择")
            return
        print("\n你选择的文件为:")
        for file in files:
            print(file)
        self.drag_table.parse_apks(files)

    def down_apks(self):
        self.serverClient.download_apks(self.current_platform, self.show_infos)
        self.parse_remote_apks()

    def parse_remote_apks(self):
        parser = ApkParser()
        remote_apk_path = local_path_parent[self.current_platform]
        files = os.listdir(remote_apk_path)
        i = 0
        for file in files:
            if file.endswith("apk"):
                remote_apk = os.path.join(remote_apk_path, file)
                parser.getAppBaseInfo(remote_apk)
                apk_info = parser.apkInfo
                self.remote_apk_table.setItem(i, 0,
                                              QTableWidgetItem(apk_info["packageName"]))
                self.remote_apk_table.setItem(i, 1,
                                              QTableWidgetItem(apk_info["versionCode"]))
                self.remote_apk_table.setItem(i, 2,
                                              QTableWidgetItem(apk_info["versionName"]))
                i += 1

    def change_platform(self):
        sender = self.sender()
        if sender.isChecked():
            self.current_platform = sender.text()
            self.drag_table.set_platform(self.current_platform)
            print(self.current_platform)

    def show_infos(self, info):
        self.text_edit_log.append(info)
        self.auto_scroll_text_edit()

    def init_combo_box(self, branch):
        self.remote_branch_combobox.addItems(branch)

    def checkout_branch(self, branch):
        cmd = 'git checkout {}'.format(branch.strip())
        print(cmd)

    def upload_apks(self):
        version_code = self.l_edit_version.text()
        if not version_code:
            QMessageBox.about(self, 'error', '请输入本地提交版本号')
            return
        main_data = self.drag_table.get_main_data()
        if main_data:
            main_data["code"] = version_code
            self.serverClient.push_apks(main_data["content"], self.show_infos)
            apk_infos_json = json.dumps(main_data)
            print("提交日志" + apk_infos_json)
            update_apk_infos(apk_infos_json)

    def get_table_infos(self):
        pass


class DragTable(QTableWidget):
    """
    自定义可以拖拽文件进入的表格控件
    """
    current_platform = "F1"

    def __init__(self, row, column):
        super().__init__(row, column)
        self.main_data = {}
        self.setAcceptDrops(True)
        self.horizontalHeader().resizeSection(0, 220)
        self.horizontalHeader().resizeSection(5, 380)

    def dropEvent():
        print("ignore")

    def dragEnterEvent(self, drag_enter_event):
        urls = drag_enter_event.mimeData().urls()
        url_uses = []
        for url in urls:
            print(os.name)
            if os.name == 'nt':
                url_use = url.toString().replace("file:///", "")
            else:
                url_use = url.toString().replace("file:///", "/")
            url_uses.append(url_use)
        self.parse_apks(url_uses)

    def parse_apks(self, urls):
        self.main_data = {"model": self.current_platform}
        content = []
        i = 0
        for url in urls:
            apk_parser = ApkParser()
            apk_parser.getAppBaseInfo(url)
            # print(ApkParser.apkInfo)
            apkInfo = apk_parser.apkInfo
            packageName = apkInfo["packageName"]
            self.setItem(i, 0, QTableWidgetItem(
                apkInfo["packageName"]))
            self.setItem(i, 1, QTableWidgetItem(
                apkInfo["versionCode"]))
            self.setItem(i, 2, QTableWidgetItem(
                apkInfo["versionName"]))
            # print("当前的平台为:" + self.current_platform)
            # print("apk的本地路径为---" + apk.ApkParser.apkInfo["localPath"])
            name_map = final_name_platform[self.current_platform]
            # print(name_map)
            # if packageName in platform_data.pre_install_apks:
            self.setItem(i, 3,
                         QTableWidgetItem(name_map[packageName]))
            # 对应平台 systemapk 远程地址
            system_apk_path = remote_system_apk_path[self.current_platform]
            # preinstall 远程地址
            pre_apk_path = remote_pre_install_path[self.current_platform]
            # Tvui 远程地址
            tvui_path = remote_tvui_path[self.current_platform]
            # 服务器具体地址
            if "com.dangbei.leard.literacy" == packageName:
                apkInfo["remote_full_path"] = (pre_apk_path + "/" +
                                               name_map[packageName] + ".apk")
            elif "com.aispeech.tvui" == packageName:
                apkInfo["remote_full_path"] = (tvui_path + "/" +
                                               name_map[packageName] + ".apk")
            else:
                apkInfo["remote_full_path"] = (system_apk_path + "/" +
                                               name_map[packageName] + ".apk")
            simple_path = apkInfo["remote_full_path"].replace(
                remote_work_parent_dir, "${work}")
            self.setItem(i, 5,
                         QTableWidgetItem(simple_path))

            channel = get_channel(url)
            self.setItem(i, 4, QTableWidgetItem(channel))
            apkInfo["rename"] = (
                final_name_platform[self.current_platform][packageName])
            content.append(apkInfo)
            i += 1
        self.main_data["content"] = content
        print(self.main_data)
        self.move_rename_apk()

    def move_rename_apk(self):
        main_data = self.main_data
        if main_data:
            # 所有apk的信息内容
            local_apks = main_data["content"]
            for local_apk in local_apks:
                local_path = local_apk["localPath"]
                if os.path.exists(local_path):
                    # 上传前改名apk的路径地址
                    local_rename_path = "./cache_apks/{}.apk".format(
                        local_apk["rename"])
                    shutil.copy(local_path, local_rename_path)
                    abs_path = os.path.abspath(local_rename_path)
                    local_apk["local_cache_path"] = abs_path
        # apk_infos_json = json.dumps(main_data)
        # print("移动后的数据" + apk_infos_json)
        # update_apk_infos(apk_infos_json)

    def set_platform(self, platform):
        self.current_platform = platform

    def get_main_data(self):
        return self.main_data


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Main()
    sys.exit(app.exec_())
