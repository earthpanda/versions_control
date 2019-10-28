
### 查看pip是否已经安装

pip --version 

默认 Python 2.7.9 + 或 Python 3.4+ 以上版本都自带 pip 工具

### 配置pyqt5

#### 检查本机python 版本：
python

#### 安装Qt5 执行如下指令：
pip install PyQt5 -i https://pypi.douban.com/simple

#### 将pyqt5-tools添加到全局环境变量（Path）中

D:\program\Python37\Lib\site-packages\PyQt5


#### 验证Qt5 是否安装成功，编写如下代码：

```java

import sys
from PyQt5 import QtWidgets
 
app = QtWidgets.QApplication(sys.argv)
widget = QtWidgets.QWidget()
widget.resize(360, 360)
widget.setWindowTitle("hello, pyqt5")
widget.show()
sys.exit(app.exec())

```

#### 删除PyQt5

pip uninstall PyQt5

#### 配置aapt环境变量
