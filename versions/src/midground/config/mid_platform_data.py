package_name_map_f1 = {"com.dangbei.leard.leradlauncher": "LeradLauncher",
                       "com.dangbei.lerad.etna.sample": "Etna",
                       "com.tv.filemanager.os": "FileManager",
                       "com.dangbei.lerad.andes": "LeradAndes",
                       "com.aispeech.tvui": "Tvui",
                       "com.dangbei.speech": "SpeechClient",
                       "com.dangbei.lerad.screensaver": "ScreenSaver",
                       "com.dangbei.leard.literacy": "DangbeiShizi",
                       "com.dangbei.leard.settings": "LeradSettings",
                       "com.dangbei.leard.mediaplayer": "LeradMediaPlayer",
                       "com.dangbei.joylink": "JoyLink",
                       "com.dangbei.lerad.leradwatcher": "LeradWatcher",
                       "com.dangbei.health.fitness.os": "Fitness",
                       "com.dangbei.mimir.pictureviewer": "PictureBrowser",
                       "com.dangbei.zhushou.os": "ProjectorManager",
                       "com.dangbei.leard.smarthome": "SmartHome",
                       "com.dangbei.lerad.ota3435": "ControllerOta"}

package_name_map_b1 = {"com.dangbei.leard.leradlauncher.b2": "LeradLauncher",
                       "com.dangbei.lerad.etna.sample": "Etna",
                       "com.tv.filemanager.os": "FileManager",
                       "com.dangbei.lerad.andes": "LeradAndes",
                       "com.aispeech.tvui": "Tvui",
                       "com.dangbei.speech": "SpeechClient",
                       "com.dangbei.lerad.screensaver": "ScreenSaver",
                       "com.dangbei.leard.literacy": "DangbeiShizi",
                       "com.dangbei.leard.settings": "LeradSettings",
                       "com.dangbei.leard.mediaplayer": "LeradMediaPlayer",
                       "com.dangbei.joylink": "JoyLink",
                       "com.dangbei.lerad.leradwatcher": "LeradWatcher",
                       "com.dangbei.health.fitness.os": "Fitness",
                       "com.dangbei.mimir.pictureviewer": "PictureBrowser",
                       "com.dangbei.zhushou.os": "ProjectorManager",
                       "com.dangbei.lerad.ota3435": "ControllerOta"}

package_name_map_c1 = {"com.dangbei.leradlauncher.p1": "LeradLauncher",
                       "com.dangbei.lerad.etna.sample": "Etna",
                       "com.tv.filemanager.os": "FileManager",
                       "com.dangbei.lerad.andes": "LeradAndes",
                       "com.aispeech.tvui": "Tvui",
                       "com.dangbei.speech": "SpeechClient",
                       "com.dangbei.lerad.screensaver": "ScreenSaver",
                       "com.dangbei.leard.literacy": "DangbeiShizi",
                       "com.dangbei.leard.settings": "LeradSettings",
                       "com.dangbei.leard.mediaplayer": "LeradMediaPlayer",
                       "com.dangbei.lerad.mediaplayer": "LeradMediaPlayer",
                       "com.dangbei.joylink": "JoyLink",
                       "com.dangbei.lerad.leradwatcher": "LeradWatcher",
                       "com.dangbei.health.fitness.os": "Fitness",
                       "com.dangbei.mimir.pictureviewer": "PictureBrowser",
                       "com.dangbei.zhushou.os": "ProjectorManager",
                       "com.dangbei.lerad.ota3435": "ControllerOta",
                       "com.dangbei.messageboard": "LeradMessageBoard",
                       "com.hpplay.happyplay.aw.new": "Lebo",
                       "com.dangbei.projector.direction.directionapplication": "LeradDirection"}

final_name_platform = {"F1": package_name_map_f1, "B1": package_name_map_b1, "C1": package_name_map_c1}

pre_install_apks = ["com.dangbei.leard.literacy", "com.hpplay.happyplay.aw.new",
                    "com.dangbei.projector.direction.directionapplication"]

remote_work_parent_dir = "/home/user/workspace/work"

remote_code_path = {"F1": "/home/user/workspace/work/mstar938vfc/code",
                    "B1": "/home/user/workspace/work/AmlogicS912Box/code",
                    "C1": "/home/user/workspace/work/msd6a358/code",
                    "D1": ""}

remote_system_apk_path = {"F1": "/home/user/workspace/work/mstar938vfc/code/vendor/mstar/dangs/systemapk",
                          "B1": "/home/user/workspace/work/AmlogicS912Box/code/vendor/dangs/systemapk",
                          "C1": "/home/user/workspace/work/msd6a358/code/vendor/dangs/systemapk",
                          "D1": ""}

remote_pre_install_path = {"F1": "/home/user/workspace/work/mstar938vfc/code/vendor/mstar/dangs/preinstall",
                           "B1": "/home/user/workspace/work/AmlogicS912Box/code/vendor/dangs/preinstall",
                           "C1": "/home/user/workspace/work/msd6a358/code/vendor/dangs/preinstall",
                           "D1": ""}

remote_tvui_path = {"F1": "/home/user/workspace/work/mstar938vfc/code/device/mstar/mangosteen/apps/Tvui",
                    "B1": "/home/user/workspace/work/AmlogicS912Box/code/vendor/dangs/systemapk",
                    "C1": "/home/user/workspace/work/msd6a358/code/vendor/dangs/systemapk",
                    "D1": ""}

local_path_parent = {
    "F1": "./remote_apks/F1",
    "B1": "./remote_apks/B1",
    "C1": "./remote_apks/C1"
}

tvui_properties_path = {
    "C1": "/home/user/workspace/work/msd6a358/code/device/mstar/bennet/apps/Tvui"
}

so_system_32_path = {
    "C1": "/home/user/workspace/work/msd6a358/code/vendor/dangs/systemlib"
}

so_system_64_path = {
    "C1": "/home/user/workspace/work/msd6a358/code/vendor/dangs/systemlib64"
}

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


def function():
    pass
