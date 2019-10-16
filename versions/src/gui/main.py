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

from PyQt5.QtWidgets import (QWidget, QHBoxLayout, QTableWidget, QPushButton,
                             QApplication, QVBoxLayout, QTableWidgetItem, QCheckBox, QAbstractItemView,
                             QHeaderView, QLabel, QFrame, QTableWidget,
                             QGridLayout, QRadioButton, QLineEdit, QTextEdit)


class ui(QWidget):
    def __init__(self):
        super().__init__()
        self.platform_kinds = ['F1', 'B1', 'C1', 'D1']
        self.init_ui()

    def init_ui(self):
        self.setGeometry(400, 100, 800, 800)
        self.setWindowTitle('文件上传以及信息打印')
        v_main_layout = QVBoxLayout()
        upload_label = QLabel("需要上传的apk，拖拽文件进入")

        h_upload_table = QHBoxLayout()

        drag_table = DragTable(2, 6)
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
        h_layout_down_path = QHBoxLayout()
        l_edit_down_path = QLineEdit()
        btn_select_down_path = QPushButton("选择apk下载目录")
        h_layout_down_path.addWidget(l_edit_down_path)
        h_layout_down_path.setStretchFactor(l_edit_down_path, 5)
        h_layout_down_path.addWidget(btn_select_down_path)
        h_layout_down_path.setStretchFactor(btn_select_down_path, 1)

        file_path_label = QLabel("apk提交信息记录文件保存路径")
        h_layout_file_path = QHBoxLayout()
        l_edit_file_path = QLineEdit()
        btn_select_file_path = QPushButton("选择文件保存路径")
        h_layout_file_path.addWidget(l_edit_file_path)
        h_layout_file_path.setStretchFactor(l_edit_file_path, 5)
        h_layout_file_path.addWidget(btn_select_file_path)
        h_layout_file_path.setStretchFactor(btn_select_file_path, 1)

        remote_apk_label = QLabel("远程apk包信息")
        h_layout_remote_apk = QHBoxLayout()
        remote_apk_table = QTableWidget(3, 6)
        remote_apk_table.setHorizontalHeaderLabels(['包名', '版本号', '版本名称',
                                                    '重命名', '渠道', '服务端路径'])

        btn_action_down = QPushButton("下载apk并解析")
        h_layout_remote_apk.addWidget(remote_apk_table)
        h_layout_remote_apk.setStretchFactor(remote_apk_table, 5)
        h_layout_remote_apk.addWidget(btn_action_down)
        h_layout_remote_apk.setStretchFactor(btn_action_down, 1)

        log_view_label = QLabel("信息输出打印区")
        h_layout_log_view = QHBoxLayout()
        text_edit_log = QTextEdit()
        v_layout_actions = QVBoxLayout()
        open_file_btn = QPushButton("查看往期提交记录")
        upload_btn = QPushButton("上传文件")
        v_layout_actions.addWidget(open_file_btn)
        v_layout_actions.addWidget(upload_btn)
        h_layout_log_view.addWidget(text_edit_log)
        h_layout_log_view.setStretchFactor(text_edit_log, 5)
        h_layout_log_view.addLayout(v_layout_actions)
        h_layout_log_view.setStretchFactor(v_layout_actions, 1)

        # 添加上传文件信息显示表格
        h_upload_table.addWidget(drag_table)
        h_upload_table.setStretchFactor(drag_table, 5)
        # 添加平台单选列表
        h_upload_table.addLayout(platform_layout)
        h_upload_table.setStretchFactor(platform_layout, 1)
        # 添加上传文件拖拽提示
        v_main_layout.addWidget(upload_label)
        # 添加上传文件信息显示布局
        v_main_layout.addLayout(h_upload_table)
        v_main_layout.addWidget(apk_down_path_label)
        v_main_layout.addLayout(h_layout_down_path)
        v_main_layout.addWidget(file_path_label)
        v_main_layout.addLayout(h_layout_file_path)
        v_main_layout.addWidget(remote_apk_label)
        v_main_layout.addLayout(h_layout_remote_apk)
        v_main_layout.addWidget(log_view_label)
        v_main_layout.addLayout(h_layout_log_view)
        # 添加空白占位
        v_main_layout.addStretch(1)

        self.setLayout(v_main_layout)
        self.show()


class DragTable(QTableWidget):
    """
    自定义可以拖拽文件进入的表格控件
    """

    def __init__(self, row, column):
        super().__init__(row, column)
        self.setAcceptDrops(True)
        # self.horizontalHeader().resizeSection(0, 250)

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
    ui = ui()
    sys.exit(app.exec_())
