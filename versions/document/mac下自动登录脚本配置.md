## shell脚本自动登录服务器

1. #### expect安装

   首先确定mac下是否已经安装expect，如何确定？

   mac自带控制台输入expect，推荐使用iTerm2

   ```
   # nemoli @ NemodeMacBook-Pro in ~ [9:40:57]
   $ expect
   expect1.1>    #不会报错，进入命令行则说明已经安装了expect
   ```

   安装expect命令，推荐用homebrew安装，brew之于mac，类似于yum之于linux。是管理软件的工具

   **安装**

   ```
   brew install expect
   ```

2. #### shell脚本

   编写登录服务端，并进入工作目录的shell脚本

   ```
   #! /usr/bin/expect
   
   set timeout 5
   spawn ssh user@192.168.18.168
   expect "*password"	
   send "123456\r"
   expect "Welcome"
   send "cd workspace/work/AmlogicS912Box/code\r"
   interact
   ```

   send命令相当于在服务端输入命令，例如 `send "cd workspace/work/AmlogicS912Box/code\r"` 就是cd到F1的工作路径下

3. #### 设置别名

   为了更加快速便捷登录服务器可以为脚本设置别名，在mac下设置如下。需要注意我这里使用的shell类型是zsh，mac默认的是bash，这两种设置环境变量的方法不同。这里以zsh为例

   1. 打开zsh的配置文件

      ```
      # nemoli @ NemodeMacBook-Pro in ~ [9:53:14]
      $ vim .zshrc
      ```

   2. 修改文件

      ```
      alias F1='/Users/nemoli/autoWork/romServer/loginF1.sh'
      ```

      配置好脚本的绝对路径就可以了

   最后只要在iTerm2中，输入F1就可以自动登录服务器并切换到F1的路径下，同理可以配置其它的平台，或者更改脚本让用户自己选择，如何改的更加智能，需要靠各位的才智了。