# -*- coding: utf-8 -*-
# (C) WangLi, Inc. 2019
# All rights reserved
# Licensed under Simplified BSD License (see LICENSE)

"""
apk上传固件小工具
"""
import apk
import sys
import random
from PyQt5.QtGui import QFont, QColor
from PyQt5.QtCore import Qt
from PyQt5 import QtWidgets
import re
import os

from server_handler import ServerClient

from PyQt5.QtWidgets import (QWidget, QHBoxLayout, QTableWidget, QPushButton,
                             QApplication, QVBoxLayout, QTableWidgetItem, QCheckBox, QAbstractItemView,
                             QHeaderView, QLabel, QFrame, QTableWidget,
                             QGridLayout, QRadioButton, QLineEdit, QTextEdit, QFileDialog)


class Main(QWidget):
    """
    apk上传工具主界面，整体分为左右两个纵向布局
    """

    def __init__(self):
        super().__init__()
        self.platform_kinds = ['F1', 'B1', 'C1', 'D1']
        self.init_ui()
        self.serverClient = ServerClient()

    def init_ui(self):
        """
        初始化布局，整体界面在这里完成搭建
        """
        # 设置位置和大小
        self.setGeometry(400, 100, 1000, 800)
        self.setWindowTitle('文件上传以及信息打印')
        upload_label = QLabel("需要上传的apk，拖拽文件进入")

        drag_table = DragTable(10, 6)
        drag_table.setHorizontalHeaderLabels(['包名', '版本号', '版本名称',
                                              '重命名', '渠道', '服务端路径'])
        drag_table.setAcceptDrops(True)

        platform_layout = QGridLayout()
        platform_position = [(i, j) for i in range(0, 2) for j in range(0, 2)]

        for platform, position in zip(self.platform_kinds, platform_position):
            platform_radio = QRadioButton(platform, self)
            platform_radio.setObjectName(platform)
            platform_layout.addWidget(platform_radio, *position)

        apk_down_path_label = QLabel("服务端apk下载文件目录")
        self.l_edit_down_path = QLineEdit()
        self.l_edit_down_path.setText(os.path.abspath('.'))
        btn_select_down_path = QPushButton("选择apk下载目录")

        file_path_label = QLabel("apk提交信息记录文件保存路径")
        self.l_edit_file_path = QLineEdit()
        self.l_edit_file_path.setText(os.path.abspath('.'))
        btn_select_file_path = QPushButton("选择文件保存路径")

        remote_apk_label = QLabel("远程apk包信息")
        remote_apk_table = QTableWidget(10, 6)
        remote_apk_table.setHorizontalHeaderLabels(['包名', '版本号', '版本名称',
                                                    '重命名', '渠道', '服务端路径'])
        remote_apk_table.horizontalHeader().resizeSection(0, 200)
        remote_apk_table.horizontalHeader().resizeSection(5, 200)

        btn_action_down = QPushButton("下载apk并解析")
        log_view_label = QLabel("信息输出打印区")
        self.text_edit_log = QTextEdit()
        v_layout_actions = QVBoxLayout()
        open_file_btn = QPushButton("查看往期提交记录")
        upload_btn = QPushButton("上传文件")

        # 主界面主布局，横行布局，分为左右两部分
        h_main_layout = QHBoxLayout()
        v_left_layout = QVBoxLayout()
        v_right_layout = QVBoxLayout()
        h_main_layout.addLayout(v_left_layout)
        h_main_layout.addLayout(v_right_layout)

        # 左边布局添加控件
        v_left_layout.addWidget(upload_label)
        v_left_layout.addWidget(drag_table)
        v_left_layout.addWidget(apk_down_path_label)
        v_left_layout.addWidget(self.l_edit_down_path)
        v_left_layout.addWidget(file_path_label)
        v_left_layout.addWidget(self.l_edit_file_path)
        v_left_layout.addWidget(remote_apk_label)
        v_left_layout.addWidget(remote_apk_table)
        v_left_layout.addWidget(log_view_label)
        v_left_layout.addWidget(self.text_edit_log)

        # 右边布局添加控件
        v_right_layout.addLayout(platform_layout)
        v_right_layout.addWidget(btn_select_down_path)
        v_right_layout.addWidget(btn_select_file_path)
        v_right_layout.addWidget(btn_action_down)
        v_right_layout.addWidget(open_file_btn)
        v_right_layout.addWidget(upload_btn)
        v_right_layout.addStretch(1)

        btn_select_down_path.clicked.connect(
            lambda: self.openDirDialog(self.l_edit_down_path))
        btn_select_file_path.clicked.connect(
            lambda: self.openDirDialog(self.l_edit_file_path))
        btn_action_down.clicked.connect(self.downApks)

        self.setLayout(h_main_layout)
        self.show()

    def openDirDialog(self, line_edit):
        path = QFileDialog.getExistingDirectory(self, "", "./")
        line_edit.setText(path)

    def downApks(self):
        self.serverClient.login()
        log = self.serverClient.download_apks()
        self.text_edit_log.setText(log)
        log_branch = self.serverClient.getBranch()
        self.text_edit_log.insertPlainText(log_branch)


class DragTable(QTableWidget):
    """
    自定义可以拖拽文件进入的表格控件
    """

    def __init__(self, row, column):
        super().__init__(row, column)
        self.setAcceptDrops(True)
        self.horizontalHeader().resizeSection(0, 200)
        self.horizontalHeader().resizeSection(5, 200)

    def dropEvent():
        print("ignore")

    def dragEnterEvent(self, dragEnterEvent):
        urls = dragEnterEvent.mimeData().urls()
        i = 0
        for url in urls:
            url_use = url.toString().replace("file:///", "/")
            apkParser = apk.ApkParser()
            apkParser.getAppBaseInfo(url_use)
            print(apk.ApkParser.apkInfo)
            self.setItem(i, 0, QTableWidgetItem(
                apk.ApkParser.apkInfo["packagename"]))
            self.setItem(i, 1, QTableWidgetItem(
                apk.ApkParser.apkInfo["versionCode"]))
            self.setItem(i, 2, QTableWidgetItem(
                apk.ApkParser.apkInfo["versionName"]))
            i += 1


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Main()
    sys.exit(app.exec_())
