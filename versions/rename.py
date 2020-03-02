from src.midground.config.mid_platform_data import *

f = open("应用包名参照.md", "w+")
f.writelines("|包原始名称|包名|固件包中规范名称|\r")
f.writelines("|---|---|---|\r")
for package, app_name in package_name_map_f1.items():
    f.writelines("||{}|{}|\r".format(package, app_name))
