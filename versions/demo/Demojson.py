from versions.entity import ApkEntity
import json


class Demojson:
    def __init__(self):
        print("init")

    def test_serialize(self):
        apk = ApkEntity(
            "com.test.packagename",
            "1.0",
            1,
            "10M",
            "dddsdddddddddddssdsd")
        json1 = json.dumps(apk)
        print(json1)
