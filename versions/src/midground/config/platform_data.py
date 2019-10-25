package_name_map_f1 = {"com.dangbei.leard.leradlauncher": "LeradLauncher",
                       "com.dangbei.lerad.etna.sample": "Etna",
                       "com.tv.filemanager.os": "FileManager",
                       "com.dangbei.lerad.andes": "LeradAndes",
                       "com.aispeech.tvui": "Tvui",
                       "com.dangbei.speech": "SpeechClient",
                       "com.dangbei.lerad.screensaver": "ScreenSaver",
                       "com.dangbei.leard.literacy": "DangbeiShizi",
                       "com.dangbei.leard.settings": "LeradSettings"}

package_name_map_b1 = {"com.dangbei.leard.leradlauncher.b2": "LeradLauncher",
                       "com.dangbei.lerad.etna.sample": "Etna",
                       "com.tv.filemanager.os": "FileManager",
                       "com.dangbei.lerad.andes": "LeradAndes",
                       "com.aispeech.tvui": "Tvui",
                       "com.dangbei.speech": "SpeechClient",
                       "com.dangbei.lerad.screensaver": "ScreenSaver",
                       "com.dangbei.zhushou.os": "DangbeiShizi"}

final_name_platform = {"F1": package_name_map_f1, "B1": package_name_map_b1}

pre_install_apks = ["com.dangbei.leard.literacy"]

remote_work_parent_dir = "/home/user/workspace/work"

remote_code_path = {"F1": "/home/user/workspace/work/mstar938vfc/code",
                    "B1": "/home/user/workspace/work/AmlogicS912Box/code",
                    "C1": "",
                    "D1": ""}

remote_system_apk_path = {"F1": "/home/user/workspace/work/mstar938vfc/code/vendor/mstar/dangs/systemapk",
                          "B1": "/home/user/workspace/work/AmlogicS912Box/code/vendor/dangs/systemapk",
                          "C1": "",
                          "D1": ""}

remote_pre_install_path = {"F1": "/home/user/workspace/work/mstar938vfc/code/vendor/mstar/dangs/preinstall",
                           "B1": "/home/user/workspace/work/AmlogicS912Box/code/vendor/dangs/preinstall",
                           "C1": "",
                           "D1": ""}

remote_tvui_path = {"F1": "/home/user/workspace/work/mstar938vfc/code/device/mstar/mangosteen/apps/Tvui",
                    "B1": "/home/user/workspace/work/mstar938vfc/code/vendor/mstar/dangs/systemapk",
                    "C1": "",
                    "D1": ""}


main_standard_data = {
    "model": "F1",
    "code": "20800",
    "content": [{
        "versionName": "f1_20800",
        "versionCode": "20800",
        "packageName": "com.dangbei.xxx",
        "md5": "xxxx",
        "length": "11111",
        "channel": "DBOS_F1"}]
}



# for key, value in package_name_map.items():
# print("key is " + key, "--value is " + value)
# for key, value in main_standard_data.items():
# print("key is " + key, "--value is " + value)
