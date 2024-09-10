<h1 align="center">GameRobot</h1>
<p align="center">
    <img height="100" width="100" src="doc/assets/icon.png">
</p>
<p align="center">
    <a href=""><img src="https://img.shields.io/badge/Python-3.10+-3776AB.svg" alt="Python 3.10+"></a>
    <a href=""><img src="https://img.shields.io/badge/OS-Windows-00A4EF.svg" alt="OS Windows"></a>
    <a href=""><img src="https://img.shields.io/badge/QQ group-285669805-1685A9.svg" alt="OS Windows"></a>
</p>

> Don't make things too complicated.



### 什么是GameRobot？
<hr>

 - GameRobot是一个基于Python的，可拓展的，能够解析简单标记语言的自动化操作工具
 - GameRobot无需任何编程基础，你可以通过几行简单的纯文本命令完成游戏自动化脚本任务
 - GameRobot是开源且免费的，通过调用Win API来完成自动化操作
 - GameRobot拥有插件系统，任何人都可以编写自己的插件，然后分享给其他人使用
 - GameRobot仍在开发中，有许多不完善的地方，并且欢迎开发者们一同参与进来

### GameRobot能做什么？
<hr>

 - GameRobot能够方便地抓取窗口和子窗口的句柄
 - GameRobot能够通过调用Win API来实现后台截图
 - GameRobot能够模拟各种鼠标和键盘事件
 - GameRobot集成了Paddle的OCR模型，通过一行命令即可调用
 - ...

## 快速开始
<hr>

使用Conda进行环境安装，或者直接使用打包好的release版本
```shell
conda create -n gamerobot python=3.10
conda activate gamerobot
pip install -r requirements.txt
```

使用你喜欢的文本编辑器，创建一个文本文档，输入以下内容：
```bot
print text="Hello, GameRobot!"
```
运行main.py(或者main.exe)，选择`File` -> `Open` 打开你刚刚保存的文本文档，此时Output窗口内应为:
```
[2024-13-32 25:00:00] Initialization complete. 
[2024-13-32 25:01:00] Load bot code from C:/Users/.../GameRobot/code.txt 
```
选择`Run` -> `Run`(快捷键Ctrl+R)，此时Output窗口内应为:
```
[2024-13-32 25:02:00] Hello, GameRobot!
```
恭喜，你完成了第一个GameRobot脚本的编写！
## 基本语法
<hr>

请移步[Bot语法](doc/bot%20syntax.md)文档。

## 编写插件
请移步[Bot插件](doc/bot%20plugin.md)文档。



    