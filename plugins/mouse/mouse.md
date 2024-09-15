# GameRobot mouse Plugin

> 此插件用于模拟鼠标事件，通过Win32API实现


### mouse_move
移动鼠标到指定位置

参数：
 - handle: 句柄
 - pos: 目标位置坐标

### mouse_press
按住鼠标

参数：
 - handle: 句柄
 - pos: 目标位置坐标
 - button: 鼠标键，可选`left(默认)` `right` `middle`
 - duration: 按住所用时长，默认为1000ms

### mouse_click
单击鼠标

参数：
 - handle: 句柄
 - pos: 目标位置坐标
 - button: 鼠标键，可选`left(默认)` `right` `middle`

### mouse_double_click
双击鼠标

参数：
 - handle: 句柄
 - pos: 目标位置坐标
 - button: 鼠标键，可选`left(默认)` `right` `middle`
 - delay: 两次双击之间的延时，默认为10ms

### mouse_drag
匀速拖拽鼠标

参数：
 - handle: 句柄
 - pos: 起始位置坐标
 - pos2: 重点位置坐标
 - button: 鼠标键，可选`left(默认)` `right` `middle`
 - duration: 拖动所用时长，默认为10ms


