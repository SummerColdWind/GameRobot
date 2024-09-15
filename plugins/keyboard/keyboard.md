# GameRobot mouse Plugin

> 此插件用于模拟键盘事件，通过Win32API实现



### key_press
按住键盘按键

参数：
 - handle: 句柄
 - key: 键名
 - duration: 按住所用时长，默认为1000ms

### key_press_exact
按住键盘按键（精确计时）

参数：
 - handle: 句柄
 - key: 键名
 - duration: 按住所用时长，默认为1000ms

### key_click
单击某键

参数：
 - handle: 句柄
 - key: 键名

### key_type
键入一串字符

参数：
 - handle: 句柄
 - text: 输入文本
 - duration: 输入所用时长，默认为10ms


