## Python开发规范

#### 命名规范

| Type |Public|Internal|
|-----|-----|------|-------|
|Modules|lower_with_under|_lower_with_under||
|Packages|lower_with_under|||
|Classes|CapWords|_CapWords||
|Exceptions|CapWords|||
|Functions|lower_with_under()|_lower_with_under()||
|Global/Class Constants|CAPS_WITH_UNDER	|_CAPS_WITH_UNDER||
|Global/Class Variables|lower_with_under	|lower_with_under||
|Instance Variables|lower_with_under	|_lower_with_under (protected) or __lower_with_under (private)||
|Method Names|lower_with_under()|_lower_with_under() (protected) or __lower_with_under() (private)||
|Function/Method Parameters|lower_with_under	|||
|Local Variables|lower_with_under|||


#### 应该避免的名称

```java

1.单字符名称
2.包/模块名中使用连字符(-)而不使用下划线(_)
3.双下划线开头并结尾的名称（如__init__）

```

#### 命名约定

```java

1.所谓”内部(Internal)”表示仅模块内可用, 或者, 在类内是保护或私有的.
2.用单下划线(_)开头表示模块变量或函数是protected的(使用import * from时不会包含).
3.用双下划线(__)开头的实例变量或方法表示类内私有.
4.将相关的类和顶级函数放在同一个模块里. 不像Java, 没必要限制一个类一个模块.
5.对类名使用大写字母开头的单词(如CapWords, 即Pascal风格), 但是模块名应该用小写加下划线的方式(如lower_with_under.py).

```

### 注释规范
#### 文档字符串

python使用文档字符串作为注释方式: 文档字符串是包, 模块, 类或函数里的第一个语句. 这些字符串可以通过对象的doc成员被自动提取, 并且被pydoc所用. 我们对文档字符串的惯例是使用三重双引号”“”( PEP-257 ).

一个文档字符串应该这样组织:
1. 首先是一行以句号, 问号或惊叹号结尾的概述(或者该文档字符串单纯只有一行). 接着是一个空行.
2. 接着是文档字符串剩下的部分, 它应该与文档字符串的第一行的第一个引号对齐.

```java

"""A user-created :class:`Response <Response>` object.
    
Used to xxx a :class: `JsonResponse <JsonResponse>`, which is xxx

:param data: response data
:param file: response files
    
Usage::

    >>> import api
    >>> rep = api.Response(url="http://www.baidu.com")
"""

```

#### 行内注释(PEP8)

注释需要和结构题对齐

```java

# if ....
if(True):
	# Compensate for border
	x = x + 1                

```

#### 模块

每个文件应该包含一个许可样板. 根据项目使用的许可(例如, Apache 2.0, BSD, LGPL, GPL), 选择合适的样板.

```java

# -*- coding: utf-8 -*-
# (C) JiaaoCap, Inc. 2017-2018
# All rights reserved
# Licensed under Simplified BSD License (see LICENSE)

```

#### 函数和方法

一个函数必须要有文档字符串注释

```java
"""Constructs and sends a :class:`Request <Request>`.
    
    :param method: method for the new :class:`Request` object.
    :param timeout: (optional) How many seconds to wait for the server to send data
        before giving up, as a float, or a :ref:`(connect timeout, read
        timeout) <timeouts>` tuple.
    :type timeout: float or tuple
    :return: :class:`Response <Response>` object
    :rtype: requests.Response
    
    Usage::
    
      >>> import requests
      >>> req = requests.request('GET', 'http://httpbin.org/get')
      <Response [200]>
"""
def simple_func(method, timeout)
   
```

### 类

类应该在其定义下有一个用于描述该类的文档字符串. 如果你的类有公共属性(Attributes), 那么文档中应该有一个属性(Attributes)段. 并且应该遵守和函数参数相同的格式.

```java
"""The built-in HTTP Adapter for urllib3.

    Provides a general-case interface for Requests sessions to contact HTTP and
    HTTPS urls by implementing the Transport Adapter interface.

    :param pool_connections: The number of urllib3 connection pools to cache.
    :param max_retries: The maximum number of retries each connection
        should attempt.

    Usage::

      >>> import requests
      >>> s = requests.Session()
      >>> a = requests.adapters.HTTPAdapter(max_retries=3)
      >>> s.mount('http://', a)
"""
class HTTPAdapter(BaseAdapter):

   
    def __init__(self, pool_connections, max_retries):
        self.pool_connections = pool_connections
        self.max_retries = max_retries


```

### 块注释和行注释

对于复杂的操作, 应该在其操作开始前写上若干行注释. 对于不是一目了然的代码, 应在其行上添加注释.

```java
# We use a weighted dictionary search to find out where i is in
# the array.  We extrapolate position based on the largest num
# in the array and the array size and then do binary search to
# get the exact number.

# true iff i is a power of 2
if i & (i-1) == 0:        

```

### 行长度

每行不超过80个字符
不要使用反斜杠连接行
Python会将 圆括号, 中括号和花括号中的行隐式的连接起来 , 你可以利用这个特点. 如果需要, 你可以在表达式外围增加一对额外的圆括号.

```java
NO:
query_sql = "SELECT image_id, image_o, image_width, image_height "\
            "FROM active_image_tbl "\
            "WHERE auction_id=:auction_id AND status=1 " \
            "ORDER BY image_id DESC"
   
YES:         
agent_sql = ("CREATE TABLE IF NOT EXISTS db_agent ("
             "id INTEGER PRIMARY KEY AUTOINCREMENT, "
             "device_id VARCHAR(128) DEFAULT '', "
             "status INTEGER DEFAULT 1, "
             "updated_time TIMESTAMP  DEFAULT CURRENT_TIMESTAMP, "
             "created_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP)")

```
```java

在注释中，如果必要，将长的URL放在一行上。
Yes: 
# See details at
# http://www.example.com/us/developer/documentation/api/content/v2.0/fication.html

```

#### 换行

使用4个空格来缩进代码
对于行连接的情况, 你应该要么垂直对齐换行的元素, 或者使用4空格的悬挂式缩进(这时第一行不应该有参数):

```java

# 垂直对齐换行的元素
foo = long_function_name(var_one, var_two,
                         var_three, var_four)


# 4空格的悬挂式缩进(这时第一行不应该有参数)
foo = long_function_name(
    var_one, var_two, var_three,
    var_four)

```

#### 空格

1. 括号内不要有空格

```java

YES:
spam(ham[1], {eggs: 2}, [])                 # 注意标点两边的空格

NO:
spam( ham[ 1 ], { eggs: 2 }, [ ] )

```

2. 不要在逗号，分号，冒号前面加空格，而应该在它们的后面加

```java

YES:
if x == 4:
    print x, y
x, y = y, x 

NO:
if x == 4 :
   print x , y
x , y = y , x

```


3. 二元操作符两边都要加上一个空格（=， ==，<, >, !=, in, not ...）
4. 当’=’用于指示关键字参数或默认参数值时

```java

def complex(real, imag=0.0): 
    return magic(r=real, i=imag)

```

5. 不要用空格来垂直对齐多行间的标记, 因为这会成为维护的负担(适用于:, #, =等)

```java
YES:
foo = 1000  # comment
long_name = 2  # comment that should not be aligned

NO:
foo       = 1000  # comment
long_name = 2     # comment that should not be aligned

```

#### 模块导入

1. 每个导入应该独占一行

```java

YES:
import os
import sys
from subprocess import Popen, PIPE      # PEP8

NO:
import sys, os

```

2. 模块导入顺序
	1. 标注库导入
	2. 第三方库导入
	3. 应用程序指定导入
3. 每种分组中, 应该根据每个模块的完整包路径按字典序排序, 忽略大小写.

```java

import foo
from foo import bar
from foo.bar import baz
from foo.bar import Quux
from Foob import ar

```

#### TODO注释

1. TODO注释应该在所有开头处包含”TODO”字符串, 紧跟着是用括号括起来的你的名字, email地址或其它标识符. 然后是一个可选的冒号. 接着必须有一行注释, 解释要做什么
2. 如果你的TODO是”将来做某事”的形式, 那么请确保你包含了一个指定的日期(“2009年11月解决”)或者一个特定的事件

```java

# TODO(kl@gmail.com): Use a "*" here for string repetition.
# TODO(Zeke) Change this to use relations.

```

#### 二元运算符换行(PEP8)

```java

# 不推荐: 操作符离操作数太远
income = (gross_wages +
          taxable_interest +
          (dividends - qualified_dividends) -
          ira_deduction -
          student_loan_interest)
 

# 推荐：运算符和操作数很容易进行匹配
income = (gross_wages
          + taxable_interest
          + (dividends - qualified_dividends)
          - ira_deduction
          - student_loan_interest)

```

### 其它规范

1. 不要在行尾加分号, 也不要用分号将两条命令放在同一行.
2. 除非是用于实现行连接, 否则不要在返回语句或条件语句中使用括号. 不过在元组两边使用括号是可以的.
3. 顶级定义之间空两行, 方法定义之间空一行

### Pandas使用规范

1. pandas数据结构命名 df_、se_
2. df取一列，禁止使用df.列名，可以使用df['列名'], 建议使用df.loc[:, '列名']
3. 禁止使用df.ix

### 目录结构示例

```java
|--docs
|--requests
|    |--__init__.py
|    |--_internal_utils.py
|    |--utils.py
|    |--api.py
|--tests
|--setup.py
|--README.rst
|--LICENSE  

```

### Class结构示例

```java

# -*- coding: utf-8 -*-
# (C) JiaaoCap, Inc. 2017-2018
# All rights reserved
# Licensed under Simplified BSD License (see LICENSE)

"""
requests.api

This module contains xxx. 
This module is designed to xxx.
"""

# stdlib
import os
import time

from base64 import b64encode

# 3p
try:
    import psutil
exception ImportError:
    psutil = None
import simplejson as json

# project
from .utils import current_time
from ._internal_utils import internal_func


class Response(object):
    """A user-created :class:`Response <Response>` object.
    
    Used to xxx a :class: `JsonResponse <JsonResponse>`, which is xxx
    
    :param data: response data
    :param file: response files
        
    Usage::
    
        >>> import api
        >>> rep = api.Response(url="http://www.baidu.com")
    """
    
    def __init__(self, data, files, json, url)
        self.data = data
    
    @staticmethod
    def _sort_params(params):
        """This is a private static method"""
        return params   

    def to_json():
        """The fully method blala bian shen,
        xxx sent to the server.
            
        Usage::
        
            >>> import api
            >>> rep = api.Response(url="http://www.baidu.com")
            >>> rep.to_json()
        """
        
        if self.url == "www":
            return True
        return False


```



 
