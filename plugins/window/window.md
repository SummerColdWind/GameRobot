# GameRobot mouse Plugin

> 此插件用于抓取句柄，通过Win32API实现



### handle
获取父窗口句柄，返回符合所有条件的第一个句柄

参数：
 - title: 完整标题匹配
 - title_part: 部分标题匹配
 - cls: 完整窗口类名匹配
 - cls_part: 部分窗口类名匹配
 - width: 窗口宽度匹配
 - height: 窗口高度匹配
 - save: 保存为变量的名称，默认为__handle



### handle_child
获取父窗口句柄，返回符合所有条件的第一个句柄

参数：
 - name: 父窗口句柄变量名称，默认为__handle
 - title: 完整标题匹配
 - title_part: 部分标题匹配
 - cls: 完整窗口类名匹配
 - cls_part: 部分窗口类名匹配
 - width: 窗口宽度匹配
 - height: 窗口高度匹配
 - save: 保存为变量的名称，默认为__handle


